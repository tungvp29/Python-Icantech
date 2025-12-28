import speech_recognition as sr
import pyttsx3
import time

class SpeechRecognitionSystem:
    def __init__(self):
        """Khởi tạo hệ thống nhận diện âm thanh"""
        # Khởi tạo speech recognition
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        
        # Khởi tạo text-to-speech engine
        self.tts_engine = pyttsx3.init()
        self.setup_tts_engine()
        
        # Điều chỉnh cho tiếng ồn môi trường
        self.adjust_for_ambient_noise()
    
    def setup_tts_engine(self):
        """Cấu hình engine text-to-speech với hỗ trợ tiếng Việt tốt hơn"""
        # Thiết lập tốc độ đọc chậm hơn cho tiếng Việt
        self.tts_engine.setProperty('rate', 120)
        
        # Thiết lập âm lượng
        self.tts_engine.setProperty('volume', 1.0)
        
        # Lấy danh sách giọng nói có sẵn
        voices = self.tts_engine.getProperty('voices')
        
        # Ưu tiên tìm giọng nói tiếng Việt (Linh)
        vietnamese_voice = None
        for voice in voices:
            if 'vi-VN' in voice.id or 'Linh' in voice.name:
                vietnamese_voice = voice
                break
        
        if vietnamese_voice:
            self.tts_engine.setProperty('voice', vietnamese_voice.id)
            print(f"✅ Đã thiết lập giọng nói tiếng Việt: {vietnamese_voice.name}")
        else:
            # Thử tìm giọng nói khác phù hợp
            for voice in voices:
                if any(lang in ['en_US', 'en_GB'] for lang in getattr(voice, 'languages', [])):
                    self.tts_engine.setProperty('voice', voice.id)
                    break
            print("⚠️ Không tìm thấy giọng nói tiếng Việt, sử dụng giọng tiếng Anh")
    
    def adjust_for_ambient_noise(self):
        """Điều chỉnh microphone cho tiếng ồn môi trường"""
        print("Đang điều chỉnh microphone cho tiếng ồn môi trường...")
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=2)
        print("Hoàn thành điều chỉnh microphone.")
    
    def text_to_speech(self, text):
        """
        Hàm chuyển văn bản thành âm thanh với cải thiện cho tiếng Việt
        
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
            'JavaScript': 'Java Script',
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
            'OK': 'ô kê',
            'email': 'i-meo',
        }
        
        processed_text = text
        for old, new in replacements.items():
            processed_text = processed_text.replace(old, new)
        
        # Thêm dấu câu để tạo nghỉ tự nhiên
        if not processed_text.endswith(('.', '!', '?')):
            processed_text += '.'
        
        return processed_text
    
    def speech_to_text(self):
        """
        Hàm nhận diện và chuyển âm thanh thành văn bản
        Lắng nghe người nói và chuyển thành văn bản
        Dừng lắng nghe khi nghe từ "stop"
        
        Returns:
            str: Văn bản được nhận diện từ âm thanh
        """
        print("Bắt đầu lắng nghe... (Nói 'stop' để dừng)")
        
        while True:
            try:
                # Lắng nghe âm thanh từ microphone
                with self.microphone as source:
                    print("Đang lắng nghe...")
                    # Timeout sau 5 giây nếu không có âm thanh
                    audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
                
                print("Đang xử lý âm thanh...")
                
                # Nhận diện âm thanh thành văn bản (sử dụng Google Speech Recognition)
                text = self.recognizer.recognize_google(audio, language='vi-VN')
                
                print(f"Bạn đã nói: {text}")
                
                # Kiểm tra từ khóa "stop" để dừng
                if "stop" in text.lower() or "dừng" in text.lower():
                    print("Đã nghe từ khóa dừng. Kết thúc lắng nghe.")
                    self.text_to_speech("Đã dừng lắng nghe.")
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
    
    def continuous_speech_recognition(self):
        """
        Hàm nhận diện âm thanh liên tục
        Lắng nghe và in ra màn hình mọi câu nói cho đến khi nghe "stop"
        """
        print("Bắt đầu nhận diện âm thanh liên tục...")
        print("Nói 'stop' hoặc 'dừng' để kết thúc chương trình.")
        
        self.text_to_speech("Chào bạn! Tôi đang lắng nghe bạn nói. Hãy nói stop để dừng.")
        
        conversation_log = []
        
        while True:
            try:
                with self.microphone as source:
                    print("\n--- Đang lắng nghe ---")
                    audio = self.recognizer.listen(source, timeout=10, phrase_time_limit=15)
                
                print("Đang xử lý...")
                
                # Nhận diện với tiếng Việt
                text = self.recognizer.recognize_google(audio, language='vi-VN')
                
                print(f"✓ Bạn nói: {text}")
                conversation_log.append(text)
                
                # Kiểm tra điều kiện dừng
                if any(word in text.lower() for word in ["stop", "dừng", "kết thúc", "tạm biệt"]):
                    print("\n=== KẾT THÚC CHƯƠNG TRÌNH ===")
                    self.text_to_speech("Tạm biệt! Cảm ơn bạn đã sử dụng chương trình.")
                    break
                
                # Phản hồi lại người dùng
                response = f"Tôi đã nghe bạn nói: {text}"
                self.text_to_speech(response)
                
            except sr.WaitTimeoutError:
                print("⏰ Timeout - Không nghe thấy âm thanh")
                continue
            except sr.UnknownValueError:
                print("❌ Không thể nhận diện âm thanh")
                self.text_to_speech("Xin lỗi, tôi không nghe rõ. Bạn có thể nói lại không?")
            except sr.RequestError as e:
                print(f"❌ Lỗi dịch vụ: {e}")
                break
            except KeyboardInterrupt:
                print("\n⏹️ Đã dừng bằng Ctrl+C")
                break
            except Exception as e:
                print(f"❌ Lỗi: {e}")
        
        # In log cuộc trò chuyện
        if conversation_log:
            print("\n=== LOG CUỘC TRÒ CHUYỆN ===")
            for i, sentence in enumerate(conversation_log, 1):
                print(f"{i}. {sentence}")


def demo_basic_functions():
    """Demo các chức năng cơ bản"""
    print("=== DEMO CHƯƠNG TRÌNH NHẬN DIỆN ÂM THANH ===\n")
    
    # Khởi tạo hệ thống
    speech_system = SpeechRecognitionSystem()
    
    # Demo chức năng text to speech
    print("1. Demo chuyển văn bản thành âm thanh:")
    sample_texts = [
        "Xin chào! Đây là chương trình nhận diện âm thanh.",
        "Chương trình có thể chuyển văn bản thành giọng nói.",
        "Và cũng có thể nhận diện giọng nói thành văn bản."
    ]
    
    for text in sample_texts:
        speech_system.text_to_speech(text)
        time.sleep(1)
    
    print("\n2. Demo nhận diện âm thanh:")
    print("Bạn có muốn thử nhận diện âm thanh không? (y/n)")
    
    try:
        choice = input().lower()
        if choice == 'y' or choice == 'yes':
            speech_system.continuous_speech_recognition()
        else:
            print("Cảm ơn bạn đã sử dụng chương trình!")
    except KeyboardInterrupt:
        print("\nTạm biệt!")


def main():
    """Hàm main của chương trình"""
    try:
        demo_basic_functions()
    except Exception as e:
        print(f"Lỗi trong chương trình chính: {e}")


if __name__ == "__main__":
    main()
