#!/bin/bash
# Script khởi chạy nhanh ứng dụng Streamlit Speech Recognition

echo "🎤 === CHƯƠNG TRÌNH NHẬN DIỆN ÂM THANH ==="
echo "🚀 Khởi động ứng dụng Streamlit..."
echo ""

# Sử dụng streamlit trực tiếp từ .venv (đã cài sẵn)
/Users/tungvu/Documents/Project/Python-Icantech/.venv/bin/streamlit run streamlit_app_fixed.py --server.port 8501 --server.headless true

echo ""
echo "✅ Ứng dụng đã dừng!"
