import streamlit as st
import json
import database as db
import os
from datetime import datetime, date, time
import uuid

# Cấu hình trang
st.set_page_config(
    page_title="Todo List Manager",
    page_icon="📝",
    layout="wide"
)

# File lưu trữ dữ liệu
DATA_FILE = "todos.json"

#BACKEND
def load_todos():
    """Tải dữ liệu todos từ file"""
    data = db.get_all_todos()
    print(data)
    if data:
        return data
    return []

def load_groups():
    """Tải danh sách nhóm từ database"""
    groups = db.get_all_groups()
    if groups:
        return [g for g in groups]
    return ["Công việc", "Học tập", "Cá nhân", "Khác"]

# Khởi tạo session state
if 'todos' not in st.session_state:
    st.session_state.todos = load_todos()
if 'groups' not in st.session_state:
    st.session_state.groups = load_groups()
if 'editing_todo' not in st.session_state:
    st.session_state.editing_todo = None

def save_data():
    """Lưu dữ liệu vào file"""
    data = {
        'todos': st.session_state.todos,
        'groups': st.session_state.groups
    }
    # db.save_data(data)

def add_todo(title, description, group, due_date, due_time, location, priority, is_important, url, image_path):
    """Thêm todo mới"""
    todo = {
        'id': str(uuid.uuid4()),
        'title': title,
        'description': description,
        'group': group,
        'due_date': due_date.isoformat() if due_date else None,
        'due_time': due_time.strftime('%H:%M') if due_time else None,
        'location': location,
        'priority': priority,
        'is_important': is_important,
        'url': url,
        'image_path': image_path,
        'completed': False,
        'created_at': datetime.now().isoformat()
    }
    st.session_state.todos.append(todo)
    db.add_todo(title, description, group, due_date.isoformat() if due_date else None, due_time.strftime('%H:%M') if due_time else None, location, priority, is_important, url, image_path, False, datetime.now().isoformat())

def update_todo(todo_id, title, description, group, due_date, due_time, location, priority, is_important, url, image_path):
    """Cập nhật todo"""
    for todo in st.session_state.todos:
        if todo[0] == todo_id:
            new_todo = list(todo)
            new_todo[1] = title
            new_todo[2] = description
            new_todo[3] = group
            new_todo[4] = due_date.isoformat() if due_date else None
            new_todo[5] = due_time.strftime('%H:%M') if due_time else None
            new_todo[6] = location
            new_todo[7] = priority
            new_todo[8] = is_important
            new_todo[9] = url
            new_todo[10] = image_path
            st.session_state.todos[st.session_state.todos.index(todo)] = tuple(new_todo)
            break
    db.update_todo(todo_id, title, description, group, 
                   due_date.isoformat() if due_date else None, 
                   due_time.strftime('%H:%M') if due_time else None, 
                   location, priority, is_important, url, image_path, False)

def delete_todo(todo_id):
    """Xóa todo"""
    st.session_state.todos = [todo for todo in st.session_state.todos if todo[0] != todo_id]
    db.delete_todo(todo_id)

def toggle_complete(todo_id):
    """Đánh dấu hoàn thành/chưa hoàn thành"""
    for todo in st.session_state.todos:
        if todo[0] == todo_id:
            new_todo = list(todo)
            new_todo[11] = not new_todo[11]
            st.session_state.todos[st.session_state.todos.index(todo)] = tuple(new_todo)
            break
    db.update_todo_completion(todo_id, new_todo[11])

def filter_todos(search_term="", selected_group="", filter_date=None, show_completed=True):
    """Lọc todos theo điều kiện"""
    filtered = st.session_state.todos.copy()
    
    # Lọc theo từ khóa tìm kiếm
    if search_term:
        filtered = [todo for todo in filtered
                   if search_term.lower() in todo[1].lower()
                   or search_term.lower() in todo[2].lower()]

    # Lọc theo nhóm
    if selected_group and selected_group != "Tất cả":
        filtered = [todo for todo in filtered if todo[3] == selected_group]
    
    # Lọc theo ngày
    if filter_date:
        filtered = [todo for todo in filtered
                   if todo[4] and todo[4] == filter_date.isoformat()]

    # Lọc theo trạng thái hoàn thành
    if not show_completed:
        filtered = [todo for todo in filtered if not todo[11]]

    return filtered

#FRONTEND
def display_todo_form(todo=None):
    """Hiển thị form thêm/sửa todo"""
    is_edit = todo is not None
    
    with st.form(key=f"todo_form_{todo[0] if is_edit else 'new'}"):
        st.subheader("✏️ Sửa công việc" if is_edit else "➕ Thêm công việc mới")
        
        col1, col2 = st.columns(2)
        
        with col1:
            title = st.text_input("Tiêu đề*", value=todo[1] if is_edit else "")
            description = st.text_area("Mô tả", value=todo[2] if is_edit else "")
            
            # Quản lý nhóm
            st.write("**Nhóm công việc**")
            col_group1, col_group2 = st.columns([3, 1])
            with col_group1:
                group = st.selectbox("Chọn nhóm", options=st.session_state.groups, 
                                   index=st.session_state.groups.index(todo[3]) if is_edit and todo[3] in st.session_state.groups else 0)
            with col_group2:
                if st.form_submit_button("➕ Nhóm mới"):
                    st.session_state.show_add_group = True
            
            # Thêm nhóm mới
            if 'show_add_group' in st.session_state and st.session_state.show_add_group:
                new_group = st.text_input("Tên nhóm mới")
                if st.form_submit_button("Thêm nhóm") and new_group and new_group not in st.session_state.groups:
                    st.session_state.groups.append(new_group)
                    db.add_group(new_group)
                    st.session_state.show_add_group = False
                    st.rerun()
        
        with col2:
            # Ngày giờ
            due_date = st.date_input("Ngày hết hạn", 
                                   value=datetime.fromisoformat(todo[4]).date() if is_edit and todo[4] else None)
            due_time = st.time_input("Giờ hết hạn",
                                   value=datetime.strptime(todo[5], '%H:%M').time() if is_edit and todo[5] else time(9, 0))

            location = st.text_input("Địa điểm", value=todo[6] if is_edit else "")

            # Độ ưu tiên
            priority_options = ["Thấp", "Trung bình", "Cao", "Rất cao"]
            priority = st.selectbox("Độ ưu tiên", options=priority_options,
                                  index=priority_options.index(todo[7]) if is_edit and todo[7] in priority_options else 1)

            is_important = st.checkbox("⭐ Công việc quan trọng",
                                     value=todo[8] if is_edit else False)

        # Đường dẫn và hình ảnh
        st.write("**Tài liệu đính kèm**")
        col3, col4 = st.columns(2)
        with col3:
            url = st.text_input("Đường dẫn URL", value=todo[9] if is_edit else "")
        with col4:
            image_path = st.text_input("Đường dẫn hình ảnh", value=todo[10] if is_edit else "")

        # Upload hình ảnh
        uploaded_file = st.file_uploader("Hoặc upload hình ảnh", type=['png', 'jpg', 'jpeg', 'gif'])
        if uploaded_file:
            # Lưu file upload
            upload_dir = "uploads"
            if not os.path.exists(upload_dir):
                os.makedirs(upload_dir)
            file_path = os.path.join(upload_dir, uploaded_file.name)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            image_path = file_path
        
        # Nút submit
        col_submit1, col_submit2, col_submit3 = st.columns([2, 1, 1])
        with col_submit1:
            submitted = st.form_submit_button("💾 Cập nhật" if is_edit else "➕ Thêm công việc", 
                                            type="primary", use_container_width=True)
        with col_submit2:
            if is_edit and st.form_submit_button("❌ Hủy", use_container_width=True):
                st.session_state.editing_todo = None
                st.rerun()
        
        if submitted and title:
            if is_edit:
                update_todo(todo[0], title, description, group, due_date, due_time, 
                          location, priority, is_important, url, image_path)
                st.session_state.editing_todo = None
                st.success("✅ Cập nhật công việc thành công!")
            else:
                add_todo(title, description, group, due_date, due_time, 
                        location, priority, is_important, url, image_path)
                st.success("✅ Thêm công việc thành công!")
            st.rerun()
        elif submitted and not title:
            st.error("❗ Vui lòng nhập tiêu đề công việc!")

def display_todo_card(todo):
    """Hiển thị card todo"""
    # Màu sắc theo độ ưu tiên
    priority_colors = {
        "Thấp": "#e8f5e8",
        "Trung bình": "#fff2cc", 
        "Cao": "#ffe6cc",
        "Rất cao": "#ffcccc"
    }
    
    # CSS cho card
    card_style = f"""
    <div style="
        background-color: {priority_colors.get(todo[7], '#f0f0f0')};
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid {'#ff6b6b' if todo[8] else '#4ecdc4'};
        margin-bottom: 10px;
        {'opacity: 0.6;' if todo[11] else ''}
    ">
    """
    
    with st.container():
        col1, col2, col3, col4, col5 = st.columns([0.5, 4, 1, 1, 1])
        
        with col1:
            # Checkbox hoàn thành
            if st.checkbox("", value=todo[11], key=f"complete_{todo[0]}"):
                if not todo[11]:
                    toggle_complete(todo[0])
                    st.rerun()
            elif todo[11]:
                toggle_complete(todo[0])
                st.rerun()
        
        with col2:
            # Thông tin todo
            title_style = "text-decoration: line-through;" if todo[11] else ""
            importance_icon = "⭐ " if todo[8] else ""
            st.markdown(f"**{importance_icon}{todo[1]}**", unsafe_allow_html=True)
            if todo[2]:
                st.write(todo[2])

            # Thông tin chi tiết
            details = []
            if todo[4]:
                date_str = datetime.fromisoformat(todo[4]).strftime('%d/%m/%Y')
                time_str = f" {todo[5]}" if todo[5] else ""
                details.append(f"📅 {date_str}{time_str}")

            if todo[6]:
                details.append(f"📍 {todo[6]}")
            
            details.append(f"🏷️ {todo[3]}")
            details.append(f"🔥 {todo[7]}")
            
            if details:
                st.caption(" | ".join(details))
            
            # Hiển thị URL và hình ảnh
            if todo[9]:
                st.markdown(f"🔗 [Link]({todo[9]})")

            if todo[10] and os.path.exists(todo[10]):
                try:
                    st.image(todo[10], width=200)
                except:
                    st.caption("❌ Không thể hiển thị hình ảnh")
        
        with col3:
            # Nút sửa
            if st.button("✏️", key=f"edit_{todo[0]}", help="Sửa"):
                st.session_state.editing_todo = todo[0]
                st.rerun()
        
        with col4:
            # Nút xóa
            if st.button("🗑️", key=f"delete_{todo[0]}", help="Xóa"):
                delete_todo(todo[0])
                st.success("🗑️ Đã xóa công việc!")
                st.rerun()

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
        completed_todos = len([t for t in st.session_state.todos if t[11]])
        important_todos = len([t for t in st.session_state.todos if t[8] and not t[11]])
        
        st.metric("Tổng công việc", total_todos)
        st.metric("Đã hoàn thành", completed_todos)
        st.metric("Quan trọng (chưa xong)", important_todos)
        
        if total_todos > 0:
            completion_rate = (completed_todos / total_todos) * 100
            st.metric("Tỷ lệ hoàn thành", f"{completion_rate:.1f}%")
    
    # Nội dung chính
    # Form thêm/sửa todo
    if st.session_state.editing_todo:
        editing_todo = next((t for t in st.session_state.todos if t[0] == st.session_state.editing_todo), None)
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
            filtered_todos.sort(key=lambda x: x[12], reverse=True)
        elif sort_option == "Ngày hết hạn":
            filtered_todos.sort(key=lambda x: x[4] or '9999-12-31')
        elif sort_option == "Độ ưu tiên":
            priority_order = {"Rất cao": 0, "Cao": 1, "Trung bình": 2, "Thấp": 3}
            filtered_todos.sort(key=lambda x: priority_order.get(x[7], 4))
        else:  # Tên công việc
            filtered_todos.sort(key=lambda x: x[1].lower())

        # Hiển thị todos
        for todo in filtered_todos:
            display_todo_card(todo)

if __name__ == "__main__":
    main()