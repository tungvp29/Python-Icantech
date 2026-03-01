import json
import todoDB as db

def load_todos():
    """Tải dữ liệu todos từ file"""
    data = db.get_all_todos()
    return data

def load_groups():
    """Tải dữ liệu groups từ file"""
    groups = db.get_all_groups()
    return groups

def add_todo(title, description, group, due_date, due_time, location, priority, is_important, url, image_path):
    db.add_todos(title, description, group, due_date.isoformat() if due_date else None, due_time.strftime('%H:%M') if due_time else None, location, priority, is_important, url, image_path)

def update_todo(todo_id, title, description, group, due_date, due_time, location, priority, is_important, url, image_path):
    db.update_todo(todo_id, title, description, group, due_date.isoformat() if due_date else None, due_time.strftime('%H:%M') if due_time else None, location, priority, is_important, url, image_path)

def delete_todo(todo_id):
    db.delete_todo(todo_id)

def toggle_complete(todo_id, completed):
    db.update_todo_completion(todo_id, completed)

def filter_todos(search_term="", selected_group="", filter_date=None, show_completed=True):
    pass

def add_group(name):
    db.add_group(name)