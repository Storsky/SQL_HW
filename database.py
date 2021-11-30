import sqlalchemy

db = 'postgresql://akvasnikov:123456@localhost:5432/musicshop'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

connection.execute("""DROP TABLE testtable;""")  
