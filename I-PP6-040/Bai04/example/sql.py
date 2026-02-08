import sqlite3

conn = sqlite3.connect('data1.db', check_same_thread=False)
c = conn.cursor()

def CreateTable(tableName, columns):
    c.execute(f'''
        CREATE TABLE IF NOT EXISTS {tableName}(
            ten TEXT,
            tuoi NUMBER
        )
    ''')
    conn.commit()

def InsertData(tableName, data):
    c.execute(f'''
    INSERT INTO {tableName} (ten, tuoi) 
    VALUES
    	({data.ten}, {data.tuoi})
    ''')
    conn.commit()

def GetAllData(tableName):
    c.execute(f'''
    SELECT *
    FROM {tableName}
    ''')
    data = c.fetchall()
    return data

def LoadTodos():
    c.execute(f'''
    SELECT *
    FROM todos
    ''')
    data = c.fetchall()
    return data