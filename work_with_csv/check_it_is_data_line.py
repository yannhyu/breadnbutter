# check_it_is_data_line.py

def line_is_data(line):
    result = True
    if len(line.split('|')) < 6:
        result = False
    return result


line_1 = '''
016950|16950|UP Healthsystem - Bell|BELL|AC0002191858|M000060027|ALAN|GIBBS|227 HILL ST APT 2||ISHPEMING|MI|49849||331-76-5009|M|11241972|ALAN|GIBBS|227 HILL ST APT 2||ISHPEMING|MI|49849|||EASTWOOD NURSING CENTER|01142017|01142017|O ER|ER|V|SP|SP|FB|646.63|596.63
'''

line_2 = '''TOTAL|30'''

line_3 = '''"END OF FILE"'''

line_4 = '''BAR.PAT.zcus.clh.dbm.medlytix.pla.modified'''

print(len(line_1.split('|')))
print(len(line_2.split('|')))
print(len(line_3.split('|')))
print(len(line_4.split('|')))

print(line_is_data(line_1))
print(line_is_data(line_2))
print(line_is_data(line_3))
print(line_is_data(line_4))


