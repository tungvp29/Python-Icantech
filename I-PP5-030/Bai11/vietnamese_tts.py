#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Phiên bản cải thiện của SpeechRecognitionSystem với TTS tiếng Việt tốt hơn
"""

import speech_recognition as sr
import pyttsx3
import time

class ImprovedSpeechRecognitionSystem:
    def __init__(self):
        """Khởi tạo hệ thống nhận diện âm thanh với TTS tiếng Việt"""
        # Khởi tạo speech recognition
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        
        # Khởi tạo text-to-speech engine
        self.tts_engine = pyttsx3.init()
        self.setup_vietnamese_tts()
        
        # Điều chỉnh cho tiếng ồn môi trường
        self.adjust_for_ambient_noise()
    
    def setup_vietnamese_tts(self):
        """Cấu hình TTS cho tiếng Việt"""
        # Tìm và thiết lập giọng nói tiếng Việt
        voices = self.tts_engine.getProperty('voices')
        vietnamese_voice = None
        
        # Tìm giọng nói tiếng Việt (Linh)
        for voice in voices:
            if 'vi-VN' in voice.id or 'Linh' in voice.name:
                vietnamese_voice = voice
                break
        
        if vietnamese_voice:
            self.tts_engine.setProperty('voice', vietnamese_voice.id)
            print(f"✅ Đã thiết lập giọng nói tiếng Việt: {vietnamese_voice.name}")
        else:
            print("⚠️ Không tìm thấy giọng nói tiếng Việt, sử dụng giọng mặc định")
            # Sử dụng giọng nói đầu tiên có sẵn
            if voices:
                self.tts_engine.setProperty('voice', voices[0].id)
        
        # Thiết lập tốc độ đọc chậm hơn cho tiếng Việt
        self.tts_engine.setProperty('rate', 120)  # Chậm hơn để phát âm rõ ràng
        
        # Thiết lập âm lượng
        self.tts_engine.setProperty('volume', 1.0)
    
    def get_available_vietnamese_voices(self):
        """Lấy danh sách giọng nói tiếng Việt có sẵn"""
        voices = self.tts_engine.getProperty('voices')
        vietnamese_voices = []
        
        for voice in voices:
            # Tìm giọng nói có thể phù hợp với tiếng Việt
            if any(keyword in voice.id.lower() or keyword in voice.name.lower() 
                   for keyword in ['vi-vn', 'vietnam', 'linh']):
                vietnamese_voices.append({
                    'id': voice.id,
                    'name': voice.name,
                    'languages': getattr(voice, 'languages', ['N/A'])
                })
        
        return vietnamese_voices
    
    def adjust_for_ambient_noise(self):
        """Điều chỉnh microphone cho tiếng ồn môi trường"""
        print("Đang điều chỉnh microphone cho tiếng ồn môi trường...")
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=2)
        print("Hoàn thành điều chỉnh microphone.")
    
    def text_to_speech_vietnamese(self, text):
        """
        Hàm chuyển văn bản tiếng Việt thành âm thanh với cải thiện
        
        Args:
            text (str): Văn bản tiếng Việt cần chuyển thành giọng nói
        """
        try:
            # Tiền xử lý văn bản tiếng Việt
            processed_text = self.preprocess_vietnamese_text(text)
            
            print(f"Đang đọc: {processed_text}")
            self.tts_engine.say(processed_text)
            self.tts_engine.runAndWait()
            
        except Exception as e:
            print(f"Lỗi khi chuyển văn bản thành âm thanh: {e}")
            # Fallback: thử với văn bản gốc
            try:
                self.tts_engine.say(text)
                self.tts_engine.runAndWait()
            except:
                print("Không thể đọc văn bản")
    
    def preprocess_vietnamese_text(self, text):
        """
        Tiền xử lý văn bản tiếng Việt để cải thiện phát âm
        """
        # Thay thế một số từ khó phát âm
        replacements = {
            'AI': 'Ây Ai',
            'API': 'Ây Pi Ây',
            'URL': 'Iu Ạt En',
            'HTML': 'Éc Ti Em En',
            'CSS': 'Xi Es Es',
            'JS': 'Giây Es',
            'Python': 'Pai thon',
            'GitHub': 'Gít Háp',
            'Streamlit': 'Strim lít',
            'TTS': 'Ti Ti Es',
            'STT': 'Es Ti Ti',
            'vs': 'với',
            '&': 'và',
            '%': 'phần trăm',
            '@': 'a còng',
            '#': 'thăng',
            '$': 'đô la',
        }
        
        processed_text = text
        for old, new in replacements.items():
            processed_text = processed_text.replace(old, new)
        
        # Thêm dấu câu để tạo nghỉ tự nhiên
        if not processed_text.endswith(('.', '!', '?')):
            processed_text += '.'
        
        return processed_text
    
    def test_vietnamese_voices(self, test_text="Xin chào, tôi đang test giọng nói tiếng Việt"):
        """Test các giọng nói tiếng Việt có sẵn"""
        voices = self.get_available_vietnamese_voices()
        
        if not voices:
            print("❌ Không tìm thấy giọng nói tiếng Việt")
            return
        
        print(f"🎤 Test {len(voices)} giọng nói tiếng Việt:")
        
        for i, voice in enumerate(voices, 1):
            print(f"\n{i}. Test giọng: {voice['name']}")
            try:
                self.tts_engine.setProperty('voice', voice['id'])
                self.tts_engine.say(test_text)
                self.tts_engine.runAndWait()
                time.sleep(1)
            except Exception as e:
                print(f"   ❌ Lỗi: {e}")
    
    def set_voice_by_name(self, voice_name):
        """Thiết lập giọng nói theo tên"""
        voices = self.tts_engine.getProperty('voices')
        
        for voice in voices:
            if voice_name.lower() in voice.name.lower():
                self.tts_engine.setProperty('voice', voice.id)
                print(f"✅ Đã chuyển sang giọng: {voice.name}")
                return True
        
        print(f"❌ Không tìm thấy giọng nói: {voice_name}")
        return False
    
    def speech_to_text(self):
        """
        Hàm nhận diện và chuyển âm thanh thành văn bản (giữ nguyên)
        """
        print("Bắt đầu lắng nghe... (Nói 'stop' để dừng)")
        
        while True:
            try:
                with self.microphone as source:
                    print("Đang lắng nghe...")
                    audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
                
                print("Đang xử lý âm thanh...")
                text = self.recognizer.recognize_google(audio, language='vi-VN')
                
                print(f"Bạn đã nói: {text}")
                
                if "stop" in text.lower() or "dừng" in text.lower():
                    print("Đã nghe từ khóa dừng. Kết thúc lắng nghe.")
                    self.text_to_speech_vietnamese("Đã dừng lắng nghe.")
                    break
                
                return text
                
            except sr.WaitTimeoutError:
                print("Không nghe thấy âm thanh nào trong 5 giây.")
            except sr.UnknownValueError:
                print("Không thể nhận diện được âm thanh. Vui lòng nói rõ hơn.")
            except sr.RequestError as e:
                print(f"Lỗi kết nối đến dịch vụ nhận diện: {e}")
            except KeyboardInterrupt:
                print("\nĐã dừng chương trình.")
                break
            except Exception as e:
                print(f"Lỗi không xác định: {e}")


def demo_vietnamese_tts():
    """Demo chức năng TTS tiếng Việt cải thiện"""
    print("=== DEMO TEXT-TO-SPEECH TIẾNG VIỆT CẢI THIỆN ===\n")
    
    # Khởi tạo hệ thống
    speech_system = ImprovedSpeechRecognitionSystem()
    
    # Hiển thị giọng nói tiếng Việt có sẵn
    vietnamese_voices = speech_system.get_available_vietnamese_voices()
    if vietnamese_voices:
        print("🎤 Giọng nói tiếng Việt có sẵn:")
        for voice in vietnamese_voices:
            print(f"  - {voice['name']} ({voice['id']})")
    
    # Test các câu tiếng Việt
    test_sentences = [
        "Xin chào các bạn! Tôi là trợ lý AI.",
        "Hôm nay là một ngày đẹp trời ở Việt Nam.",
        "Chương trình Python có thể nhận diện giọng nói tiếng Việt.",
        "Tôi có thể đọc các từ khó như: GitHub, Streamlit, API, HTML, CSS.",
        "Cảm ơn bạn đã sử dụng chương trình nhận diện âm thanh!"
    ]
    
    print(f"\n🗣️ Đang đọc {len(test_sentences)} câu test:")
    for i, sentence in enumerate(test_sentences, 1):
        print(f"\n{i}. {sentence}")
        speech_system.text_to_speech_vietnamese(sentence)
        time.sleep(1)


if __name__ == "__main__":
    demo_vietnamese_tts()
