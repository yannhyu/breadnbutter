# eBureau_real_time_async_process_one.py.py
# -*- coding: utf-8 -*-
from datetime import datetime
import xmltodict
from ebureau_real_time import package_xml_requests, async_calls2ebureau_real_time
from xml.dom import minidom
import sqlalchemy
from sqlalchemy import text
from eb_rt_logger import make_a_logger
import time
import random

# Configure logger
logger = make_a_logger('eb_real_time_async_process_one')

CONN_STRING = 'postgresql://username:passcode@luckystar:5432/dev_ml_db'

# Make sure the following two lists are cohesive
SELECT_SQL_STR = """SELECT cust_id, our_run_date, seqnum, fname, lname, addr1, city, state, zip5, ssn, dob 
                FROM payorintel.batch_insurance2_matching_t 
                LIMIT 997;"""

FIELD_NAMES = ('cust_id', 'our_run_date', 'seqnum','first','last','address','city','state','zip','social','dob')

EBUREAU_LOGIN_DATA = {    
            'userid': 'medly00003', 
            'password': 'cp96ah11wg18',
            'sid': 'xtech:locate:consumer:4'}

def get_accts_from_db(conn):
    result = []
    sql_outs = conn.execute(text(SELECT_SQL_STR))
    for row in sql_outs:
        row_out = dict(zip(FIELD_NAMES, row))
        row_out['dob'] = row_out.get('dob').strftime("%Y%m%d")
        row_out['cust_id'] = str(row_out.get('cust_id'))
        # experimental
        row_out['subuserid'] = 'Locate 4'
        row_out['sourceid'] = row_out.get('our_run_date')
        row_out['groupid'] = row_out.get('cust_id')
        row_out['account'] = row_out.get('seqnum')
        # scrub out backslahes and ampersand
        row_out['first'] = (row_out.get('first', '') or '').replace('&', '').replace('\\', '')
        row_out['last'] = (row_out.get('last', '') or '').replace('&', '').replace('\\', '')
        row_out['address'] = (row_out.get('address', '') or '').replace('&', '').replace('\\', '')
        row_out['city'] = (row_out.get('city', '') or '').replace('&', '').replace('\\', '')
        result.append(row_out)

    return result        

def prettify(rough_string):
    """Return a pretty-printed XML string for the Element.
    """
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

def truncate_tmp_tbl(conn):
    tranx = conn.begin()
    conn.execute('TRUNCATE payorintel.temp_insurance2_ebureau_realtime_t RESTART IDENTITY;')
    tranx.commit()

def populate_tmp_tbl(conn, xml_payload):
    result = 0
    INSERT_SQL_STR = "INSERT INTO payorintel.temp_insurance2_ebureau_realtime_t VALUES(XMLPARSE(DOCUMENT '{}'));".format(xml_payload)
    try:
        res = conn.execute(text(INSERT_SQL_STR))
        result = res.rowcount
        logger.info('{} record inserted into temp tbl ...'.format(result))
    except Exception as e:
        logger.error("Got db error: {}".format(e[:25]))
    
    return result

def handle_it_in_case_of_error(acct, conn, meta, payload):
    no_error = True
    data = xmltodict.parse(payload)
    if 'error' in data:
        no_error = False
        logger.error('Got error ...')
        err_keys = ('cust_id', 'our_run_date', 'seqnum')
        err = {k: acct.get(k) for k in err_keys}
        err['eb_error_message'] = data['error']['message']
        try:
            res = conn.execute(meta.tables['insurance2_ebureau_error_t'].insert(), err)
            logger.error('{} record inserted into error tbl ...'.format(res.rowcount))
        except (sqlalchemy.exc.IntegrityError, sqlalchemy.exc.InternalError) as e:
            logger.error("Got db error: {}".format(e[:25]))

    return no_error

def eBureau_requests_responses_manager(accts, conn, meta):
    if accts:
        # Experimental: use the last acct as base, add aggravator and include in output
        # genetically modify the last item accts[-1]
        #Aggravate an error pain points
        #accts[-1]['sourceid'] = accts[-1]['last'] * 100
        accts[-1]['sourceid'] = '§'

        reqs = package_xml_requests(EBUREAU_LOGIN_DATA, accts)
        resps = async_calls2ebureau_real_time(reqs)
        # accts, reqs and resps are in the same order
        for acct, resp in zip(accts, resps):
            tranx = conn.begin()
            if resp:
                pretty_resp = prettify(resp.content)
                logger.info('++++++++++++++ Response ++++++++++++++++')
                logger.info(pretty_resp)
                logger.info('........................................')
                #Error handling
                no_error = handle_it_in_case_of_error(acct, conn, meta, pretty_resp)
                if no_error:
                    result = populate_tmp_tbl(conn, pretty_resp)
                resp.close()
            tranx.commit()  

def chunks(l, n):
    """Split l into successive n-sized chunks """
    for i in range(0, len(l), n):
        yield l[i:i + n]


if __name__ == '__main__':
    start_time = time.time()
    db_engine = sqlalchemy.create_engine(CONN_STRING)
    with db_engine.connect() as conn:
        #tranx = conn.begin()
        truncate_tmp_tbl(conn)
        meta = sqlalchemy.MetaData()
        meta.reflect(conn, only=['insurance2_ebureau_error_t',])
        accts = get_accts_from_db(conn)
        if accts:
            # Split it across even sized chunk
            for chunk_of_accts in chunks(accts, 200):
                time.sleep(random.uniform(1.2, 1.5))
                eBureau_requests_responses_manager(chunk_of_accts, conn, meta)
       
        #tranx.commit()

    print("--- {} seconds ---".format(time.time() - start_time))