import json
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

def load_config(path):
    with open(path, 'r') as f:
        config = json.load(f)
        config.setdefault('user', 'postgres')
        config.setdefault('password', 'postgres')
        config.setdefault('database', 'orm_db')
        config.setdefault('server', '127.0.0.1')
        config.setdefault('port', 5432)
    return config

def create_db(engine):
    Base.metadata.create_all(engine)


class Publisher(Base):
    __tablename__ = 'publisher'
    id_publisher = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), nullable=False)

class Book(Base):
    __tablename__ = 'book'
    id_book = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=40), nullable=False)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey('publisher.id_publisher'), nullable=False)
    publisher = relationship(Publisher, backref='book')

class Shop(Base):
    __tablename__ = 'shop'
    id_shop = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), nullable=False)

class Stock(Base):
    __tablename__ = 'stock'
    id_stock = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey('book.id_book'), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey('shop.id_shop'), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)
    book = relationship(Book, backref='stock')
    shop = relationship(Shop, backref='stock')

class Sale(Base):
    __tablename__ = 'sale'
    id_sale = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Integer, nullable=False)
    date_sale = sq.Column(sq.Date, nullable=False)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey('stock.id_stock'), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)
    stock = relationship(Stock, backref='sale')



def fill_db(session, file = 'tests_data.json'):
    with open(file) as f:
        data = json.loads(f.read())

    for item in data:
        # id_name=f'id_{item["model"]}'
        # print(id_name)
        # item.update({id_name: item.pop('pk')})

        # dict = {id_name: y for x, y in item.items() if x == 'pk'}
        # print(dict)
        # print(item)
        # session.add(eval(item['model'].capitalize())(eval(id_name)=item['pk'], **item['fields']))
        session.add(eval(item['model'].capitalize())({f'id_{item["model"]}':item['pk']}, **item['fields']))
        # session.add(eval(item['model'].capitalize())(id_name=item['pk'], **item['fields']))
        # session.add(eval(item['model'].capitalize())(**dict, **item['fields']))
        
        # if item['model'] == 'stock':
        #     session.add(Stock(**item['fields'])
        # elif item['model'] == 'sale':
        #     session.add(eval(item['model'].capitalize())(id_sale=item['pk']), **item['fields'])
        # if item['model'] == 'shop':
        #     session.add(Shop(**item['fields']))
        # if item['model'] == 'book':
        #     session.add(Book(**item['fields']))
        # if item['model'] == 'publisher':
        #     session.add(Publisher(**item['fields'])) 