import psycopg2
import json

def load_config(filename):
    with open (filename) as f:
        config = json.load(f)
    return config

def create_client_db(connection, cursor):
    cursor.execute(''' CREATE TABLE IF NOT EXISTS client(
        id SERIAL PRIMARY KEY,
        name VARCHAR(40) NOT NULL,
        email VARCHAR(40) NOT NULL UNIQUE)''')
    cursor.execute(''' CREATE TABLE IF NOT EXISTS phones(
        id SERIAL PRIMARY KEY,
        client_id INTEGER REFERENCES client(id),
        phone VARCHAR(40) UNIQUE)''')
    connection.commit()