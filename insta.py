import streamlit as st
import os
import requests
import random
import re
import sys

# إعداد واجهة Streamlit لتعمل كمتصفح
st.set_page_config(page_title="Instagram Scraper", layout="centered")

# تعريف الألوان (ستظهر في التيرمينال الداخلي إذا لزم الأمر)
P='\x1b[1;97m'; B='\x1b[1;94m'; O='\x1b[1;96m'; Z='\x1b[1;30m'; X='\x1b[1;33m'; F='\x1b[2;32m'
R='\x1b[1;31m'; L='\x1b[1;95m'; C='\x1b[2;35m'; A='\x1b[2;39m'; J='\x1b[38;5;208m'
J21='\x1b[38;5;204m'; C1='\x1b[38;5;120m'

class InstagramScraper:
    def __init__(self):
        self.good = 0
        self.bad = 0       
        self.se = 0        
        self.session = requests.Session()
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
            return user_data.get('id')        
        except:
            st.error('bad user')
            return None
        
    def wech_story(self, user_id, csrftoken, cookies):
        headers = {
            'accept-language': 'en-US,en;q=0.9',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
            'x-asbd-id':str(random.randint(30000, 79999)),
            'x-csrftoken': csrftoken,
            'x-ig-app-id': str(random.randint(1000,3337)),
            'x-ig-www-claim': 'hmac.AR1qzeEVPBuPPsJxBMlPlU19lLRm0LG3bSnly_p3mz0aRW2P',
            'x-instagram-ajax':str(random.randint(100, 3939)),
            'x-requested-with': 'XMLHttpRequest'
        }    	
        data = {'fb_api_req_friendly_name': 'PolarisStoriesV3ReelPageGalleryQuery','variables': f'{{"initial_reel_id":"{user_id}","reel_ids":["{user_id}","65467266760"],"first":1}}','server_timestamps': 'true','doc_id': '8481088891928753'}
        response = self.session.post('https://www.instagram.com/graphql/query', cookies=cookies, headers=headers, data=data).text   
        if 'organic_tracking_token' in response:
            rr = r'"pk":"(\d{19})"'
            data66 = re.search(rr,response)
            return data66.group(1)   
        else:    		
            st.warning('account There is no story : لم يتم نشر ستوري أو الحساب خاص')
            return None

    def select(self, object2_id, csrftoken, cookies):    
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36',
            'x-csrftoken': csrftoken,
            'x-ig-app-id': str(random.randint(1000,3337)),
            'x-requested-with': 'XMLHttpRequest'
        }
        data = {'container_module': 'StoriesPage','entry_point': '1','location': '4','object_id': object2_id,'object_type': '1','frx_prompt_request_type': '1'}
        response = self.session.post('https://www.instagram.com/api/v1/web/reports/get_frx_prompt/', headers=headers, data=data, cookies=cookies)    
        response_json = response.json()
        report_info = response_json.get('response', {}).get('report_info', {})
        context = response_json.get('response', {}).get('context', {})
        return report_info.get("object_id", "").strip('"'), context

    def check_sesson(self, cookies):
        re = requests.get('https://i.instagram.com/api/v1/accounts/current_user/?edit=true', headers={'User-Agent': 'Instagram 136.0.0.34.124 Android', 'x-ig-app-id': '936619743392459'}, cookies=cookies).text
        self.hh = 'login_required' not in re

# واجهة المستخدم (Streamlit UI)
st.title("Instagram Scraper Tool")
scraper = InstagramScraper()

sessionid = st.text_input("Sessionid:", type="password")
username = st.text_input("Target Username:")

# قائمة الخيارات كما هي في الكود الأصلي
sele = st.selectbox("Select Report Type:", [
    "1 - لا يعجبني فحسب",
    "2 - مضايقة أو تواصل غير مرغوب فيه",
    "3 - الانتحار أو إيذاء الذات",
    "4 - عنف أو كراهية أو استغلال",
    "5 - بيع أو ترويج عناصر محظورة",
    "6 - عري أو نشاط جنسي",
    "7 - خداع أو احتيال",
    "8 - معلومات زائفة"
])

if st.button("Start Report"):
    if sessionid and username:
        cookies = {'sessionid': sessionid}
        csrftoken = scraper.get_csrftoken()
        
        # التأكد من السيزن
        check_login = scraper.session.get('https://i.instagram.com/api/v1/accounts/current_user/?edit=true', 
                                          headers={'x-ig-app-id': '936619743392459'}, cookies=cookies).text
        if 'primary_profile_link_type' not in check_login:
            st.error('Bad Login : السيزن لا يعمل')
        else:
            u_id = scraper.user_info(username)
            if u_id:
                obj2_id = scraper.wech_story(u_id, csrftoken, cookies)
                if obj2_id:
                    obj_id, context = scraper.select(obj2_id, csrftoken, cookies)
                    
                    # تعيين الـ tag بناءً على اختيارك
                    tags = {
                        "1": 'ig_i_dont_like_it_v3',
                        "2": 'adult_content-threat_to_share_nude_images-u18-yes',
                        "3": 'suicide_or_self_harm_concern-suicide_or_self_injury',
                        "4": 'violent_hateful_or_disturbing-terrorism_or_organized_crime',
                        "5": 'selling_or_promoting_restricted_items-drugs-high-risk',
                        "6": 'adult_content-nudity_or_sexual_activity',
                        "7": 'misleading_annoying_or_scam-fraud_or_scam',
                        "8": 'misleading_annoying_or_scam-false_information-health'
                    }
                    scraper.obs = tags[sele[0]]
                    
                    st.success(f"Started reporting on {username}...")
                    
                    # مكان عرض العدادات
                    status_area = st.empty()
                    
                    while True:
                        headers = {'User-Agent': 'Mozilla/5.0', 'x-csrftoken': csrftoken, 'x-ig-app-id': '936619743392459'}
                        data = {
                            'container_module': 'StoriesPage', 'entry_point': '1', 'location': '4',
                            'object_id': obj_id, 'object_type': '1', 'context': context,
                            'selected_tag_types': f'["{scraper.obs}"]', 'frx_prompt_request_type': '2'
                        }
                        response = scraper.session.post('https://www.instagram.com/api/v1/web/reports/get_frx_prompt/', 
                                                        headers=headers, data=data, cookies=cookies)
                        
                        if '"text":"Done"' in response.text:
                            scraper.good += 1
                        else:
                            scraper.bad += 1
                        
                        scraper.check_sesson(cookies)
                        
                        # تحديث النتائج في المتصفح
                        status_area.markdown(f"**True Report:** {scraper.good} | **False Report:** {scraper.bad} | **Session Live:** {scraper.hh}")
    else:
        st.warning("Please fill in all fields.")
