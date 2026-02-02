import streamlit as st
import requests
import random
from user_agent import generate_user_agent
from time import sleep

# --- إعدادات الصفحة والتصميم ---
st.set_page_config(page_title="تطوير ايمو", page_icon="⚡", layout="centered")

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        color: white;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
    }
    
    @keyframes glow {
        0% { box-shadow: 0 0 10px #00ffff; }
        50% { box-shadow: 0 0 20px #00ffff, 0 0 30px #0080ff; }
        100% { box-shadow: 0 0 10px #00ffff; }
    }
    
    @keyframes borderGlow {
        0% { border-color: #00ffff; }
        50% { border-color: #0080ff; }
        100% { border-color: #00ffff; }
    }
    
    .user-avatar {
        display: block;
        margin: 20px auto;
        border: 3px solid;
        border-radius: 20px;
        animation: float 3s ease-in-out infinite, borderGlow 2s infinite;
        width: 180px;
        height: 180px;
        object-fit: cover;
        padding: 5px;
        background: rgba(255, 255, 255, 0.05);
    }
    
    .main-title {
        text-align: center;
        font-size: 2.5rem;
        background: linear-gradient(90deg, #00ffff, #0080ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 5px;
        text-shadow: 0 2px 10px rgba(0, 255, 255, 0.3);
    }
    
    .subtitle {
        text-align: center;
        color: #a0a0ff;
        font-size: 1rem;
        margin-bottom: 30px;
        opacity: 0.9;
    }
    
    .card {
        background: rgba(20, 20, 40, 0.7);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 25px;
        margin: 20px 0;
        border: 1px solid rgba(0, 255, 255, 0.1);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
    }
    
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        background: linear-gradient(45deg, #00ffff, #0080ff);
        color: white;
        font-weight: bold;
        border: none;
        height: 50px;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        margin-top: 20px;
        animation: glow 2s infinite;
    }
    
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 25px rgba(0, 255, 255, 0.4);
        background: linear-gradient(45deg, #0080ff, #00ffff);
    }
    
    .stSelectbox div[data-baseweb="select"] {
        background-color: rgba(20, 20, 40, 0.8);
        border: 2px solid rgba(0, 255, 255, 0.3);
        border-radius: 10px;
        color: white;
    }
    
    .stSelectbox div[data-baseweb="select"]:hover {
        border-color: #00ffff;
    }
    
    .stTextInput>div>div>input {
        background-color: rgba(20, 20, 40, 0.8);
        color: #00ffff;
        border: 2px solid rgba(0, 255, 255, 0.3);
        border-radius: 10px;
        text-align: center;
        padding: 10px;
        font-size: 1rem;
    }
    
    .stTextInput>div>div>input:focus {
        border-color: #00ffff;
        box-shadow: 0 0 10px rgba(0, 255, 255, 0.5);
    }
    
    .divider {
        height: 2px;
        background: linear-gradient(90deg, transparent, #00ffff, transparent);
        margin: 30px 0;
        opacity: 0.5;
    }
    
    .footer {
        text-align: center;
        color: #888;
        font-size: 0.9rem;
        margin-top: 30px;
        padding-top: 15px;
        border-top: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .service-label {
        color: #a0a0ff;
        margin-bottom: 8px;
        font-weight: 600;
    }
    
    .input-label {
        color: #00ffff;
        margin-bottom: 8px;
        font-weight: 600;
        display: block;
    }
    </style>
    """, unsafe_allow_html=True)

# --- عرض الصورة الشخصية ---
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown(f'<img src="https://i.ibb.co/WvWSQmRr/4816e0fe7555f14dec77d03e9f1f2912.jpg" class="user-avatar">', unsafe_allow_html=True)
st.markdown('<h1 class="main-title">تطوير ايمو</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">خدمات التواصل الاجتماعي المتكاملة</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- دالة لتوليد IP عشوائي ---
def generate_random_ip():
    return ".".join(map(str, (random.randint(0, 255) for _ in range(4))))

# --- دالات الرشق الأصلية ---
def send_request(url, link, quantity=None):
    random_ip = generate_random_ip()
    headers = {
        "User-Agent": generate_user_agent(),
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://leofame.com",
        "referer": url.split('?')[0],
        "cookie": "token=FAKETOKEN; cf_clearance=FAKECOOKIE",
        "X-Forwarded-For": random_ip,
        "Client-IP": random_ip
    }
    data = {
        "token": "FAKETOKEN",
        "timezone_offset": "Asia/Baghdad",
        "free_link": link
    }
    if quantity: data["quantity"] = quantity
    
    try:
        # إضافة تأخير عشوائي بين 3 إلى 7 ثوانٍ
        wait_time = random.randint(3, 7)
        st.info(f"⏳ جاري الانتظار {wait_time} ثوانٍ لتجنب الحظر...")
        sleep(wait_time)
        
        r = requests.post(url, headers=headers, data=data)
        if "Please wait" in r.text or '"error":' in r.text:
            st.error("⚠️ الموقع يطلب الانتظار. جرب لاحقاً أو غير الرابط.")
        else:
            st.success(f"✅ تم الإرسال بنجاح بـ IP وهمي: {random_ip}")
    except Exception as e:
        st.error(f"حدث خطأ في الاتصال: {e}")

# --- واجهة الاختيار ---
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<div class="service-label">اختر الخدمة المطلوبة:</div>', unsafe_allow_html=True)

option = st.selectbox(
    "",
    ["إعجابات يوتيوب", "إعجابات تيك توك", "حفظ منشور إنستغرام", "مشاهدات تيك توك"],
    label_visibility="collapsed"
)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

st.markdown('<div class="input-label">ضع الرابط هنا:</div>', unsafe_allow_html=True)
video_url = st.text_input("", placeholder="https://...", label_visibility="collapsed")

if st.button("🚀 بدء التشغيل"):
    if video_url:
        with st.spinner('جاري معالجة الطلب...'):
            if option == "إعجابات يوتيوب":
                send_request("https://leofame.com/free-youtube-likes?api=1", video_url)
            elif option == "إعجابات تيك توك":
                send_request("https://leofame.com/free-tiktok-likes?api=1", video_url)
            elif option == "حفظ منشور إنستغرام":
                send_request("https://leofame.com/free-instagram-saves?api=1", video_url, "30")
            elif option == "مشاهدات تيك توك":
                send_request("https://leofame.com/ar/free-tiktok-views?api=1", video_url, "200")
    else:
        st.warning("⚠️ يرجى إدخال الرابط أولاً!")
        
st.markdown('</div>', unsafe_allow_html=True)

# --- التذييل ---
st.markdown('<div class="footer">تم التطوير بواسطة ايمو</div>', unsafe_allow_html=True)
