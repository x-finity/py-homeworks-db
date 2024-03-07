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

def add_new_client(connection, cursor, name, email, phone):
    try:
        cursor.execute('''INSERT INTO client(name, email) VALUES (%s, %s)''', (name, email))
    except psycopg2.errors.UniqueViolation:
        connection.rollback()
        print('Client already exists')
        return
    client_id = cursor.fetchone()[0]
    cursor.execute('''INSERT INTO phones(client_id, phone) VALUES (%s, %s)''', (client_id, phone))
    connection.commit()
    return client_id

def add_new_phone(connection, cursor, client_name, phone):
    cursor.execute('''SELECT id FROM client WHERE name = %s''', (client_name,))
    client_id = cursor.fetchone()[0]
    try:
        cursor.execute('''INSERT INTO phones(client_id, phone) VALUES (%s, %s)''', (client_id, phone))
    except psycopg2.errors.UniqueViolation:
        connection.rollback()
        print('Phone already exists')
        return
    connection.commit()

def modify_client(connection, cursor, client_name, name=None, email=None, phone=None):
    if not name and not email and not phone:
        print('No input data')
        return
    cursor.execute('''SELECT id FROM client WHERE name = %s''', (client_name,))
    client_id = cursor.fetchone()[0]
    if name:
        cursor.execute('''UPDATE client SET name = %s WHERE id = %s''', (name, client_id))
    if email:
        cursor.execute('''UPDATE client SET email = %s WHERE id = %s''', (email, client_id))
    if phone:
        cursor.execute('''UPDATE phones SET phone = %s WHERE client_id = %s''', (phone, client_id))
    connection.commit()