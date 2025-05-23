import streamlit as st
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Hàm gửi dữ liệu đến Google Sheet
def send_to_google_sheet(data_dict):
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive"
    ] 
    creds_dict = json.loads(st.secrets["GOOGLE_SHEET_CREDS"])

    # creds = ServiceAccountCredentials.from_json_keyfile_name(
    #     "ggsheet-fruit-78a2d075dde0.json", scope
    # )
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
    client = gspread.authorize(creds)

    # Mở file Google Sheet (đảm bảo file này tồn tại và được chia sẻ quyền edit)
    # sheet = client.open("DatSinhTo").worksheet("sheet1")  # <--- Thay tên file tại đây nếu khác
    sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1ZjRzms5XhLUyCuPE_x3SSQ6y7CgWoT0TZmWPJBTZ0Lc/edit?gid=568338065#gid=568338065").worksheet("sheet1")
    sheet.append_row(list(data_dict.values()))

# Giao diện Streamlit
st.set_page_config(page_title='Vương quốc mô hình', page_icon=':sparkles:')
st.title('Đặt hàng mô hình')

with st.form("form_dat_hang"):
    chu_de = st.selectbox("Chủ đề mô hình", ['Dragon Ball', 'Naruto', 'One Piece'])
    ma_so = st.selectbox("Mã số mô hình", ['001', '002', '003'])
    so_luong = st.slider("Số lượng", 1, 10, 1)
    ho_ten = st.text_input("Họ và tên")
    sdt = st.text_input("Số điện thoại")
    dia_chi = st.text_input("Địa chỉ giao hàng")
    
    submitted = st.form_submit_button("Xác nhận")

    if submitted:
        du_lieu = {
            "Chủ đề": chu_de,
            "Mã số": ma_so,
            "Số lượng": so_luong,
            "Họ tên": ho_ten,
            "SĐT": sdt,
            "Địa chỉ": dia_chi
        }

        send_to_google_sheet(du_lieu)
        st.success("Thông tin đã được gửi lên Google Sheet!")
