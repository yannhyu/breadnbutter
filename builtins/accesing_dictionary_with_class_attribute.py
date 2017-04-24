# accessing_dictionary_with_class_attribute.py

config = {'account_receivable': '4', 'account_payable': '5', 'account_cogs': '8',
'account_retained_earning': '9', 'account_income': '6', 'account_expense': '31', 
'duration': 2, 'financial_year_month': 9, 'financial_year_day': 15, 
'account_cash': '3', 'account_inventory': '2', 'account_accumulated_depriciation': '34', 
'account_depriciation_expense': '35', 'account_salary_expense': '30', 
'account_payroll_payable': '68', 'account_discount': '36', 'financial_year_close': '2008-08-08'}

class Bunch(object):
    def __init__(self, adict):
        self.__dict__.update(adict)


cb = Bunch(config)

print(cb.account_payable)
print(cb.financial_year_close)

