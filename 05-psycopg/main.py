import xf_DB as xfdb
import psycopg2
import json

if __name__ == "__main__":
    config = xfdb.load_config('config.json')
    conn = psycopg2.connect(database=config['database'], user=config['user'], password=config['password'])
    with conn.cursor() as cur:
        xfdb.create_client_db(conn, cur)
        xfdb.add_new_client(conn, cur, 'NoName', 'test@domain.lol', '123456789')
        xfdb.add_new_phone(conn, cur, 'NoName', '123456789')
        xfdb.modify_client(conn, cur, 'NoName')

    conn.close()
