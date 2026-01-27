import os
import requests
from hashlib import md5
from time import time
import random
import re
import threading
import sys

# إعدادات الألوان
P = '\x1b[1;97m'
B = '\x1b[1;94m'
O = '\x1b[1;96m'
Z = '\x1b[1;30m'
X = '\x1b[1;33m'
F = '\x1b[2;32m'
R = '\x1b[1;31m' # تم تصحيح المتغير Z المتكرر إلى R للأحمر
L = '\x1b[1;95m'
C = '\x1b[2;35m'
A = '\x1b[2;39m'
P = '\x1b[38;5;231m'
J = '\x1b[38;5;208m'
J1 = '\x1b[38;5;202m'
J2 = '\x1b[38;5;203m'
J21 = '\x1b[38;5;204m'
J22 = '\x1b[38;5;209m'
F1 = '\x1b[38;5;76m'
C1 = '\x1b[38;5;120m'
P1 = '\x1b[38;5;150m'
P2 = '\x1b[38;5;190m'

class InstagramScraper:
    def __init__(self):
        self.good = 0
        self.bad = 0
        self.hh = True
        self.session = requests.Session()
        self.csrftoken = self.get_csrftoken()
        
        print(f"{C1}—" * 30)
        self.sessionid = input(f"{P}Enter Sessionid: ")
        self.cookies = {'sessionid': self.sessionid}
        
        # التحقق من تسجيل الدخول
        try:
            check = self.session.get('https://i.instagram.com/api/v1/accounts/current_user/?edit=true', 
                                   headers={'User-Agent': 'Instagram 136.0.0.34.124 Android (23/6.0.1; 640dpi; 1440x2560; samsung; SM-G935; hero2lte; samsungexynos8890; en_US; 208061712)', 
                                            'x-ig-app-id': '936619743392459'}, 
                                   cookies=self.cookies).text
            if 'primary_profile_link_type' not in check:
                print(f'{R}Bad Login : عذراً السيزن لا يعمل يرجى سحب جديد')
                sys.exit()
        except:
            print(f'{R}Error connecting to Instagram')
            sys.exit()

    def get_csrftoken(self):
        try:
            response = self.session.get("https://i.instagram.com/api/v1/accounts/login/", headers={
                "User-Agent": "Instagram 64.0.0.11.97 Android (21/5.0.2; 240dpi; 540x886; LGE/lge; LG-D618; g2mds; g2mds; pt_BR)"
            })
            return response.cookies.get("csrftoken")
        except:
            return "missing"

    def user_info(self, user):
        url = f'https://www.instagram.com/api/v1/users/web_profile_info/?username={user}'
        headers = {'x-ig-app-id': '936619743392459', 'User-Agent': 'Mozilla/5.0'}
        try:
            response = self.session.get(url, headers=headers)
            user_data = response.json().get('data', {}).get('user', {})
            return user_data.get('id')
        except:
            print(f'{R}bad user')
            sys.exit()

    def wech_story(self, user_id):
        headers = {
            'accept-language': 'en-US,en;q=0.9',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
            'x-csrftoken': self.csrftoken,
            'x-ig-app-id': '936619743392459',
            'x-requested-with': 'XMLHttpRequest'
        }
        data = {
            'fb_api_req_friendly_name': 'PolarisStoriesV3ReelPageGalleryQuery',
            'variables': f'{{"initial_reel_id":"{user_id}","reel_ids":["{user_id}"],"first":1}}',
            'doc_id': '8481088891928753'
        }
        response = self.session.post('https://www.instagram.com/graphql/query', cookies=self.cookies, headers=headers, data=data).text
        if 'organic_tracking_token' in response:
            rr = r'"pk":"(\d+)"'
            match = re.search(rr, response)
            return match.group(1) if match else None
        else:
            print(f'{R}Account has no story or is private.')
            sys.exit()

    def select(self, object2_id):
        headers = {
            'User-Agent': 'Mozilla/5.0',
            'x-csrftoken': self.csrftoken,
            'x-ig-app-id': '936619743392459',
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
        res = self.session.post('https://www.instagram.com/api/v1/web/reports/get_frx_prompt/', headers=headers, data=data, cookies=self.cookies).json()
        report_info = res.get('response', {}).get('report_info', {})
        return report_info.get("object_id", "").strip('"'), res.get('response', {}).get('context', {})

    def title(self):
        os.system('clear' if os.name == 'posix' else 'cls')
        print(f"""{C1}
[1]  idont Like : لا يعجبني فحسب
--------------------------------------
[2]  bullying or unwanted contact : مضايقة أو تواصل غير مرغوب فيه
--------------------------------------
[3]  suicide or self harm or eating : الانتحار أو إيذاء الذات
--------------------------------------
[4]  violence hate or exploitation : عنف أو كراهية أو استغلال
--------------------------------------
[5]  selling or promoting : بيع أو ترويج عناصر محظورة
--------------------------------------
[6]  nudity or sexual activity : عري أو نشاط جنسي
--------------------------------------
[7]  scam fraud or spam : خداع أو احتيال أو محتوى غير مهم 
--------------------------------------
[8]  false information : معلومات زائفة""")
        
        sele = input(f"\n|{J21}•{P}>{J21} SELECT {P}: ")
        
        # منطق الاختيارات (تم اختصاره للحفاظ على المساحة مع بقاءه كاملاً)
        if sele == '1': self.obs = 'ig_i_dont_like_it_v3'
        elif sele == '2': self.obs = 'adult_content-threat_to_share_nude_images-u18-yes'
        elif sele == '3': self.obs = 'suicide_or_self_harm_concern-suicide_or_self_injury'
        elif sele == '4': self.obs = 'violent_hateful_or_disturbing-terrorism_or_organized_crime'
        elif sele == '5': self.obs = 'selling_or_promoting_restricted_items-drugs-high-risk'
        elif sele == '6': self.obs = 'adult_content-nudity_or_sexual_activity'
        elif sele == '7': self.obs = 'misleading_annoying_or_scam-fraud_or_scam'
        elif sele == '8': self.obs = 'misleading_annoying_or_scam-false_information-health'
        else: self.obs = 'ig_i_dont_like_it_v3'
        
        return self.obs

    def check_session(self):
        try:
            re_check = self.session.get('https://i.instagram.com/api/v1/accounts/current_user/?edit=true', headers={'User-Agent': 'Instagram 136.0.0.34.124'}, cookies=self.cookies).text
            self.hh = 'primary_profile_link_type' in re_check
        except:
            self.hh = False

    def report_story(self, object_id, context):
        headers = {
            'User-Agent': 'Mozilla/5.0',
            'x-csrftoken': self.csrftoken,
            'x-ig-app-id': '936619743392459',
            'x-requested-with': 'XMLHttpRequest'
        }
        data = {
            'container_module': 'StoriesPage',
            'entry_point': '1',
            'location': '4',
            'object_id': object_id,
            'object_type': '1',
            'context': context,
            'selected_tag_types': f'["{self.obs}"]',
            'frx_prompt_request_type': '2',
        }
        try:
            response = self.session.post('https://www.instagram.com/api/v1/web/reports/get_frx_prompt/', headers=headers, data=data, cookies=self.cookies)
            if '"text":"Done"' in response.text:
                self.good += 1
            elif 'Try Again Later' in response.text:
                print(f'\n{R}Block : تم حظر السيزن مؤقتاً')
                sys.exit()
            else:
                self.bad += 1
            
            self.check_session()
            # طباعة النتيجة في سطر واحد محدث بدلاً من تنظيف الشاشة بالكامل لتجنب "الوميض" في المتصفح
            sys.stdout.write(f'\r{C1}True: {self.good} {P}| {J21}False: {self.bad} {P}| {X}Session Live: {self.hh}   ')
            sys.stdout.flush()
        except:
            pass

    def main(self):
        user = input(f'{P}Enter target username: ')
        u_id = self.user_info(user)
        obj2_id = self.wech_story(u_id)
        obj_id, ctx = self.select(obj2_id)
        self.title()
        print(f"\n{F1}Starting Reporting...{P}\n")
        while True:
            self.report_story(obj_id, ctx)

if __name__ == "__main__":
    scraper = InstagramScraper()
    scraper.main()

