import psycopg2 

conn = psycopg2.connect(
    host='localhost',
    dbname='suppliers',
    user='postgres',
    password='pft,fk'
)

cur = conn.cursor()

list = ['Coco', '5']

cur.execute('''INSERT INTO students_data(name, phone_number)VALUES (%s);''', (list,))
            
conn.commit()