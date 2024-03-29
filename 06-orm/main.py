import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import xf_orm as xform

config = xform.load_config('config.json')
# print(config)
# DSN = f'postgresql://{config["user"]}:{config["password"]}@{config["server"]}:{config["port"]}/{config["database"]}'
DSN = xform.dsn(config)

engine = sq.create_engine(DSN) #, echo=True)

xform.create_db(engine)

Session = sessionmaker(bind=engine)
session = Session()

xform.fill_db(session, echo=False)

# xform.publishers(session)
if __name__ == '__main__':
    publisher = input('Enter publisher name: (Enter for default)')
    if not publisher: publisher = 'O\u2019Reilly'

    xform.books_by_publisher(session, publisher)

