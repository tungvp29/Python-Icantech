# Chương trình Nhận diện Âm thanh

Chương trình Python sử dụng thư viện `speechRecognition` và `pyttsx3` để nhận diện và chuyển đổi âm thanh.

## Tính năng

### 1. Chuyển văn bản thành âm thanh (Text-to-Speech)
- Tham số: Văn bản tiếng Việt
- Chức năng: Chuyển văn bản thành giọng nói người đọc
- Hỗ trợ điều chỉnh tốc độ đọc và âm lượng

### 2. Nhận diện âm thanh thành văn bản (Speech-to-Text)
- Lắng nghe người nói qua microphone
- Chuyển đổi giọng nói thành văn bản
- Hiển thị nội dung đã nói ra màn hình
- Dừng lắng nghe khi nói từ "stop" hoặc "dừng"

## Cài đặt

### Thư viện cần thiết:
```bash
pip install speechrecognition pyttsx3 pyaudio
```

### Lưu ý cho macOS:
Có thể cần cài đặt thêm:
```bash
brew install portaudio
```

## Cách sử dụng

### 1. Chạy chương trình chính:
```bash
python example.py
```

### 2. Chạy demo tương tác:
```bash
python demo.py
```

### 3. Sử dụng trong code:

```python
from example import SpeechRecognitionSystem

# Khởi tạo hệ thống
speech_system = SpeechRecognitionSystem()

# Chuyển văn bản thành âm thanh
speech_system.text_to_speech("Xin chào các bạn!")

# Nhận diện âm thanh thành văn bản
result = speech_system.speech_to_text()
print(f"Bạn đã nói: {result}")

# Chế độ trò chuyện liên tục
speech_system.continuous_speech_recognition()
```

## Cấu trúc Class

### `SpeechRecognitionSystem`

#### Phương thức chính:
- `__init__()`: Khởi tạo hệ thống
- `text_to_speech(text)`: Chuyển văn bản thành âm thanh
- `speech_to_text()`: Nhận diện âm thanh thành văn bản
- `continuous_speech_recognition()`: Chế độ nhận diện liên tục

#### Phương thức hỗ trợ:
- `setup_tts_engine()`: Cấu hình engine text-to-speech
- `adjust_for_ambient_noise()`: Điều chỉnh microphone

## Lưu ý khi sử dụng

1. **Microphone**: Đảm bảo microphone hoạt động tốt
2. **Kết nối internet**: Cần kết nối internet cho Google Speech Recognition
3. **Tiếng ồn**: Sử dụng trong môi trường ít tiếng ồn
4. **Từ khóa dừng**: Nói "stop", "dừng", "kết thúc", hoặc "tạm biệt" để dừng
5. **Ngôn ngữ**: Chương trình được tối ưu cho tiếng Việt

## Xử lý lỗi

Chương trình xử lý các lỗi phổ biến:
- Timeout khi không nghe thấy âm thanh
- Lỗi kết nối internet
- Lỗi nhận diện âm thanh
- Lỗi microphone

## Demo

Chạy `demo.py` để trải nghiệm menu tương tác với các tùy chọn:
1. Test chuyển văn bản thành âm thanh
2. Test nhận diện âm thanh thành văn bản  
3. Chế độ trò chuyện liên tục
4. Thoát chương trình
