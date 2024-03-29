import psycopg2
import json

def load_config(filename):
    with open (filename) as f:
        config = json.load(f)
    return config

def create_client_db(connection):
    with connection.cursor() as cursor:
        cursor.execute(''' CREATE TABLE IF NOT EXISTS client(
            client_id SERIAL PRIMARY KEY,
            name VARCHAR(40) NOT NULL,
            email VARCHAR(40) NOT NULL UNIQUE)''')
        cursor.execute(''' CREATE TABLE IF NOT EXISTS phones(
            phone_id SERIAL PRIMARY KEY,
            client_id INTEGER REFERENCES client(client_id),
            phone VARCHAR(40) UNIQUE)''')
    connection.commit()

def add_new_client(connection, name, email, phone=None):
    with connection.cursor() as cursor:
        try:
            cursor.execute('''INSERT INTO client(name, email) VALUES (%s, %s) RETURNING client_id''', (name, email))
        except psycopg2.errors.UniqueViolation:
            connection.rollback()
            print(f'Client "{name}" already exists')
            return
        client_id = cursor.fetchone()[0]
        if phone:
            cursor.execute('''INSERT INTO phones(client_id, phone) VALUES (%s, %s)''', (client_id, phone))
    connection.commit()
    return client_id

def add_new_phone(connection, client_name, phone):
    with connection.cursor() as cursor:
        cursor.execute('''SELECT client_id FROM client WHERE name = %s''', (client_name,))
        client_id = cursor.fetchone()[0]
        try:
            cursor.execute('''INSERT INTO phones(client_id, phone) VALUES (%s, %s)''', (client_id, phone))
        except psycopg2.errors.UniqueViolation:
            connection.rollback()
            print(f'Phone "{phone}" for client "{client_name}" already exists')
            return
    connection.commit()

def modify_client(connection, client_name, name=None, email=None, phone=None):
    with connection.cursor() as cursor:
        if not name and not email and not phone:
            print('modify client: No input data')
            return
        cursor.execute('''SELECT clientid FROM client WHERE name = %s''', (client_name,))
        client_id = cursor.fetchone()[0]
        if name:
            cursor.execute('''UPDATE client SET name = %s WHERE client_id = %s''', (name, client_id))
        if email:
            cursor.execute('''UPDATE client SET email = %s WHERE client_id = %s''', (email, client_id))
        if phone:
            cursor.execute('''UPDATE phones SET phone = %s WHERE client_id = %s''', (phone, client_id))
    connection.commit()

def delete_phone(connection, client_name, phone):
    with connection.cursor() as cursor:
        cursor.execute('''SELECT client_id FROM client WHERE name = %s''', (client_name,))
        client_id = cursor.fetchone()[0]
        cursor.execute('''DELETE FROM phones WHERE client_id = %s AND phone = %s''', (client_id, phone))
    connection.commit()

def delete_user(connection, client_name):
    with connection.cursor() as cursor:
        cursor.execute('''DELETE FROM phones WHERE client_id =
            (SELECT client_id FROM client WHERE name = %s)''', (client_name,))
        cursor.execute('''DELETE FROM client WHERE name = %s''', (client_name,))
    connection.commit()

def find_client(connection, client_name=None, email=None, phone=None):
    with connection.cursor() as cursor:
        if not client_name and not email and not phone:
            print('find client: No input data')
            return
        def print_result(search_query, client_name_n_email, phone):
            if not phone:
                print(f'Results for "{search_query}":\n\tName: {client_name_n_email[0]}\n\tEmail: {client_name_n_email[1]}')
            else:
                phone_list = []
                for tuple in phone:
                    phone_list.append(tuple[0])
                phone_list = ', '.join(phone_list)
                print(f'Results for "{search_query}":\n\tName: {client_name_n_email[0]}\n\tEmail: {client_name_n_email[1]}\n\tPhones: {phone_list}')
        if client_name:
            cursor.execute('''SELECT name, email FROM client WHERE name = %s''', (client_name,))
            client_name_n_email = cursor.fetchone()
            cursor.execute('''SELECT phone FROM phones WHERE client_id = (SELECT client_id FROM client WHERE name = %s)''', (client_name,))
            phone = cursor.fetchall()
            print_result(client_name, client_name_n_email, phone)
            return
        if email:
            cursor.execute('''SELECT name, email FROM client WHERE email = %s''', (email,))
            client_name_n_email = cursor.fetchone()
            cursor.execute('''SELECT phone FROM phones WHERE client_id = (SELECT client_id FROM client WHERE email = %s)''', (email,))
            phone = cursor.fetchall()
            print_result(email, client_name_n_email, phone)
            return
        if phone:
            cursor.execute('''SELECT name, email FROM client WHERE client_id IN
                (SELECT client_id FROM phones WHERE phone = %s)''', (phone,))
            client_name_n_email = cursor.fetchone()
            cursor.execute('''SELECT phone FROM phones WHERE client_id = %s''', (client_name_n_email[0],))
            phone = cursor.fetchall()
            print_result(phone, client_name_n_email, phone)
            return