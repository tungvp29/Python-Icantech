# 🎤 HƯỚNG DẪN CHẠY NHANH

## ⚡ Cách chạy đúng:

### 1. Dùng script (Dễ nhất):
```bash
./start_app.sh
```

### 2. Dùng streamlit trực tiếp từ .venv:
```bash
/Users/tungvu/Documents/Project/Python-Icantech/.venv/bin/streamlit run streamlit_app_fixed.py
```

### 3. Hoặc dùng Python module:
```bash
/Users/tungvu/Documents/Project/Python-Icantech/.venv/bin/python -m streamlit run streamlit_app_fixed.py
```

## ❌ Lỗi thường gặp:

### "command not found: streamlit"
**Nguyên nhân:** Chạy `streamlit` trực tiếp thay vì qua Python environment

**Giải pháp:** Sử dụng một trong 2 cách trên ⬆️

## 🔧 Troubleshooting:

### Nếu script không chạy được:
```bash
# Cấp quyền thực thi
chmod +x start_app.sh

# Chạy lại
./start_app.sh
```

### Nếu vẫn lỗi:
```bash
# Chạy với streamlit trực tiếp
/Users/tungvu/Documents/Project/Python-Icantech/.venv/bin/streamlit run streamlit_app_fixed.py

# Hoặc chạy với Python module
/Users/tungvu/Documents/Project/Python-Icantech/.venv/bin/python -m streamlit run streamlit_app_fixed.py
```

## 📱 Sau khi chạy thành công:
- Ứng dụng mở tại: **http://localhost:8501**
- Nhấn **Ctrl+C** để dừng
- Nếu browser không tự mở, copy link vào trình duyệt
