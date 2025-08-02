#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Phiên bản cải thiện của ứng dụng Streamlit với xử lý lỗi tốt hơn
"""

import streamlit as st
import sys
import os

# Kiểm tra và xử lý lỗi import
def check_dependencies():
    """Kiểm tra và hiển thị trạng thái các thư viện"""
    missing_deps = []
    dep_status = {}
    
    try:
        import speech_recognition as sr
        dep_status['speechrecognition'] = f"✅ v{getattr(sr, '__version__', 'OK')}"
    except ImportError as e:
        missing_deps.append('speechrecognition')
        dep_status['speechrecognition'] = f"❌ Lỗi: {e}"
    
    try:
        import pyttsx3
        dep_status['pyttsx3'] = "✅ OK"
    except ImportError as e:
        missing_deps.append('pyttsx3')
        dep_status['pyttsx3'] = f"❌ Lỗi: {e}"
    
    try:
        import pyaudio
        dep_status['pyaudio'] = "✅ OK"
    except ImportError as e:
        missing_deps.append('pyaudio')
        dep_status['pyaudio'] = f"❌ Lỗi: {e}"
    
    return missing_deps, dep_status

def show_installation_guide():
    """Hiển thị hướng dẫn cài đặt"""
    st.error("⚠️ Một số thư viện chưa được cài đặt đúng cách!")
    
    st.markdown("""
    ## 🔧 Hướng dẫn khắc phục lỗi PyAudio trên macOS:
    
    ### Bước 1: Cài đặt PortAudio
    ```bash
    brew install portaudio
    ```
    
    ### Bước 2: Cài đặt PyAudio
    ```bash
    pip install pyaudio
    ```
    
    ### Bước 3: Cài đặt các thư viện khác
    ```bash
    pip install speechrecognition pyttsx3 streamlit
    ```
    
    ### Lưu ý khác:
    - Trên Ubuntu/Debian: `sudo apt-get install portaudio19-dev python3-pyaudio`
    - Trên Windows: `pip install pyaudio` (thường hoạt động trực tiếp)
    
    ### Nếu vẫn gặp lỗi:
    1. Khởi động lại terminal
    2. Kích hoạt lại virtual environment
    3. Chạy lại lệnh cài đặt
    """)

# Kiểm tra dependencies trước khi chạy app chính
missing_deps, dep_status = check_dependencies()

# Cấu hình trang
st.set_page_config(
    page_title="🎤 Nhận diện Âm thanh - Fixed",
    page_icon="🎤",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1E88E5;
        text-align: center;
        margin-bottom: 2rem;
    }
    .status-box {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #1E88E5;
        margin: 1rem 0;
    }
    .success-text { color: #28a745; }
    .error-text { color: #dc3545; }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">🎤 Chương trình Nhận diện Âm thanh</h1>', unsafe_allow_html=True)

# Hiển thị trạng thái dependencies
with st.expander("📋 Kiểm tra Dependencies", expanded=bool(missing_deps)):
    st.markdown("### Trạng thái thư viện:")
    for dep, status in dep_status.items():
        st.markdown(f"- **{dep}:** {status}")

# Nếu có lỗi dependencies
if missing_deps:
    show_installation_guide()
    st.stop()

# Import các module chính sau khi đã kiểm tra
try:
    from vietnamese_tts import ImprovedSpeechRecognitionSystem
    import speech_recognition as sr
    import pyttsx3
    import threading
    import time
    from io import StringIO
    
    # Sử dụng phiên bản cải thiện
    SPEECH_SYSTEM_CLASS = ImprovedSpeechRecognitionSystem
    
except ImportError:
    try:
        from example import SpeechRecognitionSystem
        import speech_recognition as sr
        import pyttsx3
        import threading
        import time
        from io import StringIO
        
        # Fallback về phiên bản gốc
        SPEECH_SYSTEM_CLASS = SpeechRecognitionSystem
        st.info("💡 Đang sử dụng TTS phiên bản gốc. Để có TTS tiếng Việt tốt hơn, hãy chạy `python vietnamese_tts.py`")
        
    except ImportError as e:
        st.error(f"Lỗi import: {e}")
        st.stop()

# Khởi tạo session state với error handling
if 'speech_system' not in st.session_state:
    try:
        with st.spinner("Đang khởi tạo hệ thống nhận diện âm thanh với TTS tiếng Việt..."):
            st.session_state.speech_system = SPEECH_SYSTEM_CLASS()
        
        # Hiển thị thông tin về TTS
        if hasattr(st.session_state.speech_system, 'get_available_vietnamese_voices'):
            vietnamese_voices = st.session_state.speech_system.get_available_vietnamese_voices()
            if vietnamese_voices:
                st.success(f"✅ Hệ thống đã sẵn sàng với TTS tiếng Việt! Giọng nói: {vietnamese_voices[0]['name']}")
            else:
                st.success("✅ Hệ thống đã sẵn sàng với TTS tiếng Anh!")
        else:
            st.success("✅ Hệ thống đã sẵn sàng!")
            
    except Exception as e:
        st.error(f"❌ Lỗi khởi tạo hệ thống: {e}")
        
        # Hướng dẫn khắc phục cụ thể
        if "PyAudio" in str(e) or "pyaudio" in str(e):
            st.markdown("""
            ### 🔧 Khắc phục lỗi PyAudio:
            ```bash
            # macOS
            brew install portaudio
            pip install pyaudio
            
            # Ubuntu/Debian  
            sudo apt-get install portaudio19-dev python3-pyaudio
            pip install pyaudio
            ```
            """)
        elif "microphone" in str(e).lower():
            st.markdown("""
            ### 🎤 Kiểm tra Microphone:
            - Đảm bảo microphone được kết nối
            - Cấp quyền truy cập microphone cho trình duyệt
            - Thử khởi động lại ứng dụng
            """)
        
        st.stop()

if 'conversation_log' not in st.session_state:
    st.session_state.conversation_log = []

if 'is_listening' not in st.session_state:
    st.session_state.is_listening = False

# Sidebar
with st.sidebar:
    st.header("⚙️ Cài đặt")
    
    # System info
    st.markdown("### 💻 Thông tin hệ thống")
    st.markdown(f"""
    - **OS:** {sys.platform}
    - **Python:** {sys.version.split()[0]}
    - **Streamlit:** {st.__version__}
    """)
    
    # Microphone test
    st.markdown("### 🎤 Test Microphone")
    if st.button("Test Mic"):
        try:
            recognizer = sr.Recognizer()
            microphone = sr.Microphone()
            st.success("✅ Microphone OK!")
        except Exception as e:
            st.error(f"❌ Lỗi Mic: {e}")
    
    # TTS Settings
    st.subheader("🔊 Text-to-Speech")
    tts_rate = st.slider("Tốc độ đọc", 50, 300, 150)
    tts_volume = st.slider("Âm lượng", 0.0, 1.0, 0.9, 0.1)
    
    if st.button("Áp dụng cài đặt TTS"):
        try:
            st.session_state.speech_system.tts_engine.setProperty('rate', tts_rate)
            st.session_state.speech_system.tts_engine.setProperty('volume', tts_volume)
            st.success("Đã cập nhật cài đặt!")
        except Exception as e:
            st.error(f"Lỗi cập nhật: {e}")

# Main tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(["🔊 Text to Speech", "🎤 Speech to Text", "💬 Trò chuyện", "📊 Lịch sử", "🇻🇳 TTS Việt"])

# Tab 1: Text to Speech với error handling
with tab1:
    st.header("🔊 Chuyển văn bản thành giọng nói")
    
    text_input = st.text_area(
        "Nhập văn bản tiếng Việt:",
        height=150,
        placeholder="Nhập văn bản bạn muốn chuyển thành giọng nói...",
    )
    
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col2:
        if st.button("🔊 Đọc văn bản", type="primary", use_container_width=True):
            if text_input.strip():
                with st.spinner("Đang đọc văn bản..."):
                    try:
                        # Sử dụng phương thức cải thiện nếu có
                        if hasattr(st.session_state.speech_system, 'text_to_speech_vietnamese'):
                            st.session_state.speech_system.text_to_speech_vietnamese(text_input)
                        else:
                            st.session_state.speech_system.text_to_speech(text_input)
                            
                        st.success(f"✅ Đã đọc: \"{text_input[:50]}...\"")
                        
                        # Log vào lịch sử
                        st.session_state.conversation_log.append({
                            'time': time.strftime("%H:%M:%S"),
                            'type': 'text_to_speech',
                            'content': text_input
                        })
                        
                    except Exception as e:
                        st.error(f"❌ Lỗi: {str(e)}")
                        
                        # Gợi ý khắc phục
                        if "engine" in str(e).lower():
                            st.info("💡 Thử khởi động lại ứng dụng hoặc kiểm tra loa/headphone")
            else:
                st.warning("⚠️ Vui lòng nhập văn bản!")

# Tab 2: Speech to Text với error handling tốt hơn
with tab2:
    st.header("🎤 Nhận diện giọng nói thành văn bản")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if st.button("🎤 Bắt đầu nhận diện", type="primary", use_container_width=True):
            st.session_state.is_listening = True
    
    with col2:
        if st.button("⏹️ Dừng nhận diện", use_container_width=True):
            st.session_state.is_listening = False
    
    # Error handling cho Speech Recognition
    if st.session_state.is_listening:
        st.info("🔴 Đang lắng nghe... Nói 'stop' để dừng")
        
        try:
            recognizer = sr.Recognizer()
            microphone = sr.Microphone()
            
            # Điều chỉnh cho noise
            with st.spinner("Đang điều chỉnh microphone..."):
                with microphone as source:
                    recognizer.adjust_for_ambient_noise(source, duration=1)
            
            with st.spinner("Đang lắng nghe..."):
                with microphone as source:
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            
            with st.spinner("Đang xử lý âm thanh..."):
                text = recognizer.recognize_google(audio, language='vi-VN')
            
            st.success(f"✅ Bạn đã nói: \"{text}\"")
            
            # Log
            st.session_state.conversation_log.append({
                'time': time.strftime("%H:%M:%S"),
                'type': 'speech_to_text', 
                'content': text
            })
            
            # Check stop words
            if any(word in text.lower() for word in ["stop", "dừng", "kết thúc"]):
                st.session_state.is_listening = False
                st.success("✅ Đã dừng nhận diện")
                st.rerun()
                
        except sr.WaitTimeoutError:
            st.warning("⏰ Timeout - Không nghe thấy âm thanh trong 5 giây")
            st.session_state.is_listening = False
            
        except sr.UnknownValueError:
            st.error("❌ Không thể nhận diện âm thanh. Vui lòng:")
            st.markdown("""
            - Nói rõ ràng và chậm hơn
            - Kiểm tra microphone
            - Giảm tiếng ồn xung quanh
            """)
            st.session_state.is_listening = False
            
        except sr.RequestError as e:
            st.error(f"❌ Lỗi dịch vụ: {e}")
            st.info("💡 Kiểm tra kết nối internet và thử lại")
            st.session_state.is_listening = False
            
        except Exception as e:
            st.error(f"❌ Lỗi không xác định: {e}")
            st.session_state.is_listening = False

# Tab 3: Conversation mode
with tab3:
    st.header("💬 Chế độ trò chuyện liên tục")
    
    if st.button("🚀 Bắt đầu trò chuyện", type="primary"):
        st.info("Tính năng này sẽ được phát triển trong phiên bản tiếp theo!")

# Tab 4: History với export
with tab4:
    st.header("📊 Lịch sử hoạt động")
    
    if st.session_state.conversation_log:
        st.markdown(f"**Tổng số tương tác:** {len(st.session_state.conversation_log)}")
        
        # Export button
        if st.button("📥 Xuất lịch sử"):
            output = StringIO()
            output.write("=== LỊCH SỬ HOẠT ĐỘNG ===\n\n")
            for item in st.session_state.conversation_log:
                type_name = "Bạn nói" if item['type'] == 'speech_to_text' else "AI đọc"
                output.write(f"{item['time']} - {type_name}: {item['content']}\n")
            
            st.download_button(
                "💾 Tải file",
                data=output.getvalue(),
                file_name=f"lich_su_{time.strftime('%Y%m%d_%H%M%S')}.txt",
                mime="text/plain"
            )
        
        # Display history
        st.markdown("---")
        for i, item in enumerate(reversed(st.session_state.conversation_log), 1):
            icon = "🗣️" if item['type'] == 'speech_to_text' else "🔊"
            type_name = "Bạn nói" if item['type'] == 'speech_to_text' else "AI đọc"
            st.markdown(f"**{i}. {icon} {type_name} ({item['time']}):** {item['content']}")
        
        if st.button("🗑️ Xóa lịch sử"):
            st.session_state.conversation_log = []
            st.success("Đã xóa lịch sử!")
            st.rerun()
    else:
        st.info("📝 Chưa có hoạt động nào. Hãy thử các chức năng ở tab khác!")

# Tab 5: TTS Tiếng Việt Demo
with tab5:
    st.header("🇻🇳 Demo Text-to-Speech Tiếng Việt")
    
    # Hiển thị thông tin về TTS
    if hasattr(st.session_state.speech_system, 'get_available_vietnamese_voices'):
        vietnamese_voices = st.session_state.speech_system.get_available_vietnamese_voices()
        
        if vietnamese_voices:
            st.success(f"✅ Phát hiện {len(vietnamese_voices)} giọng nói tiếng Việt:")
            for voice in vietnamese_voices:
                st.markdown(f"- **{voice['name']}** (`{voice['id']}`)")
        else:
            st.warning("⚠️ Không tìm thấy giọng nói tiếng Việt trên hệ thống")
    
    st.markdown("---")
    
    # Câu test tiếng Việt
    st.subheader("🗣️ Câu test tiếng Việt với từ kỹ thuật")
    
    test_sentences = [
        "Xin chào! Tôi là AI assistant với khả năng đọc tiếng Việt.",
        "Tôi có thể đọc các thuật ngữ như: Python, JavaScript, HTML, CSS, API.",
        "GitHub là nền tảng quản lý mã nguồn rất phổ biến.",
        "Streamlit giúp tạo ứng dụng web Python một cách dễ dàng.",
        "Machine Learning và Deep Learning đang phát triển mạnh ở Việt Nam."
    ]
    
    for i, sentence in enumerate(test_sentences, 1):
        col1, col2 = st.columns([4, 1])
        
        with col1:
            st.markdown(f"**{i}.** {sentence}")
        
        with col2:
            if st.button(f"🔊 Đọc", key=f"test_vn_{i}"):
                with st.spinner("Đang đọc..."):
                    try:
                        if hasattr(st.session_state.speech_system, 'text_to_speech_vietnamese'):
                            st.session_state.speech_system.text_to_speech_vietnamese(sentence)
                        else:
                            st.session_state.speech_system.text_to_speech(sentence)
                        st.success("✅ Hoàn thành!")
                    except Exception as e:
                        st.error(f"❌ Lỗi: {e}")
    
    st.markdown("---")
    
    # So sánh TTS
    st.subheader("🔄 So sánh TTS gốc vs cải thiện")
    
    comparison_text = "Chào bạn! Tôi sử dụng Python, AI, và GitHub để phát triển ứng dụng."
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**TTS Gốc:**")
        if st.button("🔊 TTS Gốc", use_container_width=True):
            with st.spinner("Đang đọc với TTS gốc..."):
                try:
                    st.session_state.speech_system.tts_engine.say(comparison_text)
                    st.session_state.speech_system.tts_engine.runAndWait()
                    st.success("✅ Hoàn thành!")
                except Exception as e:
                    st.error(f"❌ Lỗi: {e}")
    
    with col2:
        st.markdown("**TTS Cải thiện:**")
        if st.button("🔊 TTS Cải thiện", use_container_width=True):
            with st.spinner("Đang đọc với TTS cải thiện..."):
                try:
                    if hasattr(st.session_state.speech_system, 'text_to_speech_vietnamese'):
                        st.session_state.speech_system.text_to_speech_vietnamese(comparison_text)
                    else:
                        processed = st.session_state.speech_system.preprocess_vietnamese_text(comparison_text) if hasattr(st.session_state.speech_system, 'preprocess_vietnamese_text') else comparison_text
                        st.session_state.speech_system.text_to_speech(processed)
                    st.success("✅ Hoàn thành!")
                except Exception as e:
                    st.error(f"❌ Lỗi: {e}")
    
    # Thông tin về cải thiện
    with st.expander("ℹ️ Thông tin về cải thiện TTS"):
        st.markdown("""
        ### 🎯 **Các cải thiện đã áp dụng:**
        
        1. **Giọng nói tiếng Việt:** Sử dụng giọng "Linh" (vi-VN)
        2. **Tốc độ đọc:** Giảm từ 150 xuống 120 để rõ ràng hơn
        3. **Tiền xử lý văn bản:** 
           - `AI` → `Ây Ai`
           - `Python` → `Pai thon`
           - `GitHub` → `Gít Háp`
           - `API` → `Ây Pi Ây`
        
        ### 📋 **Kết quả:**
        - Phát âm tiếng Việt tự nhiên hơn
        - Đọc thuật ngữ kỹ thuật dễ hiểu hơn
        - Tốc độ vừa phải, không quá nhanh
        
        ### 🔧 **File liên quan:**
        - `vietnamese_tts.py` - Phiên bản TTS cải thiện
        - `TTS_IMPROVEMENT_GUIDE.md` - Hướng dẫn chi tiết
        """)

# Footer với troubleshooting
st.markdown("---")
with st.expander("🛠️ Troubleshooting & Support"):
    st.markdown("""
    ### ❗ Lỗi thường gặp:
    
    **1. PyAudio không hoạt động:**
    ```bash
    # macOS
    brew install portaudio && pip install pyaudio
    
    # Ubuntu/Debian
    sudo apt-get install portaudio19-dev python3-pyaudio
    ```
    
    **2. Microphone không hoạt động:**
    - Kiểm tra quyền truy cập microphone
    - Thử trình duyệt khác (Chrome khuyến nghị)
    - Khởi động lại ứng dụng
    
    **3. Không nhận diện được giọng nói:**
    - Kiểm tra kết nối internet
    - Nói rõ ràng, không quá nhanh
    - Giảm tiếng ồn môi trường
    
    **4. TTS không hoạt động:**
    - Kiểm tra loa/headphone
    - Điều chỉnh âm lượng hệ thống
    - Khởi động lại ứng dụng
    """)

st.markdown("""
<div style="text-align: center; color: #666; margin-top: 2rem;">
    <p>🎤 <strong>Nhận diện Âm thanh v2.0</strong> | Streamlit + Python</p>
    <p>Hỗ trợ đầy đủ cho macOS, Windows, Linux</p>
</div>
""", unsafe_allow_html=True)
