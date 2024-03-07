import psycopg2
import json

with open ('config.json') as f:
    config = json.load(f)

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

conn = psycopg2.connect(database=config['database'], user=config['user'], password=config['password'])
with conn.cursor() as cur:
    create_client_db(conn, cur)

conn.close()
