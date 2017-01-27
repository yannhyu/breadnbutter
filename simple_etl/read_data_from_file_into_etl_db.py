# read_data_from_file_into_etl_db.py

import fileinput
from collections import OrderedDict
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.schema import MetaData
import psycopg2

INPUT_LAYOUT = ('acctnum', 'lname', 'mname', 'fname', 'addr1', 'addr2', 
                'city', 'state', 'zip5', 'zip4', 'ssn', 'gender', 'dob')

OUTPUT_FIELDS = ('acctnum', 'lname', 'mname', 'fname', 'addr1', 'addr2', 
                 'city', 'state', 'zip5', 'ssn', 'gender', 'dob')

conn_str = 'postgresql://test_user:med@luckdb:5432/etl'
engine = create_engine(conn_str)
meta = MetaData()
meta.reflect(bind=engine)

def project_data(dict_data):
    return OrderedDict(zip(OUTPUT_FIELDS, [ dict_data.get(field, '') for field in OUTPUT_FIELDS ]))

if __name__ == '__main__':
    for line in fileinput.input():
        if not fileinput.isfirstline():    # First line is header in this 309 case
            dic_line = dict(zip(INPUT_LAYOUT, line.strip('\n').strip('\r').split('|')))
            row = project_data(dic_line)
            try:
                engine.execute(
                    meta.tables['shiny_etl_tbl'].insert().values(data=row)
                )
            except (psycopg2.DataError, sqlalchemy.exc.DataError):
                pass