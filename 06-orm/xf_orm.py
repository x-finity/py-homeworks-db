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
    id_stock = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, nullable=False, unique=True)
    id_shop = sq.Column(sq.Integer, nullable=False, unique=True)
    count = sq.Column(sq.Integer, nullable=False)

class Sale(Base):
    __tablename__ = 'sale'
    id_sale = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Integer, nullable=False)
    date_sale = sq.Column(sq.Date, nullable=False)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey('stock.id_stock'), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)
    stock = relationship(Stock, backref='sale')

class Shop(Base):
    __tablename__ = 'shop'
    id_shop = sq.Column(sq.Integer, sq.ForeignKey('stock.id_shop'), primary_key=True)
    name = sq.Column(sq.String(length=40), nullable=False)
    stock = relationship(Stock, backref='shop')

class Book(Base):
    __tablename__ = 'book'
    id_book = sq.Column(sq.Integer, sq.ForeignKey('stock.id_book'), primary_key=True)
    title = sq.Column(sq.String(length=40), nullable=False)
    id_publisher = sq.Column(sq.Integer, nullable=False, unique=True)
    stock = relationship(Stock, backref='book')

class Publisher(Base):
    __tablename__ = 'publisher'
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey('book.id_publisher'), primary_key=True)
    name = sq.Column(sq.String(length=40), nullable=False)
    book = relationship(Book, backref='publisher')

def fill_db(session):
    pass