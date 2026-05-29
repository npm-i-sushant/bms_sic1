import pymysql

def connect_db(database_name):
    try:
        connection = pymysql.connect(user = 'root', password = 'root', host='localhost', port=3306,database=database_name, charset='UTF8')
        print('DB Connected')
    except:
        print("DB Connection Failed")
    return connection

def disconnect_db(connection):
    connection.close()
    print('DB Disconnected')

def create_table(connection):
    query = 'create table people(id int primary key auto_increment, name varchar(64) not null, gender bool not null, location varchar(32));'
    try:

        cursor = connection.cursor()
        count = cursor.execute(query)
        if count == 1:
            print("Table Creation Successfull")
        else:
            print("Table Creation Failed")
        connection.commit()
        cursor.close()
        disconnect_db(connection)

    except:
        print("Table Creation Error")


def create_person_demo():
    query='insert into people(name, gender, location, age) values("Taran", false, "Majestic", 18);'
    try:
        connection=connect_db()
        cursor = connection.cursor()
        count = cursor.execute(query)
        if count == 0:
            print("person created")
        else:
            print("person Creation Failed")
        cursor.close()
        disconnect_db(connection)

    except Exception as e:
        print("person Creation Error")
        print(e.msg())


def read_person():
    name=input('enter person name:')
    age=int(input('enter person age:'))
    gender=input('enter person gender (m/f):')
    location=input('enter person location:')
    if gender.lower() == 'f':
        gender= True
    else:
        gender = False
    return (name, gender, age, location)


def create_person():
    query='insert into people(name, gender, location, age) values(%s, %s, %s, %s);'
    try:
        person=read_person()
        connection=connect_db()
        cursor = connection.cursor()
        count = cursor.execute(query, person)
        print(f'count={count}')
        if count == 1:
            print("person created")
        else:
            print("person Creation Failed")
        cursor.close()
        disconnect_db(connection)

    except:
        print("person Creation Error")

        
def update_person():
    id = int(input('enter id of the person to be updated:'))
    new_location = input('enter new location of person:')
    query='update people set location = %s where id = %s'
    try:
        connection=connect_db()
        cursor = connection.cursor()
        count = cursor.execute(query, (new_location, id))
        connection.commit()
        print(f'count = {count}')
        if count == 1:
            print(f'peron with id={id} is updated')
            
        else:
            print(f'peron with id={id} not found')
        cursor.close()
        disconnect_db(connection)

    except:
        print("peron updation failed")


def search_person():
    id = int(input('enter id of the person to be s earched:'))
    query=f'select * from people where id={id};'
    try:
        
        connection=connect_db()
        cursor = connection.cursor()
        count = cursor.execute(query)
        print(f'count = {count}')
        if count == 1:
            row= cursor.fetchone()
            print(row)
            print(type(row))
            
        else:
            print("no person was found")
        connection.commit()
        cursor.close()
        disconnect_db(connection)

    except:
        print("listing the people failed")



def delete_person():
    id = int(input('enter id of the person to be deleted:'))
    query=f'delete from people where id={id}'
    try:
        
        connection=connect_db()
        cursor = connection.cursor()
        count = cursor.execute(query)
        connection.commit()
        print(f'count = {count}')
        if count == 1:
            print(f'peron with id={id} is deleted')
            
        else:
            print(f'peron with id={id} not found')
        cursor.close()
        disconnect_db(connection)

    except:
        print("peron deletion failed")



def list_people():
    query='select * from people;'
    try:
        
        connection=connect_db()
        cursor = connection.cursor()
        count = cursor.execute(query)
        
        if count >= 1:
            rows= cursor.fetchall()
            for row in rows:
                print(row)
               
            
        else:
            print("no person was found")
        connection.commit()
        cursor.close()
        disconnect_db(connection)

    except:
        print("listing the people failed")



list_people()