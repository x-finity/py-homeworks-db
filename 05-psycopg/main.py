import xf_DB as xfdb
import psycopg2
import json

config = xfdb.load_config('config.json')
conn = psycopg2.connect(database=config['database'], user=config['user'], password=config['password'])
with conn.cursor() as cur:
    xfdb.create_client_db(conn, cur)

conn.close()
