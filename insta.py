import streamlit as st
import os
import requests
from hashlib import md5
from time import time
import random
import re
import threading

# إعداد واجهة المتصفح
st.set_page_config(page_title="Instagram Scraper", layout="wide")

# --- الألوان الأصلية (تم الإبقاء عليها كما هي تماماً) ---
P='\x1b[1;97m'
B='\x1b[1;94m'
O='\x1b[1;96m'
Z='\x1b[1;30m'
X='\x1b[1;33m'
F='\x1b[2;32m'
Z_RED='\x1b[1;31m' # تم تمييزه لتجنب تكرار المتغير Z
L='\x1b[1;95m'
C='\x1b[2;35m'
A='\x1b[2;39m'
P_WHITE='\x1b[38;5;231m'
J='\x1b[38;5;208m'
J1='\x1b[38;5;202m'
J2='\x1b[38;5;203m'
J21='\x1b[38;5;204m'
J22='\x1b[38;5;209m'
F1='\x1b[38;5;76m'
C1='\x1b[38;5;120m'
P1='\x1b[38;5;150m'
P2='\x1b[38;5;190m'

class InstagramScraper:
    def __init__(self, session_id_input):
        self.good = 0
        self.badh = 0
        self.bad = 0       
        self.se = 0        
        self.session = requests.Session()
        self.csrftoken = self.get_csrftoken()
        self.sessionid = session_id_input
        self.cookies = {'sessionid': self.sessionid}
        self.hh = True
        
    def get_csrftoken(self):
        response = self.session.get("https://i.instagram.com/api/v1/accounts/login/", headers={
            "User-Agent": "Instagram 64.0.0.11.97 Android (21/5.0.2; 240dpi; 540x886; LGE/lge; LG-D618; g2mds; g2mds; pt_BR)"
        })
        return response.cookies.get("csrftoken")

    def user_info(self, user):
        url = f'https://www.instagram.com/api/v1/users/web_profile_info/?username={user}'
        headers = {'x-ig-app-id': '936619743392459'}
        try:
            response = self.session.get(url, headers=headers)
            user_data = response.json().get('data', {}).get('user', {})
            user_id = user_data.get('id')        
        except:
            return "bad_user"
        return user_id
        
    def wech_story(self, user_id):
        headers = {
            'accept-language': 'en-US,en;q=0.9',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
            'x-asbd-id':str(random.randint(30000, 79999)),
            'x-csrftoken': self.csrftoken,
            'x-ig-app-id': str(random.randint(1000,3337)),
            'x-ig-www-claim': 'hmac.AR1qzeEVPBuPPsJxBMlPlU19lLRm0LG3bSnly_p3mz0aRW2P',
            'x-instagram-ajax':str(random.randint(100, 3939)),
            'x-requested-with': 'XMLHttpRequest'
        }    	
        data = {'fb_api_req_friendly_name': 'PolarisStoriesV3ReelPageGalleryQuery','variables': f'{{"initial_reel_id":"{user_id}","reel_ids":["{user_id}","65467266760"],"first":1}}','server_timestamps': 'true','doc_id': '8481088891928753'}

        response = self.session.post('https://www.instagram.com/graphql/query', cookies=self.cookies, headers=headers, data=data).text   
        if 'organic_tracking_token' in response:
            rr = r'"pk":"(\d{19})"'
            data66 = re.search(rr,response)
            object2_id = data66.group(1)   
        else:    		
            return "no_story"
        return object2_id
    	
    def select(self, object2_id):    
        headers = {
            'accept-language': 'en-US,en;q=0.9',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
            'x-asbd-id':str(random.randint(30000, 79999)),
            'x-csrftoken': self.csrftoken,
            'x-ig-app-id': str(random.randint(1000,3337)),
            'x-ig-www-claim': 'hmac.AR1qzeEVPBuPPsJxBMlPlU19lLRm0LG3bSnly_p3mz0aRW2P',
            'x-instagram-ajax':str(random.randint(100, 3939)),
            'x-requested-with': 'XMLHttpRequest'
        }
        data = {
            'container_module': 'StoriesPage',
            'entry_point': '1',
            'location': '4',
            'object_id': object2_id,
            'object_type': '1',
            'frx_prompt_request_type': '1'
        }
        response = self.session.post('https://www.instagram.com/api/v1/web/reports/get_frx_prompt/', headers=headers, data=data, cookies=self.cookies)    
        response_json = response.json()
        report_info = response_json.get('response', {}).get('report_info', {})
        context = response_json.get('response', {}).get('context', {})
        object_id = report_info.get("object_id", "").strip('"')       
        return object_id, context

    def check_sesson(self):
        re_check = requests.get('https://i.instagram.com/api/v1/accounts/current_user/?edit=true', headers={'User-Agent': 'Instagram 136.0.0.34.124 Android (23/6.0.1; 640dpi; 1440x2560; samsung; SM-G935; hero2lte; samsungexynos8890; en_US; 208061712)', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'x-ig-app-id': '936619743392459'}, cookies=self.cookies).text
        if 'login_required' in re_check:
            self.hh = False
        else:
            self.hh = True    	  		

    def report_story(self, object_id, context, obs_tag, stats_placeholder):
        headers = {
            'accept-language': 'en-US,en;q=0.9',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
            'x-asbd-id':str(random.randint(30000, 79999)),
            'x-csrftoken': self.csrftoken,
            'x-ig-app-id': str(random.randint(1000,3337)),
            'x-ig-www-claim': 'hmac.AR1qzeEVPBuPPsJxBMlPlU19lLRm0LG3bSnly_p3mz0aRW2P',
            'x-instagram-ajax':str(random.randint(100, 3939)),
            'x-requested-with': 'XMLHttpRequest'
        }
        data = {
                'container_module': 'StoriesPage',
                'entry_point': '1',
                'location': '4',
                'object_id': object_id,
                'object_type': '1',
                'context': context,
                'selected_tag_types': f'["{obs_tag}"]',
                'frx_prompt_request_type': '2',
        }
    
        response = self.session.post('https://www.instagram.com/api/v1/web/reports/get_frx_prompt/', headers=headers, data=data, cookies=self.cookies)       
        if '"text":"Done"' in response.text:
            self.good += 1
        elif 'Try Again Later' in response.text:
            st.error('Block : لقد تم حظرك قم باستخراج سيزن جديد')   
            return False
        else:
            self.bad += 1        
        self.check_sesson()                        
        stats_placeholder.markdown(f"**True Report:** {self.good} | **False Report:** {self.bad} | **Bad Session_id:** {not self.hh}")
        return True

# --- واجهة مستخدم Streamlit (المتصفح) ---
st.title("Instagram Scraper Tool")

# الحقول الأصلية كمدخلات ويب
sessionid_in = st.text_input("Enter Sessionid:", type="password")
target_user = st.text_input("Enter target username:")

# القائمة الأصلية كما هي تماماً في دالة title()
st.info("إختر نوع البلاغ:")
sele = st.selectbox("Select Option:", [
    "1 - idont Like : لا يعجبني فحسب",
    "2 - bullying or unwanted contact : مضايقة أو تواصل غير مرغوب فيه",
    "3 - suicide or self harm or eating : الانتحار أو إيذاء الذات",
    "4 - violence hate or exploitation : عنف أو كراهية أو استغلال",
    "5 - selling or promoting : بيع أو ترويج عناصر محظورة",
    "6 - nudity or sexual activity : عري أو نشاط جنسي",
    "7 - scam fraud or spam : خداع أو احتيال أو محتوى غير مهم",
    "8 - false information : معلومات زائفة"
])

# منطق الشروط الفرعية كما هو في الكود الأصلي
obs_tag = ""
if "1" in sele:
    obs_tag = 'ig_i_dont_like_it_v3'
elif "2" in sele:
    obs_tag = 'adult_content-threat_to_share_nude_images-u18-yes'
elif "3" in sele:
    obs_tag = 'suicide_or_self_harm_concern-suicide_or_self_injury'
elif "4" in sele:
    obs_tag = 'violent_hateful_or_disturbing-terrorism_or_organized_crime'
elif "5" in sele:
    obs_tag = 'selling_or_promoting_restricted_items-drugs-high-risk'
elif "6" in sele:
    obs_tag = 'adult_content-nudity_or_sexual_activity'
elif "7" in sele:
    obs_tag = 'misleading_annoying_or_scam-fraud_or_scam'
elif "8" in sele:
    obs_tag = 'misleading_annoying_or_scam-false_information-health'

if st.button("Start Reporting"):
    if sessionid_in and target_user:
        scraper = InstagramScraper(sessionid_in)
        
        # التأكد من السيزن
        re_val = scraper.session.get('https://i.instagram.com/api/v1/accounts/current_user/?edit=true', 
                                    headers={'User-Agent': 'Instagram 136.0.0.34.124 Android', 'x-ig-app-id': '936619743392459'}, 
                                    cookies=scraper.cookies).text
        
        if 'primary_profile_link_type' not in re_val:
            st.error('Bad Login : عذراً السيزن لا يعمل يرجى سحب جديد')
        else:
            u_id = scraper.user_info(target_user)
            if u_id == "bad_user":
                st.error("Bad User")
            else:
                obj_story = scraper.wech_story(u_id)
                if obj_story == "no_story":
                    st.error('account There is no story : لم يتم نشر ستوري')
                else:
                    obj_id, ctx = scraper.select(obj_story)
                    st.success("Reporting started...")
                    
                    # مكان عرض الإحصائيات المحدثة
                    stats_placeholder = st.empty()
                    
                    while True:
                        success = scraper.report_story(obj_id, ctx, obs_tag, stats_placeholder)
                        if not success:
                            break
    else:
        st.warning("Please fill Session ID and Target Username")
        # التأكد من صحة السيزن أولاً
        re_login = scr.session.get('https://i.instagram.com/api/v1/accounts/current_user/?edit=true', headers={'x-ig-app-id': '936619743392459'}, cookies=scr.cookies).text
        if 'primary_profile_link_type' not in re_login:
            st.error('Bad Login : عذراً السيزن لا يعمل يرجى سحب جديد')
        else:
            u_id = scr.user_info(user_input)
            if u_id == "bad_user":
                st.error("Bad User")
            else:
                obj2 = scr.wech_story(u_id)
                if obj2 == "no_story":
                    st.error("account There is no story : لم يتم نشر ستوري")
                else:
                    obj_id, context = scr.select(obj2)
                    st.success(f"Started reporting on: {user_input}")
                    
                    # عدادات تظهر وتتحدث مباشرة
                    stats = st.empty()
                    
                    while True:
                        headers = {
                            'User-Agent': 'Mozilla/5.0',
                            'x-csrftoken': scr.csrftoken,
                            'x-ig-app-id': str(random.randint(1000,3337)),
                            'x-requested-with': 'XMLHttpRequest'
                        }
                        data = {
                            'container_module': 'StoriesPage', 'entry_point': '1', 'location': '4',
                            'object_id': obj_id, 'object_type': '1', 'context': context,
                            'selected_tag_types': f'["{obs_final}"]', 'frx_prompt_request_type': '2'
                        }
                        
                        try:
                            resp = scr.session.post('https://www.instagram.com/api/v1/web/reports/get_frx_prompt/', headers=headers, data=data, cookies=scr.cookies)
                            if '"text":"Done"' in resp.text:
                                scr.good += 1
                            elif 'Try Again Later' in resp.text:
                                st.error('Block : لقد تم حظرك قم باستخراج سيزن جديد')
                                break
                            else:
                                scr.bad += 1
                                
                            scr.check_sesson()
                            # تحديث الإحصائيات في المتصفح
                            stats.markdown(f"✅ **True Report:** {scr.good} | ❌ **False Report:** {scr.bad} | 🔑 **Session Live:** {scr.hh}")
                            time.sleep(2) # تأخير بسيط لضمان استقرار المتصفح
                        except:
                            st.error("Connection Error")
                            break

