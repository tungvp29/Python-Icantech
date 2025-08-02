#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Demo đơn giản các chức năng nhận diện âm thanh
"""

from example import SpeechRecognitionSystem

def test_text_to_speech():
    """Test chức năng chuyển văn bản thành âm thanh"""
    print("=== TEST CHUYỂN VĂN BẢN THÀNH ÂM THANH ===")
    
    speech_system = SpeechRecognitionSystem()
    
    test_sentences = [
        "Xin chào các bạn!",
        "Hôm nay là một ngày đẹp trời.",
        "Chương trình Python có thể nhận diện giọng nói.",
        "Cảm ơn bạn đã sử dụng chương trình này."
    ]
    
    for sentence in test_sentences:
        print(f"Đọc: {sentence}")
        speech_system.text_to_speech(sentence)
        input("Nhấn Enter để tiếp tục...")

def test_speech_to_text():
    """Test chức năng nhận diện âm thanh thành văn bản"""
    print("=== TEST NHẬN DIỆN ÂM THANH THÀNH VĂN BẢN ===")
    
    speech_system = SpeechRecognitionSystem()
    
    print("Hướng dẫn:")
    print("- Nói một câu bất kỳ")
    print("- Nói 'stop' để dừng")
    print("- Nhấn Ctrl+C để thoát khẩn cấp")
    
    speech_system.text_to_speech("Xin chào! Hãy nói một câu gì đó. Nói stop để dừng.")
    
    result = speech_system.speech_to_text()
    if result:
        print(f"Kết quả cuối cùng: {result}")

def interactive_menu():
    """Menu tương tác cho người dùng"""
    speech_system = SpeechRecognitionSystem()
    
    while True:
        print("\n" + "="*50)
        print("CHƯƠNG TRÌNH NHẬN DIỆN ÂM THANH")
        print("="*50)
        print("1. Test chuyển văn bản thành âm thanh")
        print("2. Test nhận diện âm thanh thành văn bản")
        print("3. Chế độ trò chuyện liên tục")
        print("4. Thoát")
        print("="*50)
        
        choice = input("Chọn chức năng (1-4): ").strip()
        
        if choice == '1':
            test_text_to_speech()
        elif choice == '2':
            test_speech_to_text()
        elif choice == '3':
            speech_system.continuous_speech_recognition()
        elif choice == '4':
            speech_system.text_to_speech("Tạm biệt! Cảm ơn bạn đã sử dụng chương trình.")
            print("Đã thoát chương trình!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1-4.")

if __name__ == "__main__":
    try:
        interactive_menu()
    except KeyboardInterrupt:
        print("\n\nĐã dừng chương trình bằng Ctrl+C")
    except Exception as e:
        print(f"Lỗi: {e}")
