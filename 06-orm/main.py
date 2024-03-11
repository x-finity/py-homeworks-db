import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import xf_orm as xform

config = xform.load_config('config.json')
# print(config)
DSN = f'postgresql://{config["user"]}:{config["password"]}@{config["server"]}:{config["port"]}/{config["database"]}'

engine = sq.create_engine(DSN)

xform.create_db(engine)

Session = sessionmaker(bind=engine)
session = Session()

# xform.fill_db(session)

xform.publishers(session)

session.commit()