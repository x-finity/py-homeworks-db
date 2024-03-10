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

class Stock(Base):
    __tablename__ = 'stock'
    stock_id = sq.Column(sq.Integer, primary_key=True)
    count = sq.Column(sq.Integer, nullable=False)

class Sale(Base):
    __tablename__ = 'sale'
    sale_id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Integer, nullable=False)
    date_sale = sq.Column(sq.Date, nullable=False)
    stock_id = sq.Column(sq.Integer, sq.ForeignKey('stock.stock_id'), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)
    stock = relationship(Stock, backref='sale')

class Shop(Base):
    __tablename__ = 'shop'
    shop_id = sq.Column(sq.Integer, sq.ForeignKey('stock.stock_id'), primary_key=True)
    name = sq.Column(sq.String(length=40), nullable=False)
    stock = relationship(Stock, backref='shop')

class Book(Base):
    __tablename__ = 'book'
    book_id = sq.Column(sq.Integer, sq.ForeignKey('stock.stock_id'), primary_key=True)
    title = sq.Column(sq.String(length=40), nullable=False)
    id_publisher = sq.Column(sq.Integer, nullable=False)
    stock = relationship(Stock, backref='book')

class Publisher(Base):
    __tablename__ = 'publisher'
    publisher_id = sq.Column(sq.Integer, sq.ForeignKey('stock.stock_id'), primary_key=True)
    name = sq.Column(sq.String(length=40), nullable=False)
    stock = relationship(Stock, backref='publisher')