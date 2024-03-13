import json
import psycopg2
import sqlalchemy
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

def dsn(config):
    return f'postgresql://{config["user"]}:{config["password"]}@{config["server"]}:{config["port"]}/{config["database"]}'

def create_db(engine):
    Base.metadata.create_all(engine)


class Publisher(Base):
    __tablename__ = 'publisher'
    def __str__(self):
        return self.name
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
    name = sq.Column(sq.String(length=40), nullable=False, unique=True)

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
    price = sq.Column(sq.Float, nullable=False)
    date_sale = sq.Column(sq.Date, nullable=False)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey('stock.id_stock'), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)
    stock = relationship(Stock, backref='sale')



def fill_db(session, file = 'tests_data.json', echo=False):
    with open(file) as f:
        data = json.loads(f.read())
    error_stack = []
    for item in data:
        id_name=f'id_{item["model"]}'
        dict = {id_name: item['pk']}  
        try:
            session.add(eval(item['model'].capitalize())(**dict, **item['fields']))
            session.commit()
        except sqlalchemy.exc.IntegrityError:
            session.rollback()
            error_stack.append(f'Item {item["pk"]} in {item["model"]} already exists')
            continue
    if echo: print(error_stack)

def publishers(session):
    for publisher in session.query(Publisher).all():
        print(f'book: {publisher.book[0].title} | price: {publisher.book[0].stock[0].sale[0].price} | shop: {publisher.book[0].stock[0].shop.name} | sale date: {publisher.book[0].stock[0].sale[0].date_sale}')
    return

def books_by_publisher(session, publisher):
    q = sq.select(Book.title, Shop.name, Sale.price, Sale.date_sale) \
        .select_from(Book) \
        .join(Publisher, Publisher.id_publisher == Book.id_publisher) \
        .join(Stock, Stock.id_book == Book.id_book) \
        .join(Shop, Shop.id_shop == Stock.id_shop) \
        .join(Sale, Sale.id_stock == Stock.id_stock) \
            .where(Publisher.name == publisher)

    for book in session.execute(q).all():
        print(f'book: {book.title:<40}| shop: {book.name:<10}| price: {book.price:<6}| sale date: {book.date_sale}')
    return