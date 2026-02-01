import json

def load_todos():
    """Tải dữ liệu todos từ file"""
    data = []
    with open('database/todo.json', 'r') as file:
        data = json.load(file)
    return data['todos']

def load_groups():
    """Tải dữ liệu groups từ file"""
    data = []
    with open('database/todo.json', 'r') as file:
        data = json.load(file)
    return data['groups']

def save_data():
    """Lưu dữ liệu vào file"""
    pass

def add_todo(title, description, group, due_date, due_time, location, priority, is_important, url, image_path):
    pass

def update_todo(todo_id, title, description, group, due_date, due_time, location, priority, is_important, url, image_path):
    pass

def delete_todo(todo_id):
    pass

def toggle_complete(todo_id):
    pass

def filter_todos(search_term="", selected_group="", filter_date=None, show_completed=True):
    pass