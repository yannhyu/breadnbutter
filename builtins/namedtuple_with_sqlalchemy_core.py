# namedtuple_with_sqlalchemy_core.py

# set up a data model. 
# We’ll just track user names and email addresses, 
# so the namedtuple will look like this
from collections import namedtuple
User = namedtuple('User', ["id", "name", "email"])
someone = User(1, "Some Body", "some@one.com")

# Setting the Stage
import json, sqlalchemy

'''some of the tuples are the User namedtuple, 
   while others are raw tuples. As long as 
   the data in the tuples match the schema, 
   SQLAlchemy will save either properly.'''
connection_string = 'sqlite://'
db = sqlalchemy.create_engine(connection_string)
engine = db.connect()
meta = sqlalchemy.MetaData(engine)

columns = (
    sqlalchemy.Column('id', sqlalchemy.Integer),
    sqlalchemy.Column('name', sqlalchemy.Text),
    sqlalchemy.Column('email', sqlalchemy.Text),
)

sqlalchemy.Table("users", meta, *columns)
meta.create_all()

table = sqlalchemy.table("users", *columns)
# Now we have a table to back the data model. 
# From here, we can start adding data.

# add test data
statements = [
    table.insert().values(user)
    for user in (
        User(1, "Alice", "alice@test.com"),
        User(2, "Bob", "bob@test.com"),
        (3, "Chuck", "Chuck@test.com"),
        (4, "Diane", "diane@test.com"),
    )
]
[engine.execute(stmt) for stmt in statements]

# Reading the Data
alice = engine.execute(table.select().where(table.c.name == "Alice")).fetchone()
print("User: {}".format(alice[1]))

# With namedtuple, accessing data and even debugging becomes easier.
tuple_alice = User(*alice)
print("User: {}".format(tuple_alice.name))
# User: Alice
print(alice)
# (1, 'Alice', 'alice@test.com')
print(tuple_alice)
# User(id=1, name='Alice', email='alice@test.com')
