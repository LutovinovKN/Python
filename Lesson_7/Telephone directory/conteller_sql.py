import sqlalchemy as db

engine = db.create_engine("sqlite:///DATA/sqlite.sqlite", echo=True)
connection = engine.connect()
metadata = db.MetaData()

phonebook = db.Table('PhoneBook', metadata, autoload=True, autoload_with=engine)