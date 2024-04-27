from snake1 import name, score
import psycopg2

conn = psycopg2.connect(
    host='localhost',
    dbname='suppliers',
    user='postgres',
    password='pft,fk'
)

cur = conn.cursor()


cur.execute('''INSERT INTO score_table (name, score) VALUES (%s, %s);''', (name, score))

conn.commit()



