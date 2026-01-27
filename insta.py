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

# --- مصفوفة المعلومات الضخمة (50 دولة و 50 جهاز) ---
COUNTRIES_LIST = ["US", "GB", "DE", "FR", "JP", "KR", "BR", "IN", "RU", "CA", "AU", "SA", "AE", "EG", "TR", "IT", "ES", "NL", "MX", "ID", "MY", "SG", "TH", "VN", "PH", "PK", "BD", "ZA", "NG", "AR", "CO", "CL", "PE", "DZ", "MA", "TN", "LY", "IQ", "JO", "KW", "QA", "OM", "BH", "SE", "NO", "FI", "DK", "PL", "CZ", "HU"]

DEVICES_LIST = [
    f"Mozilla/5.0 (Linux; Android {random.randint(9,14)}; SM-G{random.randint(100,999)}F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(100,125)}.0.0.0 Mobile Safari/537.36" 
    for _ in range(50)
]

# --- الكود الأصلي الخاص بك (بدون حذف أي حرف أو دالة) ---
class sin:
    def __init__(self):
        self.g=0
        # جلب قائمة بروكسيات محدثة لتجنب أخطاء الاتصال
        try:
            r = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=5000&country=all&ssl=all&anonymity=all")
            self.proxies_pool = [p for p in r.text.splitlines() if p]
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
            # تدوير البيانات تلقائياً في كل محاولة
            px = random.choice(self.proxies_pool) if self.proxies_pool else None
            proxies = {"http": f"http://{px}", "https": f"http://{px}"} if px else None
            ua = random.choice(DEVICES_LIST)
            country = random.choice(COUNTRIES_LIST)

            url = "https://www.instagram.com/api/v1/web/reports/get_frx_prompt/"
            # الـ Payload الأصلي الخاص بك (بدون أي تعديل أو حذف)
            payload = {
              'container_module': "profilePage",
              'entry_point': "1",
              'location': "2",
              'object_id': f"{USER_E!r}",
              'object_type': "5",
              'context': "{\"tags\":[\"ig_report_account\",\"ig_its_inappropriate\",\"violence_hate_or_exploitation\"],\"ixt_context_from_www\":\"QVFZWlRaZldlWnlJVlRtRklPMmRrNEoyd1p5WWVVRG9jblN3Slhra2JXY210QmJPQXU2YnNEcG16SHpVaFJhZXVKcVN2eU9GS25ZR3Q0a3dfWDE0ODRjeXpLWlZrb1ZQaHd0dDYwQklWMjVUcTNua05FdldGY1A1Nk5SUE9YYXM2SXhiVnh1WlJROTdBS3ZWdzRDQzREdkt5R2dsOFNoamRpekphdmZfQUJKVlFhYktzbERuQmN3S2dxUkxBVHQ3MnhsVDZqZ19kY1poTHJjT1F2N0hFMkE0dl9lQ3hINkl0aGVrU0RuNEdDbGtIamR1SGhwRm93ZnpxOXNxTVZMYUpZTGFVR0FnNEk2VnFjUGRJZGVjSklfOHl6azRsb1ZfNUhxa2lGWVlMaE5SdG9ZQzYtVjFhS05Wd2JVMkNvem5QMmVuT0JnUjdzblFJTEY0OEl0dzhaXzdsaXFXWlJoTDBiNDdfNHRxYS1iOUtjd3BQTjByZjMzcDRqZ0VIZkdZV2hjVXJmYVlLc21RQXJJWmFKOWtoRE9WZ2Y2LWJpUEt3T1BrdTU2YUZoUjV5bFBLWnJPQXBSQTlvdVdEcUJ3UmtzVkd3ZHJNcVdWUHJ5bGx4WWtzMm82ZlJOWWlRcl9WeHZBREpDRUxVamZnTkhEdEFjN0lzOFFLZlkzTGVkOHpXN1dBTXB1UkZhd09LcFZaSjNMQUpKZi13RmNLNXU3ajFrNi1DdHg3ZUVqUi1VTzQ0YXUtcHFySGM4VGRkaEtFdXh5cjhsUC1pb0s3SVhaWFBUd3lleFBQajlLcC1FWUNfanMwTjdKMkc5VWxsV2dzZ2UxZ3VaT0VXaGc3UklVUjN0Y2tldGhSTUR2X0xvd2FJewNDMHFmbWhEZmhubGpRejFsLTVhYTAyREhVYnpvX2ltNUllRTJBVXJ0eWpGVHdtTWxwS2l3ek51VEFHV2tPbVdxME56WHBMajVwa1hDRldBeGpoTUVDUU5BZmszR2o2NmVKeVBwakp5Q1FsUzEwUkFsUjc0YmRSSEpLTzN6MHNFMFMwTFNxQUVHZU5nZ1ZNbDJKZVJWU2hpRjVlX3NYb2NLdDVVTVJ4RDdVU25zelBxTXF4XzZNa3c1cnlPMVk5MDBNYmU4dmEtdTBLU1NqR3dBMkl6YXp4MFdRaHdEN0pfMG5HOG1VTG1CMWhmT2RUbUJlRllYbWhfTUZhTlFWU0ZObHpBMEpSaDBVT29veEg5bVFBOWJPRXVickd4Nl8tYmZwem5EZWZLNUxFX1V2djlGdlF0aE5BSFZHTHJqbmFoUEpfMThwdndqUTRRV3BuQnBNdFJ3NDdTaEU1YktzVEl3THQ2eVVXMWpHWFBTQUo5LUxvcV9lVmVqU3FZdDdkY0owaVgyNlo3SVhjOExiOWh6VWQyNlJMQXZFZ3daZTNBd3NoN2lYRlRYclVIUV9iQ0E2NUZIZVZHV0RJNHNyRHZzVi1NTDBtWUkxSUxLNVpVNE4ySURXOV9HaHVlaDhhbDZBMnIzN3BRdU5TSEtYRkpQNnZoU0J3U0xuTUNhbDZQVmpEZVBRc1RjT2hfRGJubWZmWXhGeWRRLXB2VVRkdW5yOWxJelFzeHh3cldnd2hvNk5VTjRrc0Rpa0p1R0xvQkpmd0t6dHRJWnZIZkNsQmQ3ZjZrcmVyZk53VHRPSk9kR0RFcWUta1QydmRBOTlRUl9QNVhsdXptdzJSeW40bko3N1NVMm5aQ1dJa3BTNUoyNFhOU0x1TmRJTjlMSXdYSWNISDB2WHBNOWNId0Zqd1Fhc2pJbXY1RWwyQ08wYXhvV1BIMW9MNGlZdzlBenZCT2pZT29zR19oOUU2eDg2VXBlbWJJNXhTUjRjeDhEZU1kNGxaMXkzMkNnWXZHZmVCQzVIR1lwczJGRnJLOFJRUnJhV2k3UVZnMi1uUl9tTVo4V0ZlQkowdkZqaFlqSWN3cndUd20wTjhwd0IwUXkwd1RkbVVRZzZSbkdrWjFUdktBeFlaVFhwM0Nud0dENmdDZFpVdE9OOHJlWjE1WGhoYkp5NjQ4Mi1sbE1mcWloUU84UzE5VnBkekNrbFBuNWFkU1MyejducmFGRUhnOUdPcm9EYWNxSGU2WmdULWMxSmo2QXdFdlV1OGpTU2YtZ1U3YTF5VlpWZlhaRTFjVGRuYnI2WUEyX0xCckYzWFdZejNvWEx1SkpXRWZQTEpFVVBJNjBMUmtvdzZrMWdBRUNxd1RNa0liWHV6R3paZHZmbVlAzUohmTI3ejJZQjE5ODFkNmI2ZWtPY3pZT200R1E1Z3pBZTFJcHBLQ3Z4X2NZSHBzUkVnUWFLSm9iQ2tpUG9SZWVvMzhtZ2pjdElycThkLW9hczdYeGZZQVc4MHhCcld1M3ZmQmNOQ01rWlZkT2ZfTzRCVEU3ck5hVG12c2QySWFRLUNwemlqWUc2LTk1WXJMWWd4bkliUmNObHJOOXF1bXZfWEkzSWpPenhpRVNnbFA2NEVxcVJiam5hdGlqbV8xSkpsNmVhSGFMTzVuLVZ3bDQxdURQY2lvTWJUbDNrUWhtMFlOMDZWNjNnVTJMUXhvME9BTVFCeUstSjVPWDkwQXR2dGhrN0Radlp2dFB5eVhDYmNoaGIxVUdDeU5rdW1PM1BlSVBtcHZmd2NPM0pMMDE1ZzZGNTgyTEJHamlJdndDWEJLaXh0Vi1xRkNpWndkRy1rRXpoX1Zwc1R6TmpIbHYxLXNJc2d3QmJhRmwxM2d3dlNqSExvVnBDeFRFM0Y4X2NqZHgtdS1WaGNGNlF2ZkYtMzBlTWtOdDI2TVkyWVpyV0tZb1RUOEhnZXZob2I2Yk95MFhEWU1FcTVSNWt4SE55em00ZXlsU1FHVkxEODhGbDd0WU0xN3c3TTRVbTM0YkRieHEtUmg5aFFDdDBHOWhBUVhnQnFyZXZzdXRoLU02eElHak5PQXRqSmhDOGJfY2U0V3ZQeVRrXzVWMWdyWmhZX1BtWk1TdFZDdHpUSmFlRVdHd1o3ZmZwS0doenlfcVFrVGVJcFVTdDdfcmhuRENUTEs0eDJMVlF3V25fN1BjZ0tzMFBnVnRydWN0RWFYQlRTMzM3ZFEyWmhuUGU3VlhxZHRIbGtKM1E3ZXBpOXZlaUdBemgtOHdjTTV1UGJ4eWt0aWJUWFZJR2U5aGI2TkZNUEdvWUlFcmNvbFpoV2Rpakp2ay1OQl9TUTBSMEY0VFY4am9WT1oxd2d3ckFUbmIzMkhVTW1JbHBTbUt4elE1TmJpVDRfNVp4d0VTbmNabVBlem5VVWRIUlYwUmhicDdXSDI2dTVVdGZjNUFweVpYVHJYVGcwcHBJVlNKMTRLSkZ0cG05NlVKaE10MzRkU0JZUXU3cFURxRmx5THV2NW14UW9IUTVya2VxRG8weF9vOTNyd2UyT054UktjZkRVTXhBMGpOMlA3NTVUdk5UeTB6WkJKNGlLem12NmhHX3FheVl2TU1jZGJ4aENYcFlPMlRBS2VJSjE1aTVFaVVnZUU5Sk1qaEdUSmZjaUpTZ0hkLVlZWHB1NW9zcV9jTGw4UExaU0t5UDJKRTR4ZkVCZl8wZHBsT29ocE5FNVFhaGV4bWVsYWVYVnB6UGhXTDVFZkFmOUtTdHo3bGxCZEJIR0w2Y3RTdEFYOVRhLXdnM1Q3a1RmSXhpT2NWUnBRVWxKSDRobGpzdkNuQ2pyOGFQRFZVTjFTVjFY0X_5SVY1Rl_zR1VtMnJGQlZvblpGWDdicEFJem91ZTlaczBURUxKZXlqSzlpX3ByQmdRb0t4c09Ld0ZXR215Qm4yeUpqd0xxeFdNSHQ4ZWM3SWY2V29Nb1Z4aWp0ODMxTW5LaDVfcjFEcjlXMnRrZXhOMnExbVFpalYzSDk2ZnVJREJGT2dhaW9DXzFBdUF2TGJQZlI3dWpSaGYxX09wQXJnaFNpU21xcGp5ZDc3UHgtZmswak9VdUhkMzhsdV93TG1ZSmtCZE5GZTQwMnF3REhJLW1pRWRjRC1SRHJCSm9SRFB3TTFnYnA4OGt5YndHdWZRUmQyN0ZyUjZpV0c5RDVzTUgybUYwcDZBd2pCejhsQ0JTMEtNY25SWWYwdGlWQ0QwUFhndXlsZ0RacWFaQUVqZUw3ZkI3UnVyYm8yakZfbURTellEd2M1VWc1OUdKbHl3OU1NUi1XaXJES1otaWk3S3VWRm94RXZZbi01ZC1vVVdKb3RUZklzaGdJZzA4QmVJSG81OUZjRHJtYU0xYjRTSVl0U21zYWpuRGI4NDJiUEFHeHBDR1ZBVXRSVlpxWHlyWU1VUnZIVmhKN2twV0hBVER5UnJ6RDdTQVFnMkNnS2tJRU9xV1JIYkIxOFFGVk1KQm5uRFM2V3BhenY1dUtjTmFFOEwtSzNxc3VDdmhSYUNTbm9BdTN2Sm5JYk1vZmRoU1FNdjhycl9Sdkx0WjZMR1ZncVBHa1JialpyeTNzb1JobzhfMEZYbVhXVHREdFliZkdBTVZXZW9DSEs0M19tMzN0MzJIZ1VBWG9zZ3gwIiwiaXh0X2NvbnRleHRfZm9yX3NlcnZlciI6IkFRWlpUWmZXZVp5SVZUbUZZTzJkazRKMndaeVllVURvY25Td0pYa2tiV2NtdEJiT0F1NmJzRHBtekh6VWhSYWV1SnFTdnVPRktuWUd0NGt3X1gxNDg0Y3l6S1pWa29WUGh3dHQ2MEJJVjI1VHEzbmtORXZXRmNQNTZOUlBPWGFzNkl4YlZ4dVpSUTk3QUt2Vnc0QzREdkt5R2dsOFNoamRpekphdmZfQUJKVlFhYktzbERuQmN3S2dxUkxBVHQ3MnhsVDZqZ19kY1poTHJjT1F2N0hFMkE0dl9lQ3hINkl0aGVrU0RuNEdDbGtIamR1SGhwRm93ZnpxOXNxTVZMYUpZTGFVR0FnNEk2VnFjUGRJZGVjSklfOHl6azRsb1ZfNUhxa2lGWVlMaE5SdG9ZQzYtVjFhS05Wd2JVMkNvem5QMmVuT0JnUjdzblFJTEY0OEl0dzhaXzdsaXFXWlJoTDBiNDdfNHRxYS1iOUtjd3BQTjByZjMzcDRqZ0VIZkdZV2hjVXJmYVlLc21RQXJJWmFKOWtoRE9WZ2Y2LWJpUEt3T1BrdTU2YUZoUjV5bFBLWnJPQXBSQTlvdVdEcUJ3UmtzVkd3ZHJNcVdWUHJ5bGx4WWtzMm82ZlJOWWlRcl9WeHZBREpDRUxVamZnTkhEdEFjN0lzOFFLZlkzTGVkOHpXN1dBTXB1UkZhd09LcFZaSjNMQUpKZi13RmNLNXU3ajFrNi1DdHg3ZUVqUi1VTzQ0YXUtcHFySGM4VGRkaEtFdXh5cjhsUC1pb0s3SVhaWFBUd3lleFBQajlLcC1FWUNfanMwTjdKMkc5VWxsV2dzZ2UxZ3VaT0VXaGc3UklVUjN0Y2tldGhSTUR2X0xvd2FJewNDMHFmbWhEZmhubGpRejFsLTVhYTAyREhVYnpvX2ltNUllRTJBVXJ0eWpGVHdtTWxwS2l3ek51VEFHV2tPbVdxME56WHBMajVwa1hDRldBeGpoTUVDUU5BZmszR2o2NmVKeVBwakp5Q1FsUzEwUkFsUjc0YmRSSEpLTzN6MHNFMFMwTFNxQUVHZU5nZ1ZNbDJKZVJWU2hpRjVlX3NYb2NLdDVVTVJ4RDdVU25zelBxTXF4XzZNa3c1cnlPMVk5MDBNYmU4dmEtdTBLU1NqR3dBMkl6YXp4MFdRaHdEN0pfMG5HOG1VTG1CMWhmT2RUbUJlRllYbWhfTUZhTlFWU0ZObHpBMEpSaDBVT29veEg5bVFBOWJPRXVickd4Nl8tYmZwem5EZWZLNUxFX1V2djlGdlF0aE5BSFZHTHJqbmFoUEpfMThwdndqUTRRV3BuQnBNdFJ3NDdTaEU1YktzVEl3THQ2eVVXMWpHWFBTQUo5LUxvcV9lVmVqU3FZdDdkY0owaVgyNlo3SVhjOExiOWh6VWQyNlJMQXZFZ3daZTNBd3NoN2lYRlRYclVIUV9iQ0E2NUZIZVZHV0RJNHNyRHZzVi1NTDBtWUkxSUxLNVpVNE4ySURXOV9HaHVlaDhhbDZBMnIzN3BRdU5TSEtYRkpQNnZoU0J3U0xuTUNhbDZQVmpEZVBRc1RjT2hfRGJubWZmWXhGeWRRLXB2VVRkdW5yOWxJelFzeHh3cldnd2hvNk5VTjRrc0Rpa0p1R0xvQkpmd0t6dHRJWnZIZkNsQmQ3ZjZrcmVyZk53VHRPSk9kR0RFcWUta1QydmRBOTlRUl9QNVhsdXptdzJSeW40bko3N1NVMm5aQ1dJa3BTNUoyNFhOU0x1TmRJTjlMSXdYSWNISDB2WHBNOWNId0Zqd1Fhc2pJbXY1RWwyQ08wYXhvV1BIMW9MNGlZdzlBenZCT2pZT29zR19oOUU2eDg2VXBlbWJJNXhTUjRjeDhEZU1kNGxaMXkzMkNnWXZHZmVCQzVIR1lwczJGRnJLOFJRUnJhV2k3UVZnMi1uUl9tTVo4V0ZlQkowdkZqaFlqSWN3cndUd20wTjhwd0IwUXkwd1RkbVVRZzZSbkdrWjFUdktBeFlaVFhwM0Nud0dENmdDZFpVdE9OOHJlWjE1WGhoYkp5NjQ4Mi1sbE1mcWloUU84UzE5VnBkekNrbFBuNWFkU1MyejducmFGRUhnOUdPcm9EYWNxSGU2WmdULWMxSmo2QXdFdlV1OGpTU2YtZ1U3YTF5VlpWZlhaRTFjVGRuYnI2WUEyX0xCckYzWFdZejNvWEx1SkpXRWZQTEpFVVBJNjBMUmtvdzZrMWdBRUNxd1RNa0liWHV6R3paZHZmbVlAzUohmTI3ejJZQjE5ODFkNmI2ZWtPY3pZT200R1E1Z3pBZTFJcHBLQ3Z4X2NZSHBzUkVnUWFLSm9iQ2tpUG9SZWVvMzhtZ2pjdElycThkLW9hczdYeGZZQVc4MHhCcld1M3ZmQmNOQ01rWlZkT2ZfTzRCVEU3ck5hVG12c2QySWFRLUNwemlqWUc2LTk1WXJMWWd4bkliUmNObHJOOXF1bXZfWEkzSWpPenhpRVNnbFA2NEVxcVJiam5hdGlqbV8xSkpsNmVhSGFMTzVuLVZ3bDQxdURQY2lvTWJUbDNrUWhtMFlOMDZWNjNnVTJMUXhvME9BTVFCeUstSjVPWDkwQXR2dGhrN0Radlp2dFB5eVhDYmNoaGIxVUdDeU5rdW1PM1BlSVBtcHZmd2NPM0pMMDE1ZzZGNTgyTEJHamlJdndDWEJLaXh0Vi1xRkNpWndkRy1rRXpoX1Zwc1R6TmpIbHYxLXNJc2d3QmJhRmwxM2d3dlNqSExvVnBDeFRFM0Y4X2NqZHgtdS1WaGNGNlF2ZkYtMzBlTWtOdDI2TVkyWVpyV0tZb1RUOEhnZXZob2I2Yk95MFhEWU1FcTVSNWt4SE55em00ZXlsU1FHVkxEODhGbDd0WU0xN3c3TTRVbTM0YkRieHEtUmg5aFFDdDBHOWhBUVhnQnFyZXZzdXRoLU02eElHak5PQXRqSmhDOGJfY2U0V3ZQeVRrXzVWMWdyWmhZX1BtWk1TdFZDdHpUSmFlRVdHd1o3ZmZwS0doenlfcVFrVGVJcFVTdDdfcmhuRENUTEs0eDJMVlF3V25fN1BjZ0tzMFBnVnRydWN0RWFYQlRTMzM3ZFEyWmhuUGU3VlhxZHRIbGtKM1E3ZXBpOXZlaUdBemgtOHdjTTV1UGJ4eWt0aWJUWFZJR2U5aGI2TkZNUEdvWUlFcmNvbFpoV2Rpakp2ay1OQl9TUTBSMEY0VFY4am9WT1oxd2d3ckFUbmIzMkhVTW1JbHBTbUt4elE1TmJpVDRfNVp4d0VTbmNabVBlem5VVWRIUlYwUmhicDdXSDI2dTVVdGZjNUFweVpYVHJYVGcwcHBJVlNKMTRLSkZ0cG05NlVKaE10MzRkU0JZUXU3cFURxRmx5THV2NW14UW9IUTVya2VxRG8weF9vOTNyd2UyT054UktjZkRVTXhBMGpOMlA3NTVUdk5UeTB6WkJKNGlLem12NmhHX3FheVl2TU1jZGJ4aENYcFlPMlRBS2VJSjE1aTVFaVVnZUU5Sk1qaEdUSmZjaUpTZ0hkLVlZWHB1NW9zcV9jTGw4UExaU0t5UDJKRTR4ZkVCZl8wZHBsT29ocE5FNVFhaGV4bWVsYWVYVnB6UGhXTDVFZkFmOUtTdHo3bGxCZEJIR0w2Y3RTdEFYOVRhLXdnM1Q3a1RmSXhpT2NWUnBRVWxKSDRobGpzdkNuQ2pyOGFQRFZVTjFTVjFY0X_5SVY1Rl_zR1VtMnJGQlZvblpGWDdicEFJem91ZTlaczBURUxKZXlqSzlpX3ByQmdRb0t4c09Ld0ZXR215Qm4yeUpqd0xxeFdNSHQ4ZWM3SWY2V29Nb1Z4aWp0ODMxTW5LaDVfcjFEcjlXMnRrZXhOMnExbVFpalYzSDk2ZnVJREJGT2dhaW9DXzFBdUF2TGJQZlI3dWpSaGYxX09wQXJnaFNpU21xcGp5ZDc3UHgtZmswak9VdUhkMzhsdV93TG1ZSmtCZE5GZTQwMnF3REhJLW1pRWRjRC1SRHJCSm9SRFB3TTFnYnA4OGt5YndHdWZRUmQyN0ZyUjZpV0c5RDVzTUgybUYwcDZBd2pCejhsQ0JTMEtNY25SWWYwdGlWQ0QwUFhndXlsZ0RacWFaQUVqZUw3ZkI3UnVyYm8yakZfbURTellEd2M1VWc1OUdKbHl3OU1NUi1XaXJES1otaWk3S3VWRm94RXZZbi01ZC1vVVdKb3RUZklzaGdJZzA4QmVJSG81OUZjRHJtYU0xYjRTSVl0U21zYWpuRGI4NDJiUEFHeHBDR1ZBVXRSVlpxWHlyWU1VUnZIVmhKN2twV0hBVER5UnJ6RDdTQVFnMkNnS2tJRU9xV1JIYkIxOFFGVk1KQm5uRFM2V3BhenY1dUtjTmFFOEwtSzNxc3VDdmhSYUNTbm9BdTN2Sm5JYk1vZmRoU1FNdjhycl9Sdkx0WjZMR1ZncVBHa1JialpyeTNzb1JobzhfMEZYbVhXVHREdFliZkdBTVZXZW9DSEs0M19tMzN0MzJIZ1VBWG9zZ3gw\",\"frx_context_from_www\":\"{\\\"location\\\":\\\"ig_profile\\\",\\\"entry_point\\\":\\\"chevron_button\\\",\\\"session_id\\\":\\\"b6f2fe68-e6c2-402d-ba61-fa32742586c3\\\",\\\"tags\\\":[\\\"ig_report_account\\\",\\\"ig_its_inappropriate\\\",\\\"violence_hate_or_exploitation\\\"],\\\"object\\\":\\\"{\\\\\\\"user_id\\\\\\\":\\\\\\\""+repr(USER_E)+"\\\\\\\"}\\\",\\\"reporter_id\\\":17841477249253541,\\\"responsible_id\\\":17841402263455874,\\\"locale\\\":\\\"ar_AR\\\",\\\"app_platform\\\":1,\\\"extra_data\\\":{\\\"container_module\\\":\\\"profilePage\\\",\\\"app_version\\\":\\\"None\\\",\\\"is_dark_mode\\\":null,\\\"app_id\\\":1217981644879628,\\\"sentry_feature_map\\\":\\\"Jv7di5q+BBgNMzcuMjM2LjEwLjEwMxhvTW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDEwOyBLKSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTQwLjAuMC4wIE1vYmlsZSBTYWZhcmkvNTM3LjM2GAVhcl9BUhwYIGE1OTk3Yzc1ZGE0ZmExNWUyYjZkNzFiMGQ5MDY3MWRhGCBmYzE0NTBiNTg5MDViOTVmNWU1YTM2YWRiZTAxYzRjOBggYzFlYzY5ZDc5NmMzYzU4ZDQ4MmI5OTFlNWM2ZmViZjIYIDczZjk2ZThjZmZmNzZkNjEwZjA0Njg2MDFjNTk1MDM3IRggZDUzOTZjNjZhMjM0NDBkOWYxMDQ5MjJhN2U1NGNiODAYJHQxM2QzMTExaDJfZThmMWU3ZTc4ZjcwXzVhYzcxOTdkZjlkMgA8LBgcYUp5MHV3QUJBQUdoTXpnY2hadUNSQ1dCdEJmSxbw6Y\\\\\\/ClGYAHBUCKwGIEWRpc3BsYXlfc2l6ZV90eXBlH0RldmljZVR5cGVCeURpc3BsYXlTaXplLlVOS05PV04AIjw5FQAZFQA5FQA5FQAAGCAwOWFmZmNiNzFmNGM0Mzg2ODkzZThjNzMxNDVmNjBjZBUCERIYEDEyMTc5ODE2NDQ4Nzk2MjgcFpjbm4bCsLI\\\\\\/GEAzNzQ4YTZmMmQ5NmY0OTM2YTM0ZmViZjI1MWNjMmM1YWU0MjBjNGRlMGM3ZDk2NGVkY2JjZmJhNTkwYTUzNjMyGBk3NzA2ODMzNDk3NToyMDoxNzU3MjI3NTU0ABwVBAASKChodHRwczovL3d3dy5pbnN0YWdyYW0uY29tL3NoZXJpbnNiZWF1dHkvGA5YTUxIdHRwUmVxdWVzdAAWyoKum9SusT8oIy9hcGkvdjEvd2ViL3JlcG9ydHMvZ2V0X2ZyeF9wcm9tcHQvFigWxKjpiw1YATQYBVZBTElEAA==\\\",\\\"shopping_session_id\\\":null,\\\"logging_extra\\\":null,\\\"is_in_holdout\\\":null,\\\"preloading_enabled\\\":null},\\\"frx_feedback_submitted\\\":false,\\\"ufo_key\\\":\\\"ufo-3f1f7ad1-e14d-4742-b7c5-0893703561c8\\\",\\\"additional_data\\\":{\\\"is_ixt_session\\\":true,\\\"frx_validation_ent\\\":\\\"IGEntUser\\\"},\\\"profile_search\\\":false,\\\"screen_type\\\":\\\"frx_tag_selection_screen\\\",\\\"ent_has_music\\\":false,\\\"evidence_selections\\\":[],\\\"is_full_screen\\\":false}\"}",
              'selected_tag_types': "[\"violent_hateful_or_disturbing-credible_threat\"]",
              'frx_prompt_request_type': "2",
              'jazoest': "22668"
            }
            headers = {
              'User-Agent': ua,
              'x-ig-app-id': "1217981644879628",
              'x-requested-with': "XMLHttpRequest",
              'x-csrftoken': crf_tt,
              'Cookie': f"csrftoken={crf_tt}; sessionid={Sessionid}"
            }
            response = requests.post(url, data=payload, headers=headers, proxies=proxies, timeout=15).text
            if '"status":"ok"' in response:
                self.g+=1
                return True, f" [{self.g}] تم البلاغ بنجاح | الدولة: {country} | IP: {px}"
            else:
                return False, f" [!] خطأ استجابة: {response[:40]}"
        except Exception as e:
            return False, f" [!] خطأ اتصال (جاري التغيير): {str(e)[:30]}"
														
    def lite_re(self,Sessionid:str,crf_tt:str,USER_E:str,)->any:
        try:
            px = random.choice(self.proxies_pool) if self.proxies_pool else None
            proxies = {"http": f"http://{px}", "https": f"http://{px}"} if px else None
            
            # تصحيح رابط لايت لتجنب أخطاء port=4
            url = f"https://i.instagram.com/api/v1/users/{USER_E}/flag/"
            headers = {
                "User-Agent": random.choice(DEVICES_LIST),
                "Host": "i.instagram.com",
                "cookie": f"sessionid={Sessionid}",
                "X-CSRFToken":crf_tt,
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
            }
            data = f"source_name=&reason_id=5&frx_context="
            r3 = requests.post(url, headers=headers, data=data, proxies=proxies, allow_redirects=False, timeout=15).text
            return r3		
        except Exception as e:
            return str(e)

# --- واجهة Streamlit (نفس تصميمك تماماً) ---
st.set_page_config(page_title="Dark Instagram Reporter", page_icon="gx1gx1", layout="centered")

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;} header {visibility: hidden;} footer {visibility: hidden;}
    .stApp { background-color: #000000; color: #ff0000; font-family: 'Courier New', monospace; }
    h1 { color: #ff0000; text-shadow: 0 0 10px #ff0000; text-align: center; }
    .stButton>button { background-color: #4a0000; color: white; border: 2px solid #ff0000; width: 100%; border-radius: 10px; }
    .header-img { display: block; margin: auto; width: 45%; border-radius: 50%; border: 2px solid #ff0000; box-shadow: 0 0 15px #ff0000; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown(f'<img src="https://files.catbox.moe/qte6xo.jpg" class="header-img">', unsafe_allow_html=True)
st.markdown("<h1>نظام البلاغات المظلم gx1gx1</h1>", unsafe_allow_html=True)

OO = sin()

user_id = st.text_input("أدخل يوزر الضحية (USER )", "")
count_sessions = st.number_input("عدد الجلسات (Sessions)", min_value=1, step=1)

session_list = []
for i in range(int(count_sessions)):
    sid = st.text_input(f"أدخل sessionid رقم {i+1}", key=f"sid_{i}", type="password")
    if sid: session_list.append(sid)

option = st.selectbox("نوع البلاغ المطور:", ["-- اختر --", "بلاغ إنستجرام", "بلاغ إنستجرام لايت"])

if st.button("بدء الـهجوم "):
    if not user_id or not session_list:
        st.error("أدخل البيانات المطلوبة!")
    elif option == "-- اختر --":
        st.warning("اختر النوع.")
    else:
        try:
            with st.spinner('جاري فحص الهدف وتفعيل البروكسي...'):
                crf_tt = OO.exit_csr()
                USER_E = OO.user_for_id(user_id)
            
            st.success(f"تم العثور على هدفك بنجاح: {USER_E}")
            placeholder = st.empty()
            log_data = ""

            for i in range(50): # 50 محاولة تلقائية ببيانات مختلفة
                for current_sid in session_list:
                    if option == "بلاغ إنستجرام":
                        _, result = OO.Send_Report(current_sid, crf_tt, USER_E)
                        log_data = f"المحاولة {i+1}: {result}\n" + log_data
                    else:
                        res_lite = OO.lite_re(current_sid, crf_tt, USER_E)
                        log_data = f"المحاولة {i+1} [Lite]: {res_lite[:60]}\n" + log_data
                    
                    placeholder.text_area("سجل البلاغات", value=log_data, height=400)
                    time.sleep(1) # تأخير بسيط لضمان ثبات الاتصال

        except Exception as e:
            st.error(f"خطأ: {e}")

