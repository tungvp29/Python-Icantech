import sqlite3 as sql


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
    conn.commit()

import uuid
def add_todos(title, description, group, due_date, due_time, location, priority, is_important, url, image_path, completed, created_at):
    new_id = str(uuid.uuid4())
    c.execute('''INSERT INTO todos 
                    (id, title, description, "group", due_date, due_time, location, priority, is_important, url, image_path, completed, created_at)
                 VALUES 
                    (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
              (new_id, title, description, group, due_date, due_time, location, priority, is_important, url, image_path, completed, created_at))
    conn.commit()
add_todos('Học Python', 'Học Python cơ bản', 'Học tập', '2023-10-01', '10:00', 'Nhà', 'Cao', True, '', '', False, '2023-09-25 09:00:00')

def get_all_todos():
    c.execute('SELECT * FROM todos')
    return c.fetchall()

def get_todo_by_id(id):
    c.execute('SELECT * FROM todos WHERE id = ?', (id,))
    return c.fetchone()

def save_data(data):
    c.execute('DELETE FROM todos')  # Xóa tất cả dữ liệu hiện có
    for todo in data.get('todos', []):
        add_todos(
            todo['id'],
            todo['title'],
            todo.get('description', ''),
            todo.get('group', ''),
            todo.get('due_date', None),
            todo.get('due_time', None),
            todo.get('location', ''),
            todo.get('priority', 'Medium'),
            todo.get('is_important', False),
            todo.get('url', ''),
            todo.get('image_path', ''),
            todo.get('completed', False),
            todo.get('created_at', None)
        )
    conn.commit()

create_table()
