import psycopg2

conn = psycopg2.connect(
    host='localhost',
    dbname='suppliers',
    user='postgres',
    password='pft,fk'
)

cur = conn.cursor()

# cur.execute('DROP TABLE students_data')

# to create a new table
cur.execute('''CREATE TABLE IF NOT EXISTS students_data(
    name VARCHAR(50),
    phone_number VARCHAR(50) PRIMARY KEY
);
''')

# to insert new values
cur.execute('''INSERT INTO students_data(name, phone_number)VALUES
            ('Alina', '74747474'),
            ('TFGHJGK','11111111');
           ''')

# to update new values
print('Do you want to insert new contact?')
answer1 = input()
if answer1 == 'Yes':
    name = input('Enter name: ')
    phone_number = input('Enter phone number: ')
    cur.execute('''INSERT INTO students_data(name, phone_number)VALUES (%s, %s)''', (name, phone_number))
    conn.commit()

print('Which one you want to change, name or phone number?')
answer2 = input()
if answer2 == 'name':
    old_name = input('Enter old name: ')
    new_name = input('Enter new name: ')
    cur.execute('''UPDATE students_data
                    SET name  = %s
                    WHERE name = %s''', (new_name, old_name))
    conn.commit()
if answer2 == 'phone number':
    name = input('Enter name: ')
    new_number = input('Enter new phone number: ')
    cur.execute('''UPDATE students_data
                    SET phone_number = %s
                    WHERE name = %s''', (new_number, name))
    conn.commit()

print('Do you want to remove contact?')
answer3 = input()
if answer3 == 'yes':
    name = input('Enter name: ')
    cur.execute('''DELETE FROM students_data
            WHERE name = %s''', (name,))
    conn.commit()

conn.close()
