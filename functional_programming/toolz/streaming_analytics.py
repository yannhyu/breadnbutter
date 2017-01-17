# streaming_analytics.py

#           id, name, balance, gender
accounts = [(1, 'Alice', 100, 'F'),
            (2, 'Bob', 200, 'M'),
            (3, 'Charlie', 150, 'M'),
            (4, 'Dennis', 50, 'M'),
            (5, 'Edith', 300, 'F')]


"""
SELECT name, balance
FROM accounts
WHERE balance > 150;
"""

from toolz.curried import pipe, map, filter, get

result_01 = pipe(accounts, 
                 filter(lambda (id, name, balance, gender): balance > 150),
                 map(get([1, 2])),
                 list)
print(result_01)

result_02 = [ (name, balance) for (id, name, balance, gender) in accounts
                 if balance > 150 ]
print(result_02)                 


