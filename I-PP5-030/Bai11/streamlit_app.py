import streamlit as st
import speech_recognition as sr
import pyttsx3
import threading
import time
import queue
from io import StringIO
import sys

# Import class từ file example.py
from example import SpeechRecognitionSystem

# Cấu hình trang
st.set_page_config(
    page_title="🎤 Nhận diện Âm thanh",
    page_icon="🎤",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS tùy chỉnh
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1E88E5;
        text-align: center;
        margin-bottom: 2rem;
    }
    .feature-box {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 5px solid #1E88E5;
    }
    .success-box {
        background-color: #d4edda;
        color: #155724;
        padding: 1rem;
        border-radius: 5px;
        border: 1px solid #c3e6cb;
    }
    .error-box {
        background-color: #f8d7da;
        color: #721c24;
        padding: 1rem;
        border-radius: 5px;
        border: 1px solid #f5c6cb;
    }
    .info-box {
        background-color: #d1ecf1;
        color: #0c5460;
        padding: 1rem;
        border-radius: 5px;
        border: 1px solid #bee5eb;
    }
</style>
""", unsafe_allow_html=True)

# Khởi tạo session state
if 'speech_system' not in st.session_state:
    with st.spinner("Đang khởi tạo hệ thống nhận diện âm thanh..."):
        st.session_state.speech_system = SpeechRecognitionSystem()
    st.success("✅ Hệ thống đã sẵn sàng!")

if 'conversation_log' not in st.session_state:
    st.session_state.conversation_log = []

if 'is_listening' not in st.session_state:
    st.session_state.is_listening = False

# Header
st.markdown('<h1 class="main-header">🎤 Chương trình Nhận diện Âm thanh</h1>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("⚙️ Cài đặt")
    
    # Cài đặt TTS
    st.subheader("🔊 Text-to-Speech")
    tts_rate = st.slider("Tốc độ đọc", 50, 300, 150)
    tts_volume = st.slider("Âm lượng", 0.0, 1.0, 0.9, 0.1)
    
    # Cập nhật cài đặt TTS
    if st.button("Áp dụng cài đặt TTS"):
        st.session_state.speech_system.tts_engine.setProperty('rate', tts_rate)
        st.session_state.speech_system.tts_engine.setProperty('volume', tts_volume)
        st.success("Đã cập nhật cài đặt!")
    
    st.divider()
    
    # Thông tin hệ thống
    st.subheader("ℹ️ Thông tin")
    st.info("""
    **Hướng dẫn sử dụng:**
    - Tab 1: Chuyển văn bản thành giọng nói
    - Tab 2: Nhận diện giọng nói thành văn bản
    - Tab 3: Trò chuyện liên tục
    
    **Lưu ý:**
    - Cần microphone để nhận diện giọng nói
    - Cần kết nối internet
    - Nói "stop" để dừng nhận diện
    """)

# Tabs chính
tab1, tab2, tab3, tab4 = st.tabs(["🔊 Text to Speech", "🎤 Speech to Text", "💬 Trò chuyện", "📊 Lịch sử"])

# Tab 1: Text to Speech
with tab1:
    st.header("🔊 Chuyển văn bản thành giọng nói")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        text_input = st.text_area(
            "Nhập văn bản tiếng Việt:",
            height=150,
            placeholder="Nhập văn bản bạn muốn chuyển thành giọng nói...",
            help="Hỗ trợ tiếng Việt có dấu"
        )
    
    with col2:
        st.markdown("### Văn bản mẫu")
        sample_texts = [
            "Xin chào các bạn!",
            "Hôm nay là một ngày đẹp trời.",
            "Chương trình Python rất thú vị.",
            "Cảm ơn bạn đã sử dụng ứng dụng."
        ]
        
        for i, sample in enumerate(sample_texts):
            if st.button(f"📝 Mẫu {i+1}", key=f"sample_{i}"):
                st.session_state.sample_text = sample
                text_input = sample
    
    # Sử dụng sample text nếu có
    if 'sample_text' in st.session_state:
        text_input = st.session_state.sample_text
        del st.session_state.sample_text
    
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col2:
        if st.button("🔊 Đọc văn bản", type="primary", use_container_width=True):
            if text_input.strip():
                with st.spinner("Đang đọc văn bản..."):
                    try:
                        st.session_state.speech_system.text_to_speech(text_input)
                        st.markdown(f'<div class="success-box">✅ Đã đọc: "{text_input}"</div>', unsafe_allow_html=True)
                    except Exception as e:
                        st.markdown(f'<div class="error-box">❌ Lỗi: {str(e)}</div>', unsafe_allow_html=True)
            else:
                st.warning("⚠️ Vui lòng nhập văn bản!")

# Tab 2: Speech to Text
with tab2:
    st.header("🎤 Nhận diện giọng nói thành văn bản")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if st.button("🎤 Bắt đầu nhận diện", type="primary", use_container_width=True):
            st.session_state.is_listening = True
    
    with col2:
        if st.button("⏹️ Dừng nhận diện", use_container_width=True):
            st.session_state.is_listening = False
    
    # Container để hiển thị kết quả real-time
    result_container = st.empty()
    status_container = st.empty()
    
    if st.session_state.is_listening:
        status_container.markdown('<div class="info-box">🔴 Đang lắng nghe... Nói "stop" để dừng</div>', unsafe_allow_html=True)
        
        try:
            with st.spinner("Đang lắng nghe..."):
                # Sử dụng microphone
                recognizer = sr.Recognizer()
                microphone = sr.Microphone()
                
                with microphone as source:
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
                
                # Nhận diện
                text = recognizer.recognize_google(audio, language='vi-VN')
                
                # Hiển thị kết quả
                result_container.markdown(f'<div class="success-box">✅ Bạn đã nói: "{text}"</div>', unsafe_allow_html=True)
                
                # Thêm vào log
                st.session_state.conversation_log.append({
                    'time': time.strftime("%H:%M:%S"),
                    'type': 'speech_to_text',
                    'content': text
                })
                
                # Kiểm tra từ khóa dừng
                if any(word in text.lower() for word in ["stop", "dừng", "kết thúc"]):
                    st.session_state.is_listening = False
                    status_container.markdown('<div class="success-box">✅ Đã dừng nhận diện</div>', unsafe_allow_html=True)
                    st.rerun()
                
        except sr.WaitTimeoutError:
            result_container.markdown('<div class="error-box">⏰ Timeout - Không nghe thấy âm thanh</div>', unsafe_allow_html=True)
            st.session_state.is_listening = False
        except sr.UnknownValueError:
            result_container.markdown('<div class="error-box">❌ Không thể nhận diện âm thanh. Vui lòng nói rõ hơn.</div>', unsafe_allow_html=True)
            st.session_state.is_listening = False
        except Exception as e:
            result_container.markdown(f'<div class="error-box">❌ Lỗi: {str(e)}</div>', unsafe_allow_html=True)
            st.session_state.is_listening = False

# Tab 3: Trò chuyện liên tục
with tab3:
    st.header("💬 Chế độ trò chuyện liên tục")
    
    st.markdown("""
    <div class="feature-box">
        <h4>🤖 Chế độ AI Assistant</h4>
        <p>Trong chế độ này, chương trình sẽ:</p>
        <ul>
            <li>Lắng nghe liên tục</li>
            <li>Phản hồi bằng giọng nói</li>
            <li>Ghi lại toàn bộ cuộc trò chuyện</li>
            <li>Dừng khi nghe "stop", "dừng", "tạm biệt"</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        if st.button("🚀 Bắt đầu trò chuyện", type="primary", use_container_width=True):
            st.session_state.conversation_mode = True
            st.session_state.speech_system.text_to_speech("Xin chào! Tôi đang lắng nghe bạn.")
    
    with col2:
        if st.button("⏸️ Tạm dừng", use_container_width=True):
            st.session_state.conversation_mode = False
    
    with col3:
        if st.button("🧹 Xóa lịch sử", use_container_width=True):
            st.session_state.conversation_log = []
            st.success("Đã xóa lịch sử trò chuyện!")
    
    # Hiển thị cuộc trò chuyện real-time
    if 'conversation_mode' in st.session_state and st.session_state.conversation_mode:
        chat_container = st.container()
        
        with chat_container:
            st.markdown("### 💬 Cuộc trò chuyện")
            
            # Hiển thị các tin nhắn gần đây
            if st.session_state.conversation_log:
                for message in st.session_state.conversation_log[-5:]:  # Hiển thị 5 tin nhắn gần nhất
                    if message['type'] == 'speech_to_text':
                        st.markdown(f"**🗣️ Bạn ({message['time']}):** {message['content']}")
                    elif message['type'] == 'text_to_speech':
                        st.markdown(f"**🤖 AI ({message['time']}):** {message['content']}")
            
            st.markdown("---")
            st.markdown("🔴 **Đang lắng nghe...** Nói gì đó hoặc nói 'stop' để dừng")

# Tab 4: Lịch sử
with tab4:
    st.header("📊 Lịch sử hoạt động")
    
    if st.session_state.conversation_log:
        st.markdown(f"**Tổng số tương tác:** {len(st.session_state.conversation_log)}")
        
        # Bộ lọc
        col1, col2 = st.columns([1, 1])
        with col1:
            filter_type = st.selectbox("Lọc theo loại:", ["Tất cả", "Speech to Text", "Text to Speech"])
        with col2:
            show_time = st.checkbox("Hiển thị thời gian", value=True)
        
        st.markdown("---")
        
        # Hiển thị lịch sử
        filtered_log = st.session_state.conversation_log
        if filter_type != "Tất cả":
            type_map = {"Speech to Text": "speech_to_text", "Text to Speech": "text_to_speech"}
            filtered_log = [msg for msg in st.session_state.conversation_log if msg['type'] == type_map[filter_type]]
        
        for i, message in enumerate(reversed(filtered_log), 1):
            time_str = f" ({message['time']})" if show_time else ""
            icon = "🗣️" if message['type'] == 'speech_to_text' else "🤖"
            type_name = "Bạn nói" if message['type'] == 'speech_to_text' else "AI đọc"
            
            st.markdown(f"**{i}. {icon} {type_name}{time_str}:** {message['content']}")
        
        # Xuất lịch sử
        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("📥 Xuất lịch sử", use_container_width=True):
                output = StringIO()
                output.write("=== LỊCH SỬ TRÒ CHUYỆN ===\n\n")
                for message in st.session_state.conversation_log:
                    type_name = "Bạn nói" if message['type'] == 'speech_to_text' else "AI đọc"
                    output.write(f"{message['time']} - {type_name}: {message['content']}\n")
                
                st.download_button(
                    label="💾 Tải file lịch sử",
                    data=output.getvalue(),
                    file_name=f"lich_su_tro_chuyen_{time.strftime('%Y%m%d_%H%M%S')}.txt",
                    mime="text/plain"
                )
        
        with col2:
            if st.button("🗑️ Xóa toàn bộ lịch sử", use_container_width=True):
                st.session_state.conversation_log = []
                st.success("Đã xóa toàn bộ lịch sử!")
                st.rerun()
    else:
        st.info("📝 Chưa có hoạt động nào. Hãy thử các chức năng ở các tab khác!")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666;">
    <p>🎤 <strong>Chương trình Nhận diện Âm thanh</strong> | Powered by Streamlit & Python</p>
    <p>Sử dụng SpeechRecognition & pyttsx3 | Hỗ trợ tiếng Việt</p>
</div>
""", unsafe_allow_html=True)
