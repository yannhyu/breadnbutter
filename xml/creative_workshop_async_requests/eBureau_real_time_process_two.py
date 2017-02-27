# eBureau_real_time_process_two.py
import sqlalchemy
from sqlalchemy import text
import xmltodict
from datetime import datetime
import collections
from eb_rt_logger import make_a_logger

#Configure logger
logger = make_a_logger('eb_real_time_process_two')

CONN_STRING = 'postgresql://username:passcode@luckystardb:5432/dev_ml_db'

SELECT_SQL_STR = """SELECT payload 
                FROM payorintel.temp_insurance2_ebureau_realtime_t;
                """

def get_payloads(conn):
    sql_outs = conn.execute(text(SELECT_SQL_STR))
    for payload in sql_outs:
        yield payload[0]

def parse_n_store_in_eb_real_time(conn, payload):        
    data = xmltodict.parse(payload)
    uuid = data['root']['transaction']['status']['uuid']
    str_run_date = data['root']['transaction']['input']['account']['sourceid']
    our_run_date = datetime.strptime(str_run_date, "%Y-%m-%d %H:%M:%S")
    cust_id = data['root']['transaction']['input']['account']['groupid']
    seqnum = data['root']['transaction']['input']['account']['account']
    INSERT_SQL_TEMPL = """INSERT INTO payorintel.insurance2_ebureau_realtime_t 
                        (uuid, cust_id, our_run_date, seqnum, payload) 
                        VALUES('{0}', {1}, TIMESTAMP '{2}', {3}, XMLPARSE(DOCUMENT '{4}'))
                        RETURNING *;
                     """                   
    INSERT_SQL_STR = INSERT_SQL_TEMPL.format(uuid, cust_id, our_run_date, seqnum, payload)
    return conn.execute(text(INSERT_SQL_STR))

def parse_n_store_in_eb_address(conn, meta, payload):
    result = 0
    addresses = []
    data = xmltodict.parse(payload)
    str_run_date = data['root']['transaction']['input']['account']['sourceid']
    our_run_date = datetime.strptime(str_run_date, "%Y-%m-%d %H:%M:%S")    
    cust_id = data['root']['transaction']['input']['account']['groupid']
    seqnum = data['root']['transaction']['input']['account']['account']
    output = data['root']['transaction']['output']
    if 'address' in output:    # not always have address block
        addrs = output['address']
        if type(addrs) is collections.OrderedDict:
            addr = {}
            addr['cust_id'] = int(cust_id)
            addr['our_run_date'] = our_run_date
            addr['seqnum'] = int(seqnum)
            addr['eb_addr_fname'] = addrs.get('first', '')
            addr['eb_addr_lname'] = addrs.get('last', '')
            addr['eb_addr_addr1'] = (addrs.get('address', '') or '').replace('&', '').replace('\\', '')
            addr['eb_addr_city'] = addrs.get('city', '')
            addr['eb_addr_state'] = addrs.get('state', '')
            our_zip = addrs.get('zip', '')
            addr['eb_addr_zip5'] = our_zip[:5] or ''
            addr['eb_addr_zip4'] = our_zip[-4:] if len(our_zip) == 9 else ''
            addr['eb_addr_dob'] = addrs.get('dob', '')
            addr['eb_addr_match'] = addrs.get('match', '')
            addr['eb_addr_status'] = addrs.get('status', '')
            addr['eb_addr_score'] = int(addrs.get('score', ''))
            addr['eb_addr_rank'] = int(addrs.get('rank', ''))
            # Truncate
            addr['eb_addr_fname'] = addr['eb_addr_fname'][:30]
            addr['eb_addr_lname'] = addr['eb_addr_lname'][:30]
            addr['eb_addr_addr1'] = addr['eb_addr_addr1'][:50]
            addr['eb_addr_city'] = addr['eb_addr_city'][:30]
            addr['eb_addr_dob'] = addr['eb_addr_dob'][:6]

            addresses.append(addr)
        elif type(addrs) is list:
            for row in addrs:
                addr = {}
                addr['cust_id'] = int(cust_id)
                addr['our_run_date'] = our_run_date
                addr['seqnum'] = int(seqnum)
                addr['eb_addr_fname'] = row.get('first', '')
                addr['eb_addr_lname'] = row.get('last', '')
                addr['eb_addr_addr1'] = (row.get('address', '') or '').replace('&', '').replace('\\', '')
                addr['eb_addr_city'] = row.get('city', '')
                addr['eb_addr_state'] = row.get('state', '')
                our_zip = row.get('zip', '')
                addr['eb_addr_zip5'] = our_zip[:5] or ''
                addr['eb_addr_zip4'] = our_zip[-4:] if len(our_zip) == 9 else ''
                addr['eb_addr_dob'] = row.get('dob', '')
                addr['eb_addr_match'] = row.get('match', '')
                addr['eb_addr_status'] = row.get('status', '')
                addr['eb_addr_score'] = int(row.get('score', ''))
                addr['eb_addr_rank'] = int(row.get('rank', ''))
                # Truncate
                addr['eb_addr_fname'] = addr['eb_addr_fname'][:30]
                addr['eb_addr_lname'] = addr['eb_addr_lname'][:30]
                addr['eb_addr_addr1'] = addr['eb_addr_addr1'][:50]
                addr['eb_addr_city'] = addr['eb_addr_city'][:30]
                addr['eb_addr_dob'] = addr['eb_addr_dob'][:6]

                addresses.append(addr)

        res = conn.execute(meta.tables['insurance2_ebureau_addr_t'].insert(), addresses)
        result = res.rowcount
    return result

def parse_n_store_in_eb_phone(conn, meta, payload):
    result = 0
    phones = []
    data = xmltodict.parse(payload)
    str_run_date = data['root']['transaction']['input']['account']['sourceid']
    our_run_date = datetime.strptime(str_run_date, "%Y-%m-%d %H:%M:%S")     
    cust_id = data['root']['transaction']['input']['account']['groupid']
    seqnum = data['root']['transaction']['input']['account']['account']
    output = data['root']['transaction']['output']
    if 'phone' in output:    # not always have phone block
        phs = output['phone']
        if type(phs) is collections.OrderedDict:
            ph = {}
            ph['cust_id'] = int(cust_id)
            ph['our_run_date'] = our_run_date
            ph['seqnum'] = int(seqnum)
            ph['eb_ph_fname'] = phs.get('first', '')
            ph['eb_ph_lname'] = phs.get('last', '')
            ph['eb_ph_phone'] = phs.get('phone', '')
            ph['eb_ph_match'] = phs.get('match', '')
            ph['eb_ph_score'] = int(phs.get('score', ''))
            ph['eb_ph_rank'] = int(phs.get('rank', ''))
            # Truncate
            ph['eb_ph_fname'] = ph['eb_ph_fname'][:30]
            ph['eb_ph_lname'] = ph['eb_ph_lname'][:30]
            ph['eb_ph_phone'] = ph['eb_ph_phone'][:15]

            phones.append(ph)
        elif type(phs) is list:
            for row in phs:
                ph = {}
                ph['cust_id'] = int(cust_id)
                ph['our_run_date'] = our_run_date
                ph['seqnum'] = int(seqnum)
                ph['eb_ph_fname'] = row.get('first', '')
                ph['eb_ph_lname'] = row.get('last', '')
                ph['eb_ph_phone'] = row.get('phone', '')
                ph['eb_ph_match'] = row.get('match', '')
                ph['eb_ph_score'] = int(row.get('score', ''))
                ph['eb_ph_rank'] = int(row.get('rank', ''))
                # Truncate
                ph['eb_ph_fname'] = ph['eb_ph_fname'][:30]
                ph['eb_ph_lname'] = ph['eb_ph_lname'][:30]
                ph['eb_ph_phone'] = ph['eb_ph_phone'][:15]

                phones.append(ph)

        res = conn.execute(meta.tables['insurance2_ebureau_phone_t'].insert(), phones)
        result = res.rowcount
    return result          

def parse_n_store_in_eb_message(conn, meta, payload):
    result = 0
    messages = []
    data = xmltodict.parse(payload)
    str_run_date = data['root']['transaction']['input']['account']['sourceid']
    our_run_date = datetime.strptime(str_run_date, "%Y-%m-%d %H:%M:%S")     
    cust_id = data['root']['transaction']['input']['account']['groupid']
    seqnum = data['root']['transaction']['input']['account']['account']
    output = data['root']['transaction']['output']
    if 'message' in output:    # Always have message block??
        msgs = output['message']    
        if type(msgs) is collections.OrderedDict:
            msg = {}
            msg['cust_id'] = int(cust_id)
            msg['our_run_date'] = our_run_date
            msg['seqnum'] = int(seqnum)
            msg['eb_message'] = (msgs.get('message', '') or '').replace('&', '').replace('\\', '')
            # Truncate
            msg['eb_message'] = msg['eb_message'][:75]

            messages.append(msg)
        elif type(msgs) is list:
            for row in msgs:
                msg = {}
                msg['cust_id'] = int(cust_id)
                msg['our_run_date'] = our_run_date
                msg['seqnum'] = int(seqnum)
                msg['eb_message'] = (row.get('message', '') or '').replace('&', '').replace('\\', '')
                # Truncate
                msg['eb_message'] = msg['eb_message'][:75]

                messages.append(msg)
        res = conn.execute(meta.tables['insurance2_ebureau_message_t'].insert(), messages)
        result = res.rowcount
    return result

def parse_n_store_in_eb_status(conn, meta, payload):
    result = 0
    sts = []
    data = xmltodict.parse(payload)
    transaction = data['root']['transaction']
    str_run_date = transaction['input']['account']['sourceid']
    our_run_date = datetime.strptime(str_run_date, "%Y-%m-%d %H:%M:%S")
    cust_id = transaction['input']['account']['groupid']
    seqnum = transaction['input']['account']['account']
    output = transaction['output']
    if 'status' in transaction and 'quality' in output:
        status = data['root']['transaction']['status']
        quality = output['quality']
        st = {}
        st['cust_id'] = int(cust_id)
        st['our_run_date'] = our_run_date
        st['seqnum'] = int(seqnum)
        st['eb_status'] = status['result']
        st['eb_fname_quality'] = quality['first']
        st['eb_lname_quality'] = quality['last']
        st['eb_addr1_quality'] = quality['address']
        st['eb_city_quality'] = quality['city']
        st['eb_state_quality'] = quality['state']
        st['eb_zip_quality'] = quality['zip']
        st['eb_dob_quality'] = quality['dob']
        st['eb_ssn_quality'] = quality['social']
        st['eb_phone_quality'] = quality['phone']
        sts.append(st)

        res = conn.execute(meta.tables['insurance2_ebureau_status_t'].insert(), sts)
        result = res.rowcount
    return result    

def happy_path_parse_n_store(conn, meta, payload):
    tranx = conn.begin()
    try:
        # eBureau main table
        result = parse_n_store_in_eb_real_time(conn, payload)
        row = result.fetchone()
        logger.info('main tbl: {}'.format(row[0]))

        # address table
        result = parse_n_store_in_eb_address(conn, meta, payload)
        logger.info('addr tbl: {}'.format(result))

        # phone table
        result = parse_n_store_in_eb_phone(conn, meta, payload)
        logger.info('phone tbl: {}'.format(result))

        # message table
        result = parse_n_store_in_eb_message(conn, meta, payload)
        logger.info('msg tbl: {}'.format(result))

        # status table
        result = parse_n_store_in_eb_status(conn, meta, payload)
        logger.info('status tbl: {}'.format(result))          

        tranx.commit()
    except Exception as e:
        tranx.rollback()
        logger.error("Got db error: {}...".format(e[:25]))


if __name__ == '__main__':
    db_engine = sqlalchemy.create_engine(CONN_STRING)
    with db_engine.connect() as conn:
        meta = sqlalchemy.MetaData()
        meta.reflect(conn, only=['insurance2_ebureau_addr_t',
                                 'insurance2_ebureau_status_t',
                                 'insurance2_ebureau_message_t',
                                 'insurance2_ebureau_phone_t',
                                 'insurance2_ebureau_addr_t'])        
        for payload in get_payloads(conn):
            data = xmltodict.parse(payload)
            if 'error' in data:
                logger.error('error path ...')
            elif 'root' in data:
                happy_path_parse_n_store(conn, meta, payload)
