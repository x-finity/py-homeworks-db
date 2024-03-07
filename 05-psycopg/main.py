import xf_DB as xfdb
import psycopg2
import json

if __name__ == "__main__":
    config = xfdb.load_config('config.json')
    conn = psycopg2.connect(database=config['database'], user=config['user'], password=config['password'])
    with conn.cursor() as cur:
        xfdb.create_client_db(conn, cur)
        xfdb.add_new_client(conn, cur, 'NoName', 'test@domain.lol', '123456789')
        xfdb.add_new_client(conn, cur, 'NoName2', 'test2@domain.lol', '234567890')
        xfdb.add_new_client(conn, cur, 'NoName3', 'test3@domain.lol')
        xfdb.modify_client(conn, cur, 'NoName')
        xfdb.delete_phone(conn, cur, 'NoName', '123456789')
        xfdb.add_new_phone(conn, cur, 'NoName', '123456000')
        xfdb.delete_user(conn, cur, 'test')
        xfdb.find_client(conn, cur, 'NoName')
        xfdb.find_client(conn, cur, 'NoName3')
        xfdb.find_client(conn, cur, email='test2@domain.lol')
    conn.close()
