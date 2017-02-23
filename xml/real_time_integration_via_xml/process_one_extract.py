# process_one_extract.py
# -*- coding: utf-8 -*-
from datetime import datetime
import xmltodict
from ebureau_real_time import generate_xml_request, call_ebureau_real_time
from xml.dom import minidom
import sqlalchemy
from sqlalchemy import text
from eb_rt_logger import make_a_logger

#Configure logger
logger = make_a_logger('eb_real_time_process_one')

CONN_STRING = 'postgresql://dev_u:u782nmt5@devmaindb01:5432/dev_ml_db'

# make sure the following two lists are cohesive
SELECT_SQL_STR = """SELECT cust_id, seqnum, fname, lname, addr1, city, state, zip5, ssn, dob 
                FROM batch_insurance2_matching_t 
                LIMIT 5;"""

FIELD_NAMES = ('cust_id','seqnum','first','last','address','city','state','zip','social','dob')

RUN_DATE = datetime.now().date()

EBUREAU_LOGIN_DATA = {    
            'userid': 'medly00003', 
            'password': 'cp96ah11wg18',
            'sid': 'xtech:locate:consumer:4'}

def get_accts_from_db(conn):
    sql_outs = conn.execute(text(SELECT_SQL_STR))

    for row in sql_outs:
        row_out = dict(zip(FIELD_NAMES, row))
        row_out['dob'] = row_out.get('dob').strftime("%Y%m%d")
        row_out['cust_id'] = str(row_out.get('cust_id'))
        # experimental
        row_out['subuserid'] = 'Locate 4'
        row_out['sourceid'] = 'eBureau Real Time'
        row_out['groupid'] = row_out.get('cust_id')
        row_out['account'] = row_out.get('seqnum')
        # scrub out backslahes and ampersand
        row_out['first'] = row_out.get('first', '').replace('&', '').replace('\\', '')
        row_out['last'] = row_out.get('last', '').replace('&', '').replace('\\', '')
        row_out['address'] = row_out.get('address', '').replace('&', '').replace('\\', '')
        row_out['city'] = row_out.get('city', '').replace('&', '').replace('\\', '')
        yield row_out

def prettify(rough_string):
    """Return a pretty-printed XML string for the Element.
    """
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

def truncate_tmp_tbl(conn):
    tranx = conn.begin()
    conn.execute('TRUNCATE temp_insurance2_ebureau_realtime_t RESTART IDENTITY;')
    tranx.commit()

def populate_tmp_tbl(conn, xml_payload):
    result = 0
    INSERT_SQL_STR = "INSERT INTO temp_insurance2_ebureau_realtime_t VALUES(XMLPARSE(DOCUMENT '{}'));".format(xml_payload)
    try:
        res = conn.execute(text(INSERT_SQL_STR))
        result = res.rowcount
        logger.info('{} record inserted into temp tbl ...'.format(result))
    except Exception as e:
        logger.error("Got db error: {}".format(e))
    
    return result

def handle_it_in_case_of_error(acct, conn, meta, payload):
    no_error = True
    data = xmltodict.parse(payload)
    if 'error' in data:
        no_error = False
        logger.error('Got error ...')
        err_keys = ('cust_id', 'our_run_date', 'seqnum')
        err = {k: acct.get(k) for k in err_keys}
        err['our_run_date'] = RUN_DATE
        err['eb_error_message'] = data['error']['message']
        try:
            res = conn.execute(meta.tables['insurance2_ebureau_error_t'].insert(), err)
            logger.error('{} record inserted into error tbl ...'.format(res.rowcount))
        except (sqlalchemy.exc.IntegrityError, sqlalchemy.exc.InternalError) as e:
            logger.error("Got db error: {}".format(e))

    return no_error


if __name__ == '__main__':
    db_engine = sqlalchemy.create_engine(CONN_STRING)
    with db_engine.connect() as conn:
        #meta = sqlalchemy.MetaData(bind=conn, reflect=True)
        meta = sqlalchemy.MetaData()
        #meta.reflect(db_engine, only=['insurance2_ebureau_error_t',])
        meta.reflect(conn, only=['insurance2_ebureau_error_t',])

        tranx = conn.begin()
        truncate_tmp_tbl(conn)
        accts = get_accts_from_db(conn)
        for acct in accts:
            #Aggravate an error with pain points
            #acct['sourceid'] = acct['last'] * 100
            #acct['sourceid'] = '§'
            xml_req = generate_xml_request(EBUREAU_LOGIN_DATA, acct)
            logger.info('++++++++++++ Request +++++++++++++')
            logger.info(xml_req)
            logger.info('..................................')
            resp = call_ebureau_real_time(xml_req)
            pretty_resp = prettify(resp)
            logger.info('++++++++++++++ Response ++++++++++++++++')
            logger.info(pretty_resp)
            logger.info('........................................')
            #Error handling
            no_error = handle_it_in_case_of_error(acct, conn, meta, pretty_resp)
            if no_error:
                result = populate_tmp_tbl(conn, pretty_resp)

        tranx.commit()
