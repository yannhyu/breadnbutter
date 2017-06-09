# scene_70_loop_claimsParty_iso_2csv.py

import xmltodict
import json
import csv

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

def digest_match_detail(iso_top, matchDetail):
    iso_header_RqUID = iso_top['RqUID']
    iso_header_TransactionResponseDt = iso_top['TransactionResponseDt']
    iso_top_policy_number = iso_top['Policy']['PolicyNumber']

    row_dict = {}
    row_dict['Response_Id'] = iso_header_RqUID
    row_dict['ISO_Response_Date'] = iso_header_TransactionResponseDt
    row_dict['MLX_Policy_Number'] = iso_top_policy_number 

    # print(matchDetail)
    matchDetail_Policy = matchDetail['Policy']

    row_dict['Match_Insurer_Policy_Number'] = (
        matchDetail_Policy.get('PolicyNumber', ''))
    
    row_dict['Match_Insurer_Effective_Date'] = (
        matchDetail_Policy
        .get('ContractTerm', {})
        .get('EffectiveDt', ''))

    row_dict['Match_Insurer_Term_Date'] = (
        matchDetail_Policy
        .get('ContractTerm', {})
        .get('ExpirationDt', ''))    

    row_dict['Match_Insurer_LOB'] = (
        matchDetail_Policy
        .get('LOBCd', {})
        .get('#text', ''))

    row_dict['Match_Insurer_Name'] = (
        matchDetail_Policy
        .get('MiscParty', {})
        .get('GeneralPartyInfo', {})
        .get('NameInfo', {})
        .get('CommlName', {})
        .get('CommercialName', ''))

    row_dict['Match_Insurer_Addr1'] = (
        matchDetail_Policy
        .get('MiscParty', {})
        .get('GeneralPartyInfo', {})
        .get('Addr', {})
        .get('Addr1', ''))

    row_dict['Match_Insurer_Addr2'] = (
        matchDetail_Policy
        .get('MiscParty', {})
        .get('GeneralPartyInfo', {})
        .get('Addr', {})
        .get('Addr2', ''))

    row_dict['Match_Insurer_City'] = (
        matchDetail_Policy
        .get('MiscParty', {})
        .get('GeneralPartyInfo', {})
        .get('Addr', {})
        .get('City', ''))

    row_dict['Match_Insurer_State'] = (
        matchDetail_Policy
        .get('MiscParty', {})
        .get('GeneralPartyInfo', {})
        .get('Addr', {})
        .get('StateProvCd', ''))

    row_dict['Match_Insurer_Zip'] = (
        matchDetail_Policy
        .get('MiscParty', {})
        .get('GeneralPartyInfo', {})
        .get('Addr', {})
        .get('PostalCode', ''))
    
    row_dict['Match_Insurer_Phone'] = (
        matchDetail_Policy
        .get('MiscParty', {})
        .get('GeneralPartyInfo', {})
        .get('Communications', {})
        .get('PhoneInfo', {})
        .get('PhoneNumber', ''))    

    row_dict['Match_Insurer_Role_Code'] = (
        matchDetail_Policy
        .get('MiscParty', {})
        .get('MiscPartyInfo', {})
        .get('MiscPartyRoleCd', '')) 

    row_dict['ISO_Agency_Id'] = (
        matchDetail
        .get('ClaimsOccurrence', {})
        .get('ItemIdInfo', {})
        .get('AgencyId', ''))
    
    row_dict['ISO_Insured_Id'] = (
        matchDetail
        .get('ClaimsOccurrence', {})
        .get('ItemIdInfo', {})
        .get('InsurerId', ''))

    row_dict['Loss_Date'] = (
        matchDetail
        .get('ClaimsOccurrence', {})
        .get('LossDt', ''))

    row_dict['Loss_Time'] = (
        matchDetail
        .get('ClaimsOccurrence', {})
        .get('LossTime', ''))

    row_dict['Loss_Description'] = (
        matchDetail
        .get('ClaimsOccurrence', {})
        .get('IncidentDesc', ''))

    row_dict['Loss_Address_1'] = (
        matchDetail
        .get('ClaimsOccurrence', {})
        .get('Addr', {})
        .get('Addr1', ''))

    row_dict['Loss_City'] = (
        matchDetail
        .get('ClaimsOccurrence', {})
        .get('Addr', {})
        .get('City', ''))

    row_dict['Loss_State'] = (
        matchDetail
        .get('ClaimsOccurrence', {})
        .get('Addr', {})
        .get('StateProvCd', ''))

    claimsParty_list = matchDetail.get('ClaimsParty')
    if isinstance(claimsParty_list, list):
        row_dict = digest_claimsParty(row_dict, claimsParty_list)
    else:    # TODO: revisit: in case there is only one claimsParty
        pass
   
    adjusterParty_list = matchDetail.get('AdjusterParty')
    if isinstance(adjusterParty_list, list):
        row_dict = digest_adjusterParty_list(row_dict, adjusterParty_list)
    elif isinstance(adjusterParty_list, dict):
        # print('adjusterParty_list is OrderedDict {}'.format(adjusterParty_list))
        row_dict = digest_adjusterParty(row_dict, adjusterParty_list)       
    else:    # TODO: revisit: in case there is only one adjusterParty
        pass   
    
    return scrub_data_value(row_dict)

def digest_claimsParty(row_dict, claimsParty_list):
    for index, claimsParty in enumerate(claimsParty_list):
        row_dict['Claims_Party_{}_Last_Name'.format(index+1)] = (
            claimsParty
            .get('GeneralPartyInfo', {})
            .get('NameInfo', {})
            .get('PersonName', {})
            .get('Surname', ''))

        row_dict['Claims_Party_{}_First_Name'.format(index+1)] = (
            claimsParty
            .get('GeneralPartyInfo', {})
            .get('NameInfo', {})
            .get('PersonName', {})
            .get('GivenName', ''))

        row_dict['Claims_Party_{}_Commercial_Name'.format(index+1)] = (
            claimsParty
            .get('GeneralPartyInfo', {})
            .get('NameInfo', {})
            .get('CommlName', {})
            .get('CommercialName', ''))

        row_dict['Claims_Party_{}_Id_Type'.format(index+1)] = (
            claimsParty
            .get('GeneralPartyInfo', {})
            .get('TaxIdentity', {})
            .get('TaxIdTypeCd', ''))    

        row_dict['Claims_Party_{}_Id_number'.format(index+1)] = (
            claimsParty
            .get('GeneralPartyInfo', {})
            .get('TaxIdentity', {})
            .get('TaxId', '')) 

        row_dict['Claims_Party_{}_Id_State'.format(index+1)] = (
            claimsParty
            .get('GeneralPartyInfo', {})
            .get('TaxIdentity', {})
            .get('StateProvCd', ''))

        row_dict['Claims_Party_{}_Gender'.format(index+1)] = (
            claimsParty
            .get('GeneralPartyInfo', {})
            .get('PersonInfo', {})
            .get('GenderCd', ''))

        row_dict['Claims_Party_{}_Birth_Date'.format(index+1)] = (
            claimsParty
            .get('GeneralPartyInfo', {})
            .get('PersonInfo', {})
            .get('BirthDt', ''))

        # TODO: revisit this with Matt
        row_dict['Claims_Party_{}_Injury_Info_1'.format(index+1)] = (
            claimsParty
            .get('GeneralPartyInfo', {})
            .get('ClaimsInjuredInfo', {})
            .get('ClaimsInjury', {})
            .get('InjuryNatureDesc', ''))

        # TODO: revisit this with Matt
        row_dict['Claims_Party_{}_Injury_Info_2'.format(index+1)] = (
            claimsParty
            .get('GeneralPartyInfo', {})
            .get('ClaimsInjuredInfo', {})
            .get('ClaimsInjury', {})
            .get('InjuryNatureDesc', ''))

        row_dict['Claims_Party_{}_Address_1'.format(index+1)] = (
            claimsParty
            .get('GeneralPartyInfo', {})
            .get('Addr', {})
            .get('Addr1', ''))

        row_dict['Claims_Party_{}_City'.format(index+1)] = (
            claimsParty
            .get('GeneralPartyInfo', {})
            .get('Addr', {})
            .get('City', ''))

        row_dict['Claims_Party_{}_State'.format(index+1)] = (
            claimsParty
            .get('GeneralPartyInfo', {})
            .get('Addr', {})
            .get('StateProvCd', ''))

        row_dict['Claims_Party_{}_Zip'.format(index+1)] = (
            claimsParty
            .get('GeneralPartyInfo', {})
            .get('Addr', {})
            .get('PostalCode', ''))

        row_dict['Claims_Party_{}_Comm_1_type'.format(index+1)] = (
            claimsParty
            .get('GeneralPartyInfo', {})
            .get('Communications', {})
            .get('PhoneInfo', {})
            .get('PhoneTypeCd', ''))

        row_dict['Claims_Party_{}_Comm_1_use'.format(index+1)] = (
            claimsParty
            .get('GeneralPartyInfo', {})
            .get('Communications', {})
            .get('PhoneInfo', {})
            .get('CommunicationUseCd', ''))

        claimsParty_phoneNumber = (
            claimsParty
            .get('GeneralPartyInfo', {})
            .get('Communications', {})
            .get('PhoneInfo', {})
            .get('PhoneNumber', '')
            )
        if isinstance(claimsParty_phoneNumber, dict):
            claimsParty_phoneNumber = claimsParty_phoneNumber.get('#text', '')
        row_dict['Claims_Party_{}_Comm_1_number'.format(index+1)] = (
            claimsParty_phoneNumber)

        # maybe unicode or dict 
        claimsPartyRoleCd = (
            claimsParty
            .get('ClaimsPartyInfo', {})
            .get('ClaimsPartyRoleCd', ''))
        if isinstance(claimsPartyRoleCd, dict):
            claimsPartyRoleCd = (
                claimsPartyRoleCd.get('#text', ''))
        row_dict['Claims_Party_{}_Role_Code'.format(index+1)] = (
            claimsPartyRoleCd)

    return row_dict

def digest_adjusterParty_list(row_dict, adjusterParty_list):
    print('...inside digest_adjusterParty_list(...)')
    # row_dict['Adjuster_Party_1_Commercial_Name'] = (
    #     adjusterParty_list[0]
    #     .get('GeneralPartyInfo', {})
    #     .get('NameInfo', {})
    #     .get('CommlName', {})
    #     .get('CommercialName', ''))
    for index, adjusterParty in enumerate(adjusterParty_list):
        digest_adjusterParty_common(row_dict, adjusterParty, index+1)

    return row_dict

def digest_adjusterParty(row_dict, adjusterParty):
    print('inside digest_adjusterParty(...)')
    return digest_adjusterParty_common(row_dict, adjusterParty, 1)

def digest_adjusterParty_common(row_dict, adjusterParty, mlx_index):
    # NameInfo maybe list
    nameInfo_list = (
        adjusterParty
        .get('GeneralPartyInfo', {})
        .get('NameInfo', {}))

    if isinstance(nameInfo_list, list):
        nameInfo_list = nameInfo_list[0]

    row_dict['Adjuster_Party_{}_Commercial_Name'.format(mlx_index)] = (
        nameInfo_list
        .get('CommlName', {})
        .get('CommercialName', ''))

    row_dict['Adjuster_Party_{}_Last_Name'.format(mlx_index)] = (
        nameInfo_list
        .get('PersonName', {})
        .get('Surname', ''))

    row_dict['Adjuster_Party_{}_First_Name'.format(mlx_index)] = (
        nameInfo_list
        .get('PersonName', {})
        .get('GivenName', ''))

    communications = (
        adjusterParty
        .get('GeneralPartyInfo', {})
        .get('Communications', {}))

    row_dict['Adjuster_Party_{}_Comm_1_type'.format(mlx_index)] = (
        communications
        .get('PhoneInfo', {})
        .get('PhoneTypeCd', ''))

    row_dict['Adjuster_Party_{}_Comm_1_use'.format(mlx_index)] = (
        communications
        .get('PhoneInfo', {})
        .get('CommunicationUseCd', ''))

    row_dict['Adjuster_Party_{}_Comm_1_number'.format(mlx_index)] = (
        communications
        .get('PhoneInfo', {})
        .get('PhoneNumber', ''))

    return row_dict    

def scrub_data_value(input_dict):
    return {k: v.replace('|', r' ') for k, v in input_dict.items()}

def digest_iso_resp(filename):
    iso_results = []
    with open(filename, 'r') as fh:
        xml = fh.read().replace('\n', '')
        result = xmltodict.parse(xml)
        # print(json.dumps(result, indent=4))

        iso_top = result['ClaimInvestigationAddRs']

        matchDetails = iso_top['MatchDetails']
        # print(len(matchDetails))
        # print(type(matchDetails))
        if isinstance(matchDetails, list):
            for matchDetail in matchDetails:
                row_dict = digest_match_detail(iso_top, matchDetail)
                iso_results.append(row_dict)
        else:          
            row_dict = digest_match_detail(iso_top, matchDetails)
            iso_results.append(row_dict)

    return iso_results


if __name__ == '__main__':
    # resp_file = 'Matt_WC_response.xml'
    resp_file = 'Multiple_Matches.xml'
    output_file = 'iso_MLX_scene_70_loop_claimsParty.txt'
    iso_results = digest_iso_resp(resp_file)
    write(output_file, iso_results)