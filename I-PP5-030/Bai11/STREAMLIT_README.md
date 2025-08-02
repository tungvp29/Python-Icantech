# 🎤 Ứng dụng Nhận diện Âm thanh - Streamlit

Ứng dụng web tương tác cho chương trình nhận diện âm thanh sử dụng Streamlit.

## 🚀 Cách chạy ứng dụng

### 1. Cài đặt dependencies (đã hoàn thành)
```bash
pip install -r requirements.txt
```

### 2. Chạy ứng dụng Streamlit

#### ✅ **Cách 1: Dùng script (Khuyến nghị)**
```bash
./start_app.sh
```

#### ✅ **Cách 2: Chạy với Python environment**
```bash
/Users/tungvu/Documents/Project/Python-Icantech/.venv/bin/python -m streamlit run streamlit_app_fixed.py
```

#### ❌ **KHÔNG chạy trực tiếp:**
```bash
streamlit run streamlit_app.py  # Sai - sẽ báo lỗi command not found
```

### 3. Mở trình duyệt
Ứng dụng sẽ tự động mở tại: `http://localhost:8501`

## 🎯 Tính năng của ứng dụng

### 📱 **Giao diện chính**
- **4 tabs chính:** Text to Speech, Speech to Text, Trò chuyện, Lịch sử
- **Sidebar cài đặt:** Điều chỉnh tốc độ đọc và âm lượng
- **Responsive design:** Tương thích mọi thiết bị

### 🔊 **Tab 1: Text to Speech**
- Nhập văn bản tiếng Việt
- Văn bản mẫu có sẵn
- Điều chỉnh tốc độ đọc và âm lượng
- Phản hồi trực quan

### 🎤 **Tab 2: Speech to Text**
- Nhận diện giọng nói real-time
- Hiển thị kết quả ngay lập tức
- Tự động dừng khi nói "stop"
- Xử lý lỗi thông minh

### 💬 **Tab 3: Trò chuyện liên tục**
- Chế độ AI Assistant
- Lắng nghe và phản hồi liên tục
- Ghi lại toàn bộ cuộc trò chuyện
- Hiển thị chat real-time

### 📊 **Tab 4: Lịch sử**
- Xem toàn bộ lịch sử tương tác
- Bộ lọc theo loại hoạt động
- Xuất lịch sử ra file
- Quản lý dữ liệu

## ⚙️ **Sidebar - Cài đặt**

### 🔊 **Text-to-Speech Settings**
- **Tốc độ đọc:** 50-300 từ/phút
- **Âm lượng:** 0.0-1.0
- Áp dụng cài đặt real-time

### ℹ️ **Thông tin & Hướng dẫn**
- Hướng dẫn sử dụng từng tab
- Lưu ý quan trọng
- Tips sử dụng hiệu quả

## 🎨 **Giao diện & UX**

### **Màu sắc chủ đạo**
- Primary: #1E88E5 (Blue)
- Background: #FFFFFF (White)
- Secondary: #F0F2F6 (Light Gray)

### **Các component đặc biệt**
- **Success Box:** Thông báo thành công (xanh lá)
- **Error Box:** Thông báo lỗi (đỏ)
- **Info Box:** Thông tin (xanh dương)
- **Feature Box:** Khung tính năng (xám nhạt)

### **Icons & Emoji**
- 🎤 Microphone
- 🔊 Speaker
- 💬 Chat
- 📊 Statistics
- ⚙️ Settings
- 🤖 AI Assistant

## 🔧 **Tính năng kỹ thuật**

### **Session State Management**
- Lưu trữ hệ thống speech recognition
- Quản lý lịch sử trò chuyện
- Trạng thái lắng nghe real-time

### **Real-time Processing**
- Nhận diện âm thanh không lag
- Cập nhật giao diện tức thì
- Xử lý bất đồng bộ

### **Error Handling**
- Timeout handling
- Microphone errors
- Network connection issues
- User-friendly error messages

## 📱 **Responsive Design**

### **Desktop** (>1200px)
- Layout 2 cột cho các tính năng
- Sidebar mở rộng
- Hiển thị đầy đủ thông tin

### **Tablet** (768px - 1200px)
- Layout 1 cột
- Sidebar thu gọn
- Tối ưu cho touch

### **Mobile** (<768px)
- Stack layout
- Buttons lớn hơn
- Text size tăng

## 🚀 **Performance Tips**

1. **Microphone Quality:** Sử dụng mic chất lượng tốt
2. **Internet:** Cần kết nối ổn định cho Google Speech API
3. **Environment:** Môi trường ít tiếng ồn
4. **Browser:** Chrome/Firefox hiệu suất tốt nhất

## 🐛 **Troubleshooting**

### **Lỗi thường gặp:**

1. **Microphone không hoạt động**
   - Kiểm tra permissions trong browser
   - Restart ứng dụng
   - Kiểm tra mic hardware

2. **Không nhận diện được giọng nói**
   - Kiểm tra kết nối internet
   - Nói rõ ràng, không quá nhanh
   - Thử lại với môi trường ít tiếng ồn

3. **TTS không hoạt động**
   - Kiểm tra âm lượng hệ thống
   - Restart ứng dụng
   - Thử điều chỉnh settings

## 📚 **Documentation**

- `streamlit_app.py` - Main application file
- `example.py` - Core speech recognition system
- `demo.py` - CLI demo version
- `.streamlit/config.toml` - Streamlit configuration

## 🎯 **Future Enhancements**

- [ ] Hỗ trợ nhiều ngôn ngữ
- [ ] Voice authentication
- [ ] Real-time translation
- [ ] Audio file upload/download
- [ ] Cloud storage integration
- [ ] Mobile app version
