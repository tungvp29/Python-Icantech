import sqlite3 as sql

conn = sql.connect('data.db', check_same_thread=False)
c = conn.cursor()

def create_table():
    c.execute('''
        CREATE TABLE IF NOT EXISTS Person(
            ten TEXT,
            tuoi NUMBER)
    ''')
    conn.commit()

def add_person(ten, tuoi):
    c.execute('''
              INSERT INTO Person (ten, tuoi) 
              VALUES 
                (?, ?)
              ''', (ten, tuoi))
    conn.commit()



def add_todo(title, description, group, due_date, due_time, location, priority, is_important, url, image_path, completed, created_at):
    c.execute('''
              INSERT INTO todos (
              id, title, description, "group", due_date, due_time, location, priority, is_important, url, image_path, completed, created_at) 
              VALUES 
                (new_id, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
              ''', (title, description, group, due_date, due_time, location, priority, is_important, url, image_path, completed, created_at))
    conn.commit()

def update_person(tuoi):
    c.execute('''
              UPDATE Person 
              SET tuoi = ?           
              ''', (tuoi,))
    conn.commit()

def delete_person(ten):
    c.execute('''
              DELETE FROM Person 
              WHERE ten = ? AND tuoi = 25
              ''', (ten,))
    conn.commit()

def get_all_person():
    c.execute('''
              SELECT * 
              FROM Person
              WHERE ten LIKE '%Nguyễn Văn Nam%'
              ''')
    return c.fetchall()

create_table()
# update_person(15)
# delete_person('Nguyễn Văn Nam')
# print(get_all_person())
