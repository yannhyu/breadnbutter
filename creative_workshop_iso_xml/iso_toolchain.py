# iso_toolchain.py
import csv

def scrub_data_value(input_dict):
    return {k: v.replace('|', r' ') for k, v in input_dict.items() if v}

def write(output_filename, toCSV):
    if toCSV:
        keys = (
            'Response_Id',
            'ISO_Response_Date',
            'MLX_Policy_Number',
            'Match_Insurer_Policy_Number',
            'Match_Insurer_Effective_Date',
            'Match_Insurer_Term_Date',
            'Match_Insurer_LOB',
            'Match_Insurer_Name',
            'Match_Insurer_Addr1',
            'Match_Insurer_Addr2',    # 10
            'Match_Insurer_City',
            'Match_Insurer_State',
            'Match_Insurer_Zip',
            'Match_Insurer_Phone',
            'Match_Insurer_Role_Code',
            'ISO_Agency_Id',
            'ISO_Insured_Id',
            'Loss_Date',
            'Loss_Time',
            'Loss_Description',    # 20
            'Loss_Address_1',
            'Loss_City',
            'Loss_State',
            'Claims_Party_1_Last_Name',
            'Claims_Party_1_First_Name',
            'Claims_Party_1_Commercial_Name',
            'Claims_Party_1_Id_Type',
            'Claims_Party_1_Id_number',
            'Claims_Party_1_Id_State',
            'Claims_Party_1_Gender',    # 30
            'Claims_Party_1_Birth_Date',
            'Claims_Party_1_Injury_Info_1',
            'Claims_Party_1_Injury_Info_2',
            'Claims_Party_1_Address_1',
            'Claims_Party_1_City',
            'Claims_Party_1_State',
            'Claims_Party_1_Zip',
            'Claims_Party_1_Comm_1_type',
            'Claims_Party_1_Comm_1_use',
            'Claims_Party_1_Comm_1_number',    # 40
            'Claims_Party_1_Role_Code',
            'Adjuster_Party_1_Commercial_Name',
            'Adjuster_Party_1_Last_Name',
            'Adjuster_Party_1_First_Name',
            'Adjuster_Party_1_Comm_1_type',
            'Adjuster_Party_1_Comm_1_use',
            'Adjuster_Party_1_Comm_1_number',
            'Claims_Party_2_Last_Name',
            'Claims_Party_2_First_Name',
            'Claims_Party_2_Commercial_Name',
            'Claims_Party_2_Id_Type',
            'Claims_Party_2_Id_number',
            'Claims_Party_2_Id_State',
            'Claims_Party_2_Gender',
            'Claims_Party_2_Birth_Date',
            'Claims_Party_2_Injury_Info_1',
            'Claims_Party_2_Injury_Info_2',
            'Claims_Party_2_Address_1',
            'Claims_Party_2_City',
            'Claims_Party_2_State',
            'Claims_Party_2_Zip',
            'Claims_Party_2_Comm_1_type',
            'Claims_Party_2_Comm_1_use',
            'Claims_Party_2_Comm_1_number',
            'Claims_Party_2_Role_Code',
            'Adjuster_Party_2_Commercial_Name',
            'Adjuster_Party_2_Last_Name',
            'Adjuster_Party_2_First_Name',
            'Adjuster_Party_2_Comm_1_type',
            'Adjuster_Party_2_Comm_1_use',
            'Adjuster_Party_2_Comm_1_number',                        
            )
        with open(output_filename, 'wb') as output_file:
            dict_writer = csv.DictWriter(output_file, keys, delimiter="|")
            dict_writer.writeheader()
            dict_writer.writerows(toCSV)