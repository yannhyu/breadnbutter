# scene_8_flatley.py

import xmltodict
#import json
from iso_toolchain import write, scrub_data_value
from flatten_dict import flatten

def digest_iso_resp(filename):
    iso_results = []
    with open(filename, 'r') as fh:
        xml = fh.read().replace('\n', '')
        res = xmltodict.parse(xml)
        #print(json.dumps(result, indent=4))
        flat_res = flatten(res)
        #for k, v in flat_res.items():
        #    print('{} ---> {}'.format(k, v))

        # if TRUE then it is multi; otherwise single MatchDetails
        if ('ClaimInvestigationAddRs', 'MatchDetails') in flat_res:
            print('multi MatchDetails')
            match_details = flat_res.get(('ClaimInvestigationAddRs', 'MatchDetails'))
            for match_detail in match_details:
                print(len(match_details))
        else:
            print('single MatchDetails')
            iso_results.append(digest_single_match(flat_res))


    return iso_results

def digest_single_match(iso):
    row = {}
    
    discover = iso.get
    row['Response_Id'] = discover(
        ('ClaimInvestigationAddRs',
         'RqUID'))
    row['ISO_Response_Date'] = discover(
        ('ClaimInvestigationAddRs',
         'TransactionResponseDt'))
    row['MLX_Policy_Number'] = discover(
        ('ClaimInvestigationAddRs',
         'Policy',
         'PolicyNumber'))

    row['Match_Insurer_Policy_Number'] = discover(
        ('ClaimInvestigationAddRs',
         'MatchDetails',
         'Policy',
         'PolicyNumber'))

    row['Match_Insurer_Effective_Date'] = discover(
        ('ClaimInvestigationAddRs',
         'MatchDetails',
         'Policy',
         'ContractTerm',
         'EffectiveDt'))

    row['Match_Insurer_Term_Date'] = discover(
        ('ClaimInvestigationAddRs',
         'MatchDetails',
         'Policy',
         'ContractTerm',
         'ExpirationDt'))

    if ('ClaimInvestigationAddRs',
         'MatchDetails',
         'Policy',
         'LOBCd') in iso:
        row['Match_Insurer_LOB'] = discover(
            ('ClaimInvestigationAddRs',
             'MatchDetails',
             'Policy',
             'LOBCd'))    
    else:
        row['Match_Insurer_LOB'] = discover(
            ('ClaimInvestigationAddRs',
             'MatchDetails',
             'Policy',
             'LOBCd',
             '#text'))

    row['Match_Insurer_Name'] = discover(
        ('ClaimInvestigationAddRs',
         'MatchDetails',
         'Policy',
         'MiscParty',
         'GeneralPartyInfo',
         'NameInfo',
         'CommlName',
         'CommercialName'))

    row['Match_Insurer_Addr1'] = discover(
        ('ClaimInvestigationAddRs',
         'MatchDetails',
         'Policy',
         'MiscParty',
         'GeneralPartyInfo',
         'Addr',
         'Addr1'))

    row['Match_Insurer_Addr2'] = discover(
        ('ClaimInvestigationAddRs',
         'MatchDetails',
         'Policy',
         'MiscParty',
         'GeneralPartyInfo',
         'Addr',
         'Addr2'))

    row['Match_Insurer_City'] = discover(
        ('ClaimInvestigationAddRs',
         'MatchDetails',
         'Policy',
         'MiscParty',
         'GeneralPartyInfo',
         'Addr',
         'City'))

    row['Match_Insurer_State'] = discover(
        ('ClaimInvestigationAddRs',
         'MatchDetails',
         'Policy',
         'MiscParty',
         'GeneralPartyInfo',
         'Addr',
         'StateProvCd'))

    row['Match_Insurer_Zip'] = discover(
        ('ClaimInvestigationAddRs',
         'MatchDetails',
         'Policy',
         'MiscParty',
         'GeneralPartyInfo',
         'Addr',
         'PostalCode'))

    row['Match_Insurer_Phone'] = discover(
        ('ClaimInvestigationAddRs',
         'MatchDetails',
         'Policy',
         'MiscParty',
         'GeneralPartyInfo',
         'Communications',
         'PhoneInfo',
         'PhoneNumber'))

    row['Match_Insurer_Role_Code'] = discover(
        ('ClaimInvestigationAddRs',
         'MatchDetails',
         'Policy',
         'MiscParty',
         'MiscPartyInfo',
         'MiscPartyRoleCd'))

    row['ISO_Agency_Id'] = discover(
        ('ClaimInvestigationAddRs',
         'MatchDetails',
         'ClaimsOccurrence',
         'ItemIdInfo',
         'AgencyId'))
    
    row['ISO_Insured_Id'] = discover(
        ('ClaimInvestigationAddRs',
         'MatchDetails',
         'ClaimsOccurrence',
         'ItemIdInfo',
         'InsurerId'))

    row['Loss_Date'] = discover(
        ('ClaimInvestigationAddRs',
         'MatchDetails',
         'ClaimsOccurrence',
         'LossDt'))

    row['Loss_Time'] = discover(
        ('ClaimInvestigationAddRs',
         'MatchDetails',
         'ClaimsOccurrence',
         'LossTime'))


    row['Loss_Description'] = discover(
        ('ClaimInvestigationAddRs',
         'MatchDetails',
         'ClaimsOccurrence',
         'IncidentDesc'))

    row['Loss_Address_1'] = discover(
        ('ClaimInvestigationAddRs',
         'MatchDetails',
         'ClaimsOccurrence',
         'Addr',
         'Addr1'))

    row['Loss_City'] = discover(
        ('ClaimInvestigationAddRs',
         'MatchDetails',
         'ClaimsOccurrence',
         'Addr',
         'City'))

    row['Loss_State'] = discover(
        ('ClaimInvestigationAddRs',
         'MatchDetails',
         'ClaimsOccurrence',
         'Addr',
         'StateProvCd'))

    claimsParty_list = discover(
        ('ClaimInvestigationAddRs',
         'MatchDetails',
         'ClaimsParty'))
    if isinstance(claimsParty_list, list):
        # print(claimsParty_list)
        row = digest_single_match_claimsParty_list(row, claimsParty_list)
    else:    # TODO: revisit: in case there is only one claimsParty
        pass

    adjusterParty_list = discover(
        ('ClaimInvestigationAddRs',
         'MatchDetails',
         'AdjusterParty'))
    if isinstance(adjusterParty_list, list):
        row_dict = digest_single_match_adjusterParty_list(row, adjusterParty_list)
    else:    # TODO: revisit: in case there is only one adjusterParty
        pass 



    return scrub_data_value(row)

def digest_single_match_claimsParty_list(row, claimsParty_list):
    for index, claimsParty in enumerate(claimsParty_list):
        flat_claimsParty = flatten(claimsParty)
        #for k, v in flat_claimsParty.items():
        #    print('{} ---> {}'.format(k, v))
        row['Claims_Party_{}_Last_Name'.format(index+1)] = (
            flat_claimsParty.get(
                ('GeneralPartyInfo',
                 'NameInfo',
                 'PersonName',
                 'Surname')))

        row['Claims_Party_{}_First_Name'.format(index+1)] = (
            flat_claimsParty.get(
                ('GeneralPartyInfo',
                 'NameInfo',
                 'PersonName',
                 'GivenName')))

        row['Claims_Party_{}_Commercial_Name'.format(index+1)] = (
            flat_claimsParty.get(
                ('GeneralPartyInfo',
                 'NameInfo',
                 'CommlName',
                 'CommercialName')))

        row['Claims_Party_{}_Id_Type'.format(index+1)] = (
            flat_claimsParty.get(
                ('GeneralPartyInfo',
                 'TaxIdentity',
                 'TaxIdTypeCd')))

        row['Claims_Party_{}_Id_number'.format(index+1)] = (
            flat_claimsParty.get(
                ('GeneralPartyInfo',
                 'TaxIdentity',
                 'TaxId')))

        row['Claims_Party_{}_Id_State'.format(index+1)] = (
            flat_claimsParty.get(
                ('GeneralPartyInfo',
                 'TaxIdentity',
                 'StateProvCd')))

        row['Claims_Party_{}_Gender'.format(index+1)] = (
            flat_claimsParty.get(
                ('GeneralPartyInfo',
                 'PersonInfo',
                 'GenderCd')))            

        row['Claims_Party_{}_Birth_Date'.format(index+1)] = (
            flat_claimsParty.get(
                ('GeneralPartyInfo',
                 'PersonInfo',
                 'BirthDt')))

        # TODO: revisit this with Matt
        row['Claims_Party_{}_Injury_Info_1'.format(index+1)] = (
            flat_claimsParty.get(
                ('GeneralPartyInfo',
                 'ClaimsInjuredInfo',
                 'ClaimsInjury',
                 'InjuryNatureDesc')))

        # TODO: revisit this with Matt
        row['Claims_Party_{}_Injury_Info_2'.format(index+1)] = (
            flat_claimsParty.get(
                ('GeneralPartyInfo',
                 'ClaimsInjuredInfo',
                 'ClaimsInjury',
                 'InjuryNatureDesc')))

        row['Claims_Party_{}_Address_1'.format(index+1)] = (
            flat_claimsParty.get(
                ('GeneralPartyInfo',
                 'Addr',
                 'Addr1')))

        row['Claims_Party_{}_City'.format(index+1)] = (
            flat_claimsParty.get(
                ('GeneralPartyInfo',
                 'Addr',
                 'City')))

        row['Claims_Party_{}_State'.format(index+1)] = (
            flat_claimsParty.get(
                ('GeneralPartyInfo',
                 'Addr',
                 'StateProvCd')))            
     
        row['Claims_Party_{}_Zip'.format(index+1)] = (
            flat_claimsParty.get(
                ('GeneralPartyInfo',
                 'Addr',
                 'PostalCode')))

        row['Claims_Party_{}_Comm_1_type'.format(index+1)] = (
            flat_claimsParty.get(
                ('GeneralPartyInfo',
                 'Communications',
                 'PhoneInfo',
                 'PhoneTypeCd')))

        row['Claims_Party_{}_Comm_1_use'.format(index+1)] = (
            flat_claimsParty.get(
                ('GeneralPartyInfo',
                 'Communications',
                 'PhoneInfo',
                 'CommunicationUseCd')))             

        row['Claims_Party_{}_Comm_1_number'.format(index+1)] = (
            flat_claimsParty.get(
                ('GeneralPartyInfo',
                 'Communications',
                 'PhoneInfo',
                 'PhoneNumber')))

        # maybe unicode or dict 
        claimsPartyRoleCd = (
            flat_claimsParty.get(
                ('ClaimsPartyInfo',
                 'ClaimsPartyRoleCd')))
        if not claimsPartyRoleCd:
            claimsPartyRoleCd = (
                flat_claimsParty.get(
                    ('ClaimsPartyInfo',
                     'ClaimsPartyRoleCd',   
                     '#text')))
        row['Claims_Party_{}_Role_Code'.format(index+1)] = (
            claimsPartyRoleCd)

    return row

def digest_single_match_adjusterParty_list(row, adjusterParty_list):
    # print(adjusterParty_list)
    for index, adjusterParty in enumerate(adjusterParty_list):
        flat_adjusterParty = flatten(adjusterParty)
        # for k, v in flat_adjusterParty.items():
        #     print('{} ---> {}'.format(k, v))
        row['Adjuster_Party_{}_Commercial_Name'.format(index+1)] = (
            flat_adjusterParty.get(
                ('GeneralPartyInfo',
                 'NameInfo',
                 'CommlName',
                 'CommercialName')))
        
        row['Adjuster_Party_{}_Last_Name'.format(index+1)] = (
            flat_adjusterParty.get(
                ('GeneralPartyInfo',
                 'NameInfo',
                 'PersonName',
                 'Surname')))

        row['Adjuster_Party_{}_First_Name'.format(index+1)] = (
            flat_adjusterParty.get(
                ('GeneralPartyInfo',
                 'NameInfo',
                 'PersonName',
                 'GivenName')))

        row['Adjuster_Party_{}_Comm_1_type'.format(index+1)] = (
            flat_adjusterParty.get(
                ('GeneralPartyInfo',
                 'Communications',
                 'PhoneInfo',
                 'PhoneTypeCd')))

        row['Adjuster_Party_{}_Comm_1_use'.format(index+1)] = (
            flat_adjusterParty.get(
                ('GeneralPartyInfo',
                 'Communications',
                 'PhoneInfo',
                 'CommunicationUseCd')))

        row['Adjuster_Party_{}_Comm_1_number'.format(index+1)] = (
            flat_adjusterParty.get(
                ('GeneralPartyInfo',
                 'Communications',
                 'PhoneInfo',
                 'PhoneNumber')))
              

    return row        


if __name__ == '__main__':
    resp_file = 'Multiple_Matches.xml'
    # resp_file = 'Matt_WC_response.xml'
    output_file = 'iso_MLX_8.txt'
    iso_results = digest_iso_resp(resp_file)
    write(output_file, iso_results)