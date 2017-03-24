#!/usr/bin/python
# test_lambda_use_case.py
# Usage           : ./test_lambda_use_case.py UPHSBell-02_21_17-12_04_15.txt
# the output ought to match output_UPHSBell-02_21_17-12_04_15
# ==============================================================================
import fileinput

input_fields = ('hid', 'temp1', 'temp2', 'temp3', 'acctnum', 'cpi', 'fname', 'lname', 'addr1', 'addr2', 'city', 'state',
                'zip5', 'zip4', 'ssn', 'gender', 'dob', 'g_fname', 'g_lname', 'g_addr1', 'g_addr2', 'g_city', 'g_state',
                'g_zip5', 'g_zip4', 'g_dob', 'g_employ_name', 'service_date_begin', 'service_date_end', 'pat_proc_type',
                'pat_type', 'fin_class', 'payor_plan1', 'payor_plan2', 'acct_status', 'charges', 'balance')

results_fields = ('cust_id', 'treatment_code', 'output_id', 'hid', 'acctnum', 'cpi', 'lname', 'mname', 'fname', 'addr1',
                  'addr2', 'city', 'state', 'zip5', 'zip4', 'ssn', 'gender', 'dob', 'g_lname', 'g_mname', 'g_fname',
                  'g_addr1', 'g_addr2', 'g_city', 'g_state', 'g_zip5', 'g_zip4', 'g_ssn', 'g_gender', 'g_dob',
                  'g_employ_name', 'provider_state', 'service_date_begin', 'service_date_end', 'pat_proc_type',
                  'pat_type', 'fin_class', 'payor_plan1', 'payor_plan2', 'cpt', 'drg', 'diag1', 'diag2', 'charges',
                  'balance', 'acct_status', 'client_field1', 'client_field2', 'client_field3', 'client_date1')

def update_data(dict_data):
    dict_data['provider_state'] = 'MI'
    dict_data['treatment_code'] = dict_data['output_id'] = '1'
    dict_data['cust_id'] = '302'
    if not dict_data.get('state', ''):
        dict_data['state'] = dict_data['provider_state']
    print('|'.join([dict_data.get(i, '') for i in results_fields]))


if __name__ == '__main__':
    line_is_data = lambda line: len(line.split('|')) >= 6
    for line in fileinput.input():
        if not fileinput.isfirstline() and line_is_data(line):
            dic_line = dict(zip(input_fields, line.translate(None, '\r\n').split('|')))
            update_data(dic_line)

