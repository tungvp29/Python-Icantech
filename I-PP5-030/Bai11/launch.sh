#!/bin/bash
# Script đơn giản sử dụng .venv có sẵn

echo "🎤 Khởi động ứng dụng Nhận diện Âm thanh..."
echo "🔗 Sử dụng .venv tại: /Users/tungvu/Documents/Project/Python-Icantech/.venv"
echo "🌐 Ứng dụng sẽ mở tại: http://localhost:8501"
echo ""

# Chạy trực tiếp bằng streamlit từ .venv
/Users/tungvu/Documents/Project/Python-Icantech/.venv/bin/streamlit run streamlit_app_fixed.py
