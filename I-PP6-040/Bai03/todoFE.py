import streamlit as st
from datetime import datetime, date, time
import json
import os
from todoBE import load_todos

st.set_page_config(
    page_title="Todo List Manager",
    page_icon="",
    layout="wide"
)

is_edit = False
groups = ['Công việc', 'Giải trí', 'Học tập']
def display_todo_form(todo = None):
    show_add_group = False
    with st.form(key=f'todo_form_{todo['id'] if is_edit == True else 'new'}'):
        st.subheader("Sửa công việc" if is_edit == True else 'Thêm mới công việc') 
        col1, col2 = st.columns(2)

        with col1:
            title = st.text_input("Tiêu đề",  value=todo['title'] if is_edit else '')
            description = st.text_area("Mô tả", value=todo['description'] if is_edit else '')
            st.write("**Nhóm công việc**")
            col_group1, col_group2 = st.columns([3,1])
            with col_group1:
                group = st.selectbox("Chọn nhóm", options = groups)
            with col_group2:
                if st.form_submit_button('Nhóm mới'):
                    show_add_group = True

            if show_add_group:
                new_group = st.text_input("Tên nhóm mới")
                if st.form_submit_button("Thêm nhóm") and new_group:
                    groups.append(new_group)
                    show_add_group = False
                    st.rerun()
        with col2:
            due_date = st.date_input("Ngày hết hạn",  value=datetime.fromisoformat(todo['due_date']).date() if is_edit else None)
            due_time = st.time_input("Giờ hết hạn",  value=datetime.strptime(todo['due_time']).time() if is_edit else time(9,0))
            location = st.text_input("Địa điểm",  value=todo['location'] if is_edit else '')
            priority_options = ['Thấp', 'Trung bình', 'Cao', 'Rất cao']
            priority = st.selectbox("Độ ưu tiên", options = priority_options)
            is_important = st.checkbox('Công việc quan trọng', value=todo['is_important'] if is_edit else False)

        col3, col4 = st.columns(2)
        with col3:
            url = st.text_input('Đường dẫn URL', value=todo['url'] if is_edit else '')
        with col4:
            image_path = st.text_input('Hình ảnh', value=todo['image_path'] if is_edit else '')

        uploaded_file = st.file_uploader("Upload hình ảnh", type=['png', 'jpg', 'jpeg', 'pdf'])
        if uploaded_file:
            #Lưu file đã upload
            upload_dir = 'uploads'
            if not os.path.exists(upload_dir):
                os.makedirs(upload_dir)
            file_path = os.path.join(upload_dir, uploaded_file.name)
            with open(file_path, 'wb') as f:
                f.write(uploaded_file.getbuffer())
            image_path = file_path

        col_submit1, col_submit2, col_submit3 = st.columns([2,1,1])
        with col_submit1:
            st.form_submit_button("Cập nhật" if is_edit else 'Thêm mới', type='primary', use_container_width=True)
        with col_submit2:
            st.form_submit_button('Huỷ', use_container_width=True)

        st.form_submit_button()

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
        background-color: {priority_colors.get(todo['priority'], '#f0f0f0')};
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid {'#ff6b6b' if todo['is_important'] else '#4ecdc4'};
        margin-bottom: 10px;
        {'opacity: 0.6;' if todo['completed'] else ''}
    ">
    """
    
    with st.container():
        col1, col2, col3, col4, col5 = st.columns([0.5, 4, 1, 1, 1])
        
        with col1:
            # Checkbox hoàn thành
            if st.checkbox("", value=todo['completed'], key=f"complete_{todo['id']}"):
                if not todo['completed']:
                    # toggle_complete(todo['id'])
                    st.rerun()
            elif todo['completed']:
                # toggle_complete(todo['id'])
                st.rerun()
        
        with col2:
            # Thông tin todo
            title_style = "text-decoration: line-through;" if todo['completed'] else ""
            importance_icon = "⭐ " if todo['is_important'] else ""
            
            st.markdown(f"**{importance_icon}{todo['title']}**", unsafe_allow_html=True)
            if todo['description']:
                st.write(todo['description'])
            
            # Thông tin chi tiết
            details = []
            if todo['due_date']:
                date_str = datetime.fromisoformat(todo['due_date']).strftime('%d/%m/%Y')
                time_str = f" {todo['due_time']}" if todo['due_time'] else ""
                details.append(f"📅 {date_str}{time_str}")
            
            if todo['location']:
                details.append(f"📍 {todo['location']}")
            
            details.append(f"🏷️ {todo['group']}")
            details.append(f"🔥 {todo['priority']}")
            
            if details:
                st.caption(" | ".join(details))
            
            # Hiển thị URL và hình ảnh
            if todo['url']:
                st.markdown(f"🔗 [Link]({todo['url']})")
            
            if todo['image_path'] and os.path.exists(todo['image_path']):
                try:
                    st.image(todo['image_path'], width=200)
                except:
                    st.caption("❌ Không thể hiển thị hình ảnh")
        
        with col3:
            # Nút sửa
            if st.button("✏️", key=f"edit_{todo['id']}", help="Sửa"):
                st.session_state.editing_todo = todo['id']
                st.rerun()
        
        with col4:
            # Nút xóa
            if st.button("🗑️", key=f"delete_{todo['id']}", help="Xóa"):
                # delete_todo(todo['id'])
                st.success("🗑️ Đã xóa công việc!")
                st.rerun()

def main():
    display_todo_form()
    for todo in load_todos():
        display_todo_card(todo)

main()