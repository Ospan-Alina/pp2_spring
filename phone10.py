import psycopg2
import csv

conn = psycopg2.connect(
    host='localhost',
    dbname='suppliers',
    user='postgres',
    password='pft,fk'
)

cur = conn.cursor()

# to create a new table
cur.execute('''CREATE TABLE IF NOT EXISTS students_data(
    name VARCHAR(50),
    phone_number VARCHAR(50) PRIMARY KEY
);
''')



def insert():
    print('Write name and phone number')
    name = input('')
    phone_number = input('')
    cur.execute('''INSERT INTO students_data(name, phone_number)VALUES (%s, %s);''', (name, phone_number))
            
    conn.commit()
        
def update():
    print('What do you want to update? Name or phone number?')
    answer = input('')  
    if answer == 'name':
        print('Write current name:')
        current_name = input('')
        print('Write new name:')
        new_name = input('')
        cur.execute('''UPDATE students_data SET name = %s WHERE name = %s;''', (new_name, current_name))  
        conn.commit()
        
    if answer == 'phone number':
        print('Write current number:')
        current_num = input('')
        print('Write new number:')
        new_num = input('')
        cur.execute('''UPDATE students_data SET phone_number = %s WHERE phone_number = %s;''', (new_num, current_num))  
        conn.commit()
        
def remove():
    print('Write phone number:')
    r_num = input('')
    cur.execute('''DELETE FROM students_data
            WHERE phone_number = %s;''', (r_num,))
    conn.commit()
    

while True:
    print('\nChoose an option:')
    print('1 - Insert')
    print('2 - Update')
    print('3 - Remove')
    print('4 - Exit')
    option = input('Option: ')

    if option == '1':
        insert()
    elif option == '2':
        update()
    elif option == '3':
        remove()
    elif option == '4':
        print('Exiting program...')
        break
    else:
        print('Invalid option!')
        


    
    