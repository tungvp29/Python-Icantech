import streamlit as st
import json
import os
from datetime import datetime, date, time
import uuid

st.set_page_config(
    page_title="Todo List Manager",
    page_icon="📝",
    layout="wide"
)

DATA_FILE = "todos.json"

def load_todos():
    """Tải dữ liệu todos từ file"""
    return []

def load_groups():
    """Tải dữ liệu groups từ file"""
    return ['Công việc', 'Cá nhân', 'Học tập', 'Khác']

# Khởi tạo session state
if 'todos' not in st.session_state:
    st.session_state.todos = load_todos()
if 'groups' not in st.session_state:
    st.session_state.groups = load_groups()
if 'editing_todo' not in st.session_state:
    st.session_state.editing_todo = None

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

def display_todo_form(todo=None):
    """Hiển thị form thêm/sửa todo"""
    is_edit = todo is not None

    with st.sidebar:
        st.header("🔍 Tìm kiếm và lọc")
        search = st.text_input("Tìm kiếm công việc")
        group_filter = st.selectbox("Lọc theo nhóm", ["Tất cả"] + st.session_state.groups)
        filter_date = st.date_input("Lọc theo ngày", value=None)
        show_done = st.checkbox("Hiển thị công việc đã hoàn thành", value=True)

        st.markdown("---")
        st.header("📊 Thống kê")
        total = len(st.session_state.todos)
        done = sum(1 for t in st.session_state.todos if t["done"])
        important = sum(1 for t in st.session_state.todos if t["important"] and not t["done"])
        st.metric("Tổng công việc", total)
        st.metric("Đã hoàn thành", done)
        st.metric("Quan trọng (chưa xong)", important)

    with st.form(key=f"todo_form_{todo['id'] if is_edit else 'new'}"):
        st.subheader("✏️ Sửa công việc" if is_edit else "➕ Thêm công việc mới")

        col1, col2 = st.columns(2)

        with col1:
            title = st.text_input("Tiêu đề*", value=todo['title'] if is_edit else "")
            description = st.text_area("Mô tả", value=todo['description'] if is_edit else "")

            # Quản lý nhóm
            st.write("**Nhóm công việc**")
            col_group1, col_group2 = st.columns([3, 1])
            with col_group1:
                group = st.selectbox("Chọn nhóm", options=st.session_state.groups, 
                                index=st.session_state.groups.index(todo['group']) if is_edit and todo['group'] in st.session_state.groups else 0)
            with col_group2:
                if st.form_submit_button("➕ Nhóm mới"):
                    st.session_state.show_add_group = True

            # Thêm nhóm mới
            if 'show_add_group' in st.session_state and st.session_state.show_add_group:
                new_group = st.text_input("Tên nhóm mới")
                if st.form_submit_button("Thêm nhóm") and new_group and new_group not in st.session_state.groups:
                    st.session_state.groups.append(new_group)
                    save_data()
                    st.session_state.show_add_group = False
                    st.rerun()

        with col2:
            # Ngày giờ
            due_date = st.date_input("Ngày hết hạn", value=datetime.fromisoformat(todo['due_date']).date() if is_edit and todo['due_date'] else None)
            due_time = st.time_input("Giờ hết hạn", value=datetime.strptime(todo['due_time'], '%H:%M').time() if is_edit and todo['due_time'] else time(9, 0))

            location = st.text_input("Địa điểm", value=todo['location'] if is_edit else "")

            # Độ ưu tiên
            priority_options = ["Thấp", "Trung bình", "Cao", "Rất cao"]
            priority = st.selectbox("Độ ưu tiên", options=priority_options, index=priority_options.index(todo['priority']) if is_edit and todo['priority'] in priority_options else 1)

            is_important = st.checkbox("⭐ Công việc quan trọng", value=todo['is_important'] if is_edit else False)

def main():
    """Hàm chính"""
    st.title("📝 Todo List Manager")
    st.markdown("---")
    
    # Sidebar cho bộ lọc
    with st.sidebar:
        st.header("🔍 Tìm kiếm & Lọc")
        
        # Tìm kiếm
        search_term = st.text_input("🔍 Tìm kiếm công việc")
        
        # Lọc theo nhóm
        group_options = ["Tất cả"] + st.session_state.groups
        selected_group = st.selectbox("🏷️ Lọc theo nhóm", options=group_options)
        
        # Lọc theo ngày
        filter_date = st.date_input("📅 Lọc theo ngày", value=None)
        
        # Hiển thị công việc đã hoàn thành
        show_completed = st.checkbox("✅ Hiển thị công việc đã hoàn thành", value=True)
        
        st.markdown("---")
        
        # Thống kê
        st.header("📊 Thống kê")
        total_todos = len(st.session_state.todos)
        print(st.session_state.todos)
        completed_todos = len([t for t in st.session_state.todos if t['completed'] == 1])
        important_todos = len([t for t in st.session_state.todos if t['is_important'] and not t['completed']])
        
        st.metric("Tổng công việc", total_todos)
        st.metric("Đã hoàn thành", completed_todos)
        st.metric("Quan trọng (chưa xong)", important_todos)
        
        if total_todos > 0:
            completion_rate = (completed_todos / total_todos) * 100
            st.metric("Tỷ lệ hoàn thành", f"{completion_rate:.1f}%")
    
    # Nội dung chính
    # Form thêm/sửa todo
    if st.session_state.editing_todo:
        editing_todo = next((t for t in st.session_state.todos if t['id'] == st.session_state.editing_todo), None)
        if editing_todo:
            display_todo_form(editing_todo)
        else:
            st.session_state.editing_todo = None
    else:
        display_todo_form()
    
    st.markdown("---")
    
    # Hiển thị danh sách todos
    st.header("📋 Danh sách công việc")
    
    # Lọc todos
    filtered_todos = filter_todos(search_term, selected_group, filter_date, show_completed)
    
    if not filtered_todos:
        st.info("📝 Không có công việc nào phù hợp với bộ lọc!")
    else:
        # Sắp xếp todos
        sort_option = st.selectbox("📊 Sắp xếp theo", 
                                 ["Ngày tạo (mới nhất)", "Ngày hết hạn", "Độ ưu tiên", "Tên công việc"])
        
        if sort_option == "Ngày tạo (mới nhất)":
            filtered_todos.sort(key=lambda x: x['created_at'], reverse=True)
        elif sort_option == "Ngày hết hạn":
            filtered_todos.sort(key=lambda x: x['due_date'] or '9999-12-31')
        elif sort_option == "Độ ưu tiên":
            priority_order = {"Rất cao": 0, "Cao": 1, "Trung bình": 2, "Thấp": 3}
            filtered_todos.sort(key=lambda x: priority_order.get(x['priority'], 4))
        else:  # Tên công việc
            filtered_todos.sort(key=lambda x: x['title'].lower())

        # # Hiển thị todos
        # for todo in filtered_todos:
        #     display_todo_card(todo)

if __name__ == "__main__":
    main()
            