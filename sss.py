import psycopg2
import csv

conn = psycopg2.connect(
    host='localhost',
    dbname='suppliers',
    user='postgres',
    password='pft,fk'
)

cur = conn.cursor()

print(cur.execute('''select from students_data where name = 'hi';'''))
conn.commit()