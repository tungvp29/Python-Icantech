import sqlite3 as sql
import uuid

conn = sql.connect('data.db', check_same_thread=False)
c = conn.cursor()

def create_table():
    c.execute('''CREATE TABLE IF NOT EXISTS todos
                  (id GUID PRIMARY KEY,
                   title TEXT NOT NULL,
                   description TEXT ,
                   "group" TEXT ,
                   due_date DATE ,
                   due_time TIME ,
                   location TEXT,
                   priority TEXT,
                   is_important BOOLEAN ,
                   url TEXT,
                   image_path TEXT,
                   completed BOOLEAN ,
                   created_at DATETIME )''')
    c.execute('''CREATE TABLE IF NOT EXISTS groups
                  (name TEXT PRIMARY KEY)''')
    conn.commit()

def add_todos(title, description, group, due_date, due_time, location, priority, is_important, url, image_path, completed, created_at = None):
    new_id = str(uuid.uuid4())
    c.execute('''INSERT INTO todos 
                    (id, title, description, "group", due_date, due_time, location, priority, is_important, url, image_path, completed, created_at)
                 VALUES 
                    (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 0, ?)''',
              (new_id, title, description, group, due_date, due_time, location, priority, is_important, url, image_path, completed, created_at))
    conn.commit()

def update_todo(id, title, description, group, due_date, due_time, location, priority, is_important, url, image_path, completed):
    c.execute('''UPDATE todos SET 
                    title = ?, 
                    description = ?, 
                    "group" = ?, 
                    due_date = ?, 
                    due_time = ?, 
                    location = ?, 
                    priority = ?, 
                    is_important = ?, 
                    url = ?, 
                    image_path = ?, 
                    completed = ? 
                 WHERE id = ?''',
              (title, description, group, due_date, due_time, location, priority, is_important, url, image_path, completed, id))
    print("Todo updated:", id)
    conn.commit()

def update_todo_completion(id, completed):
    c.execute('UPDATE todos SET completed = ? WHERE id = ?', (completed, id))
    conn.commit()

def delete_todo(id):
    c.execute('DELETE FROM todos WHERE id = ?', (id,))
    conn.commit()

def get_all_todos():
    c.execute('SELECT * FROM todos')
    return c.fetchall()

def get_todo_by_id(id):
    c.execute('SELECT * FROM todos WHERE id = ?', (id,))
    return c.fetchone()

def get_all_groups():
    c.execute('SELECT * FROM groups')
    return [row[0] for row in c.fetchall()]

def add_group(name):
    c.execute('INSERT OR IGNORE INTO groups (name) VALUES (?)', (name,))
    conn.commit()

create_table()
