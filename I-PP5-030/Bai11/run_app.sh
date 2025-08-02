#!/bin/bash
# Script khởi chạy ứng dụng Streamlit Speech Recognition

echo "🎤 Khởi động ứng dụng Nhận diện Âm thanh..."
echo "=================================================="

# Kiểm tra Python environment
echo "📍 Kiểm tra Python environment..."
/Users/tungvu/Documents/Project/Python-Icantech/.venv/bin/python --version

# Kiểm tra các thư viện cần thiết
echo "📦 Kiểm tra dependencies..."
/Users/tungvu/Documents/Project/Python-Icantech/.venv/bin/python -c "
import speech_recognition as sr
import pyttsx3
import streamlit as st
print('✅ Tất cả thư viện đã sẵn sàng!')
"

echo "🚀 Khởi động Streamlit..."
echo "📱 Ứng dụng sẽ mở tại: http://localhost:8501"
echo "⏹️  Nhấn Ctrl+C để dừng"
echo "=================================================="

# Chạy ứng dụng Streamlit (sử dụng .venv)
echo "� Sử dụng môi trường .venv đã có sẵn..."
/Users/tungvu/Documents/Project/Python-Icantech/.venv/bin/streamlit run streamlit_app_fixed.py
