import os
import requests
import webbrowser
import time
import streamlit as st
import random
import re
from typing import Any
from hashlib import md5

# محاولة استيراد المكتبات الأصلية
try:
    import instaloader
except:
    os.system('pip install instaloader')
    import instaloader

# --- الكود الأصلي المدمج (بدون حذف أي حرف) ---
class sin:
    def __init__(self):
        self.g=0
        # الحفاظ على جميع تعريفات الألوان من الكود الأول
        self.P='\x1b[1;97m'
        self.B='\x1b[1;94m'
        self.O='\x1b[1;96m'
        self.Z='\x1b[1;30m'
        self.X='\x1b[1;33m'
        self.F='\x1b[2;32m'
        self.Z_red='\x1b[1;31m'
        self.L='\x1b[1;95m'
        self.C='\x1b[2;35m'
        self.A='\x1b[2;39m'
        self.P_white='\x1b[38;5;231m'
        self.J='\x1b[38;5;208m'
        self.J1='\x1b[38;5;202m'
        self.J2='\x1b[38;5;203m'
        self.J21='\x1b[38;5;204m'
        self.J22='\x1b[38;5;209m'
        self.F1='\x1b[38;5;76m'
        self.C1='\x1b[38;5;120m'
        self.P1='\x1b[38;5;150m'
        self.P2='\x1b[38;5;190m'
        self.session = requests.Session()

    def exit_csr(self)->any:
        api=requests.get('https://www.instagram.com').cookies.get('csrftoken')
        return api

    def user_for_id(self,user_id :str,)->any:
        B = instaloader.Instaloader()
        username = user_id
        profile = instaloader.Profile.from_username(B.context, username)
        return profile.userid

    # --- كود البلاغ على الستوري (بدون أي حذف أو تعديل) ---
    def wech_story(self, user_id, sessionid, csrftoken):
        headers = {
            'accept-language': 'en-US,en;q=0.9',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
            'x-asbd-id': str(random.randint(30000, 79999)),
            'x-csrftoken': csrftoken,
            'x-ig-app-id': str(random.randint(1000, 3337)),
            'x-ig-www-claim': 'hmac.AR1qzeEVPBuPPsJxBMlPlU19lLRm0LG3bSnly_p3mz0aRW2P',
            'x-instagram-ajax': str(random.randint(100, 3939)),
            'x-requested-with': 'XMLHttpRequest'
        }
        cookies = {'sessionid': sessionid}
        data = {
            'fb_api_req_friendly_name': 'PolarisStoriesV3ReelPageGalleryQuery',
            'variables': f'{{"initial_reel_id":"{user_id}","reel_ids":["{user_id}","65467266760"],"first":1}}',
            'server_timestamps': 'true',
            'doc_id': '8481088891928753'
        }
        try:
            response = requests.post('https://www.instagram.com/graphql/query', cookies=cookies, headers=headers, data=data).text
            if 'organic_tracking_token' in response:
                rr = r'"pk":"(\d{19})"'
                data66 = re.search(rr, response)
                object2_id = data66.group(1)
                return object2_id
            return None
        except:
            return None

    def report_story_logic(self, sessionid, csrftoken, story_id):
        headers = {
            'accept-language': 'en-US,en;q=0.9',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
            'x-asbd-id': str(random.randint(30000, 79999)),
            'x-csrftoken': csrftoken,
            'x-ig-app-id': '1217981644879628',
            'x-requested-with': 'XMLHttpRequest'
        }
        cookies = {'sessionid': sessionid}
        data = {
            'container_module': 'StoriesPage',
            'entry_point': '1',
            'location': '4',
            'object_id': story_id,
            'object_type': '1',
            'selected_tag_types': '["violent_hateful_or_disturbing-credible_threat"]',
            'frx_prompt_request_type': '2',
        }
        try:
            response = requests.post('https://www.instagram.com/api/v1/web/reports/get_frx_prompt/', headers=headers, data=data, cookies=cookies)
            if '"text":"Done"' in response.text or '"status":"ok"' in response.text:
                self.g += 1
                return True, f" [{self.g}] تم بلاغ الستوري بنجاح ✅"
            return False, " [!] فشل بلاغ الستوري"
        except Exception as e:
            return False, str(e)

    # --- كود البلاغ على الحساب (بدون حذف الـ context الطويل) ---
    def Send_Report(self,Sessionid:str,crf_tt:str,USER_E:str,)->any:
        try:
            url = "https://www.instagram.com/api/v1/web/reports/get_frx_prompt/"
            payload = {
              'container_module': "profilePage",
              'entry_point': "1",
              'location': "2",
              'object_id': f"{USER_E!r}",
              'object_type': "5",
              'context': "{\"tags\":[\"ig_report_account\",\"ig_its_inappropriate\",\"violence_hate_or_exploitation\"],\"ixt_context_from_www\":\"QVFZWlRaZldlWnlJVlRtRklPMmRrNEoyd1p5WWVVRG9jblN3Slhra2JXY210QmJPQXU2YnNEcG16SHpVaFJhZXVKcVN2eU9GS25ZR3Q0a3dfWDE0ODRjeXpLWlZrb1ZQaHd0dDYwQklWMjVUcTNua05FdldGY1A1Nk5SUE9YYXM2SXhiVnh1WlJROTdBS3ZWdzRDQzREdkt5R2dsOFNoamRpekphdmZfQUJKVlFhYktzbERuQmN3S2dxUkxBVHQ3MnhsVDZqZ19kY1poTHJjT1F2N0hFMkE0dl9lQ3hINkl0aGVrU0RuNEdDbGtIamR1SGhwRm93ZnpxOXNxTVZMYUpZTGFVR0FnNEk2VnFjUGRJZGVjSklfOHl6azRsb1ZfNUhxa2lGWVlMaE5SdG9ZQzYtVjFhS05Wd2JVMkNvem5QMmVuT0JnUjdzblFJTEY0OEl0dzhaXzdsaXFXWlJoTDBiNDdfNHRxYS1iOUtjd3BQTjByZjMzcDRqZ0VIZkdZV2hjVXJmYVlLc21RQXJJWmFKOWtoRE9WZ2Y2LWJpUEt3T1BrdTU2YUZoUjV5bFBLWnJPQXBSQTlvdVdEcUJ3UmtzVkd3ZHJNcVdWUHJ5bGx4WWtzMm82ZlJOWWlRcl9WeHZBREpDRUxVamZnTkhEdEFjN0lzOFFLZlkzTGVkOHpXN1dBTXB1UkZhd09LcFZaSjNMQUpKZi13RmNLNXU3ajFrNi1DdHg3ZUVqUi1VTzQ0YXUtcHFySGM4VGRkaEtFdXh5cjhsUC1pb0s3SVhaWFBUd3lleFBQajlLcC1FWUNfanMwTjdKMkc5VWxsV2dzZ2UxZ3VaT0VXaGc3UklVUjN0Y2tldGhSTUR2X0xvd2FJewNDMHFmbWhEZmhubGpRejFsLTVhYTAyREhVYnpvX2ltNUllRTJBVXJ0eWpGVHdtTWxwS2i3ek51VEFHV2tPbVdxME56WHBMajVwa1hDRldBeGpoTUVDUU5BZmszR2o2NmVKeVBwakp5Q1FsUzEwUkFsUjc0YmRSSEpLTzN6MHNFMFMwTFNxQUVHZU5nZ1ZNbDJKZVJWU2hpRjVlX3NYb2NLdDVVTVJ4RDdVU25nelBxTXF4XzZNa3c1cnlPMVk5MDBNYmU4dmEtdTBLU1NqR3dBMkl6YXp4MFdRaHdEN0pfMG5HOG1VTG1CMWhmT2RUbUJlRllYbWhfTUZhTlFWU0ZObHpBMEpSaDBVT29veEg5bVFBOWJPRXVickd4Nl8tYmZwem5EZWZLNUxFX1V2djlGdlF0aE5BSFZHTHJqbmFoUEpfMThwdndqUTRRV3BuQnBNdFJ3NDdTaEU1YktzVEl3THQ2eVVXMWpHWFBTQUo5LUxvcV9lVmVqU3FZdDdkY0owaVgyNlo3SVhjOExiOWh6VWQyNlJMQXZFZ3daZTNBd3NoN2lYRlRYclVIUV9iQ0E2NUZIZVZHV0RJNHNyRHZzVi1NTDBtWUkxSUxLNVpVNE4ySURXOV9HaHVlaDhhbDZBMnIzN3BRdU5TSEtYRkpQNnZoU0J3U0xuTUNhbDZQVmpEZVBRc1RjT2hfRGJubWZmWXhGeWRRLXB2VVRkdW5yOWxJelFzeHh3cldnd2hvNk5VTjRrc0Rpa0p1R0xvQkpmd0t6dHRJWnZIZkNsQmQ3ZjZrcmVyZk53VHRPSk9kR0RFcWUta1QydmRBOTlRUl9QNVhsdXptdzJSeW40bko3N1NVMm5aQ1dJa3BTNUoyNFhOU0x1TmRJTjlMSXdYSWNISDB2WHBNOWNId0Zqd1Fhc2pJbXY1RWwyQ08wYXhvV1BIMW9MNGlZdzlBenZCT2pZT29zR19oOUU2eDg2VXBlbWJJNXhTUjRjeDhEZU1kNGxaMXkzMkNnWXZHZmVCQzVIR1lwczJGRnJLOFJRUnJhV2k3UVZnMi1uUl9tTVo4V0ZlQkowdkZqaFlqSWN3cndUd20wTjhwd0IwUXkwd1RkbVVRZzZSbkdrWjFUdktBeFlaVFhwM0Nud0dENmdDZFpVdE9OOHJlWjE1WGhoYkp5NjQ4Mi1sbE1mcWloUU84UzE5VnBkekNrbFBuNWFkU1MyejducmFGRUhnOUdPcm9EYWNxSGU2WmdULWMxSmo2QXdFdlV1OGpTU2YtZ1U3YTF5VlpWZlhaRTFjVGRuYnI2WUEyX0xCckYzWFdZejNvWEx1SkpXRWZQTEpFVVBJNjBMUmtvdzZrMWdBRUNxd1RNa0liWHV6R3paZHZmbVlAzUohmTI3ejJZQjE5ODFkNmI2ZWtPY3pZT200R1E1Z3pBZTFJcHBLQ3Z4X2NZSHBzUkVnUWFLSm9iQ2tpUG9SZWVvMzhtZ2pjdElycThkLW9hczdYeGZZQVc4MHhCcld1M3ZmQmNOQ01rWlZkT2ZfTzRCVEU3ck5hVG12c2QySWFRLUNwemlqWUc2LTk1WXJMWWd4bkliUmNObHJOOXF1bXZfWEkzSWpPenhpRVNnbFA2NEVxcVJiam5hdGlqbV8xSkpsNmVhSGFMTzVuLVZ3bDQxdURQY2lvTWJUbDNrUWhtMFlOMDZWNjNnVTJMUXhvME9BTVFCeUstSjVPWDkwQXR2dGhrN0Radlp2dFB5eVhDYmNoaGIxVUdDeU5rdW1PM1BlSVBtcHZmd2NPM0pMMDE1ZzZGNTgyTEJHamlJdndDWEJLaXh0Vi1xRkNpWndkRy1rRXpoX1Zwc1R6TmpIbHYxLXNJc2d3QmJhRmwxM2d3dlNqSExvVnBDeFRFM0Y4X2NqZHgtdS1WaGNGNlF2ZkYtMzBlTWtOdDI2TVkyWVpyV0tZb1RUOEhnZXZob2I2Yk95MFhEWU1FcTVSNWt4SE55em00ZXlsU1FHVkxEODhGbDd0WU0xN3c3TTRVbTM0YkRieHEtUmg5aFFDdDBHOWhBUVhnQnFyZXZzdXRoLU02eElHak5PQXRqSmhDOGJfY2U0V3ZQeVRrXzVWMWdyWmhZX1BtWk1TdFZDdHpUSmFlRVdHd1o3ZmZwS0doenlfcVFrVGVJcFVTdDdfcmhuRENUTEs0eDJMVlF3V25fN1BjZ0tzMFBnVnRydWN0RWFYQlRTMzM3ZFEyWmhuUGU3VlhxZHRIbGtKM1E3ZXBpOXZlaUdBemgtOHdjTTV1UGJ4eWt0aWJUWFZJR2U5aGI2TkZMUEdvWUlFcmNvbFpoV2Rpakp2ay1OQl9TUTBSMEY0VFY4am9WT1oxd2d3ckFUbmIzMkhVTW1JbHBTbUt4elE1TmJpVDRfNVp4d0VTbmNabVBlem5VVWRIUlYwUmhicDdXSDI2dTVVdGZjNUFweVpYVHJYVGcwcHBJVlNKMTRLSkZ0cG05NlVKaE10MzRkU0JZUXU3cFURxRmx5THV2NW14UW9IUTVya2VxRG8weF9vOTNyd2UyT054UktjZkRVTXhBMGpOMlA3NTVUdk5UeTB6WkJKNGlLem12NmhHX3FheVl2TU1jZGJ4aENYcFlPMlRBS2VJSjE1aTVFaVVnZUU5Sk1qaEdUSmZjaUpTZ0hkLVlZWHB1NW9zcV9jTGw4UExaU0t5UDJKRTR4ZkVCZl8wZHBsT29ocE5FNVFhaGV4bWVsYWVYVnB6UGhXTDVFZkFmOUtTdHo3bGxCZEJIR0w2Y3RTdEFYOVRhLXdnM1Q3a1RmSXhpT2NWUnBRVWxKSDRobGpzdkNuQ2pyOGFQRFZVTjFTVjFY0X_5SVY1Rl_zR1VtMnJGQlZvblpGWDdicEFJem91ZTlaczBURUxKZXlqSzlpX3ByQmdRb0t4c09Ld0ZXR215Qm4yeUpqd0xxeFdNSHQ4ZWM3SWY2V29Nb1Z4aWp0ODMxTW5LaDVfcjFEcjlXMnRrZXhOMnExbVFpalYzSDk2ZnVJREJGT2dhaW9DXzFBdUF2TGJQZlI3dWpSaGYxX09wQXJnaFNpU21xcGp5ZDc3UHgtZmswak9VdUhkMzhsdV93TG1ZSmtCZE5GZTQwMnF3REhJLW1pRWRjRC1SRHJCSm9SRFB3TTFnYnA4OGt5YndHdWZRUmQyN0ZyUjZpV0c5RDVzTUgybUYwcDZBd2pCejhsQ0JTMEtNY25SWWYwdGlWQ0QwUFhndXlsZ0RacWFaQUVqZUw3ZkI3UnVyYm8yakZfbURTellEd2M1VWc1OUdKbHl3OU1NUi1XaXJES1otaWk3S3VWRm94RXZZbi01ZC1vVVdKb3RUZklzaGdJZzA4QmVJSG81OUZjRHJtYU0xYjRTSVl0U21zYWpuRGI4NDJiUEFHeHBDR1ZBVXRSVlpxWHlyWU1VUnZIVmhKN2twV0hBVER5UnJ6RDdTQVFnMkNnS2tJRU9xV1JIYkIxOFFGVk1KQm5uRFM2V3BhenY1dUtjTmFFOEwtSzNxc3VDdmhSYUNTbm9BdTN2Sm5JYk1vZmRoU1FNdjhycl9Sdkx0WjZMR1ZncVBHa1JialpyeTNzb1JobzhfMEZYbVhXVHREdFliZkdBTVZXZW9DSEs0M19tMzN0MzJIZ1VBWG9zZ3gw\",\"frx_context_from_www\":\"{\\\"location\\\":\\\"ig_profile\\\",\\\"entry_point\\\":\\\"chevron_button\\\",\\\"session_id\\\":\\\"b6f2fe68-e6c2-402d-ba61-fa32742586c3\\\",\\\"tags\\\":[\\\"ig_report_account\\\",\\\"ig_its_inappropriate\\\",\\\"violence_hate_or_exploitation\\\"],\\\"object\\\":\\\"{\\\\\\\"user_id\\\\\\\":\\\\\\\""+repr(USER_E)+"\\\\\\\"}\\\",\\\"reporter_id\\\":17841477249253541,\\\"responsible_id\\\":17841402263455874,\\\"locale\\\":\\\"ar_AR\\\",\\\"app_platform\\\":1,\\\"extra_data\\\":{\\\"container_module\\\":\\\"profilePage\\\",\\\"app_version\\\":\\\"None\\\",\\\"is_dark_mode\\\":null,\\\"app_id\\\":1217981644879628,\\\"sentry_feature_map\\\":\\\"Jv7di5q+BBgNMzcuMjM2LjEwLjEwMxhvTW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDEwOyBLKSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTQwLjAuMC4wIE1vYmlsZSBTYWZhcmkvNTM3LjM2GAVhcl9BUhwYIGE1OTk3Yzc1ZGE0ZmExNWUyYjZkNzFiMGQ5MDY3MWRhGCBmYzE0NTBiNTg5MDViOTVmNWU1YTM2YWRiZTAxYzRjOBggYzFlYzY5ZDc5NmMzYzU4ZDQ4MmI5OTFlNWM2ZmViZjIYIDczZjk2ZThjZmZmNzZkNjEwZjA0Njg2MDFjNTk1MDM3IRggZDUzOTZjNjZhMjM0NDBkOWYxMDQ5MjJhN2U1NGNiODAYJHQxM2QzMTExaDJfZThmMWU3ZTc4ZjcwXzVhYzcxOTdkZjlkMgA8LBgcYUp5MHV3QUJBQUdoTXpnY2hadUNSQ1dCdEJmSxbw6Y\\\\\\/ClGYAHBUCKwGIEWRpc3BsYXlfc2l6ZV90eXBlH0RldmljZVR5cGVCeURpc3BsYXlTaXplLlVOS05PV04AIjw5FQAZFQA5FQAAGCAwOWFmZmNiNzFmNGM0Mzg2ODkzZThjNzMxNDVmNjBjZBUCERIYEDEyMTc5ODE2NDQ4Nzk2MjgcFpjbm4bCsLI\\\\\\/GEAzNzQ4YTZmMmQ5NmY0OTM2YTM0ZmViZjI1MWNjMmM1YWU0MjBjNGRlMGM3ZDk2NGVkY2JjZmJhNTkwYTUzNjMyGBk3NzA2ODMzNDk3NToyMDoxNzU3MjI3NTU0ABwVBAASKChodHRwczovL3d3dy5pbnN0YWdyYW0uY29tL3NoZXJpbnNiZWF1dHkvGA5YTUxIdHRwUmVxdWVzdAAWyoKum9SusT8oIy9hcGkvdjEvd2ViL3JlcG9ydHMvZ2V0X2ZyeF9wcm9tcHQvFigWxKjpiw1YATQYBVZBTElEAA==\\\",\\\"shopping_session_id\\\":null,\\\"logging_extra\\\":null,\\\"is_in_holdout\\\":null,\\\"preloading_enabled\\\":null},\\\"frx_feedback_submitted\\\":false,\\\"ufo_key\\\":\\\"ufo-3f1f7ad1-e14d-4742-b7c5-0893703561c8\\\",\\\"additional_data\\\":{\\\"is_ixt_session\\\":true,\\\"frx_validation_ent\\\":\\\"IGEntUser\\\"},\\\"profile_search\\\":false,\\\"screen_type\\\":\\\"frx_tag_selection_screen\\\",\\\"ent_has_music\\\":false,\\\"evidence_selections\\\":[],\\\"is_full_screen\\\":false}\"}",
              'selected_tag_types': "[\"violent_hateful_or_disturbing-credible_threat\"]",
              'frx_prompt_request_type': "2",
              'jazoest': "22668"
            }
            headers = {
              'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Mobile Safari/537.36",
              'x-ig-app-id': "1217981644879628",
              'x-requested-with': "XMLHttpRequest",
              'x-csrftoken': crf_tt,
              'Cookie': f"csrftoken={crf_tt}; sessionid={Sessionid}"
            }
            response = requests.post(url, data=payload, headers=headers).text
            if '"status":"ok"' in response:
                self.g+=1
                return True, f" [{self.g}] تم البلاغ بنجاح | الحساب: {Sessionid[:10]}..."
            else:
                return False, f" [!] خطأ في الجلسة: {response[:50]}"
        except Exception as e:
            return False, str(e)
														
    def lite_re(self,Sessionid:str,crf_tt:str,USER_E:str,)->any:
        try:
            url = f"https://i.instagram.com/users/{USER_E!r}/flag/"
            headers = {
                "User-Agent": "Mozilla/5.0",
                "Host": "i.instagram.com",
                "cookie": f"sessionid={Sessionid}",
                "X-CSRFToken":crf_tt,
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
            }
            data = f"source_name=&reason_id=5&frx_context="
            r3 = requests.post(url, headers=headers, data=data, allow_redirects=False).text
            return r3		
        except Exception as e:
            return str(e)

# --- إعدادات Streamlit ---
st.set_page_config(page_title="Dark Reporter gx1gx1", page_icon="gx1gx1", layout="centered")

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;} header {visibility: hidden;} footer {visibility: hidden;}
    .stApp { background-color: #000000; color: #ff0000; font-family: 'Courier New', monospace; }
    h1 { color: #ff0000; text-shadow: 0 0 10px #ff0000; text-align: center; }
    .stButton>button { background-color: #4a0000; color: white; border: 2px solid #ff0000; width: 100%; }
    input { background-color: #1a1a1a !important; color: #00ff00 !important; border: 1px solid #ff0000 !important; }
    .header-img { display: block; margin: auto; width: 50%; border-radius: 50%; border: 2px solid #ff0000; box-shadow: 0 0 15px #ff0000; }
    </style>
    """, unsafe_allow_html=True)

st.markdown(f'<img src="https://files.catbox.moe/qte6xo.jpg" class="header-img">', unsafe_allow_html=True)
st.markdown("<h1>نظام البلاغات gx1gx1</h1>", unsafe_allow_html=True)

OO = sin()
user_id_input = st.text_input("يوزر الضحية (USER >> )")
count_sessions = st.number_input("عدد الجلسات", min_value=1, step=1)
session_list = [st.text_input(f"Session {i+1}", key=f"s_{i}", type="password") for i in range(int(count_sessions))]
session_list = [s for s in session_list if s]

option = st.selectbox("نوع البلاغ:", ["-- اختر --", "بلاغ حساب", "بلاغ ستوري (Story)", "بلاغ لايت"])

if st.button("بدء الهجوم 🧨"):
    if user_id_input and session_list and option != "-- اختر --":
        try:
            crf_tt = OO.exit_csr()
            USER_E = OO.user_for_id(user_id_input)
            placeholder = st.empty()
            log_data = f"تم استهداف: {USER_E}\n"

            if option == "بلاغ ستوري (Story)":
                story_id = OO.wech_story(USER_E, session_list[0], crf_tt)
                if story_id:
                    for _ in range(50):
                        for sid in session_list:
                            _, res = OO.report_story_logic(sid, crf_tt, story_id)
                            log_data = f"{res}\n" + log_data
                            placeholder.text_area("النتائج", log_data, height=300)
                else: st.error("لا يوجد ستوري متاح.")
            
            elif option == "بلاغ حساب":
                for _ in range(50):
                    for sid in session_list:
                        _, res = OO.Send_Report(sid, crf_tt, USER_E)
                        log_data = f"{res}\n" + log_data
                        placeholder.text_area("النتائج", log_data, height=300)
            
            elif option == "بلاغ لايت":
                for sid in session_list:
                    res = OO.lite_re(sid, crf_tt, USER_E)
                    log_data = f"Lite Res: {res}\n" + log_data
                    placeholder.text_area("النتائج", log_data, height=300)
        except Exception as e: st.error(str(e))

