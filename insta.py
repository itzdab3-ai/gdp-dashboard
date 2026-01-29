import os
import subprocess
import sys

# قائمة المكتبات المطلوبة
required_packages = [
    "requests",
    "user_agent",
    "pyfiglet"
]

# دالة لتثبيت مكتبة واحدة
def install(package):
    # تم إضافة محاولة (try) هنا لمنع الكود من التوقف إذا كان السيرفر يمنع التثبيت اليدوي
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    except Exception:
        pass 

# محاولة تثبيت كل مكتبة إن لم تكن موجودة
for pkg in required_packages:
    try:
        if pkg == "user_agent":
            import user_agent
        elif pkg == "pyfiglet":
            import pyfiglet
        else:
            __import__(pkg)
    except ImportError:
        print(f"[!] Installing {pkg} ...")
        install(pkg)

# بعد التثبيت، استيراد جميع المكتبات كما طلبت
import re
import requests
import time
import sys
import os
import random
from os import path
from concurrent.futures import ThreadPoolExecutor, as_completed
from user_agent import generate_user_agent
import pyfiglet

print("\n✅ جميع المكتبات جاهزة للاستخدام!")

R = "\033[1;31m" # احمر
G = "\033[1;32m" # اخضر
Y = "\033[1;33m" # اصفر
B = "\033[1;34m" # ازرق
C = "\033[1;97m"  # ابيض
rest = "\033[0m"  # استرجاع اللون الى الون الاصلي

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# --- الواجهة المخيفة الجديدة ---
def scary_interface():
    clear()
    # عرض الصورة المطلوبة مع إطار مميز
    print(f"{R}╔════════════════════════════════════════════════════════════════╗")
    print(f"{R}║ {C}IMAGE LINK: https://files.catbox.moe/8z2xdh.jpg {R}║")
    print(f"{R}╚════════════════════════════════════════════════════════════════╝")
    
    banner = pyfiglet.figlet_format("DEATH  TOOL", font="slant")
    print(f"{R}{banner}")
    print(f"{Y}      [!] WARNING: YOU ARE ENTERING THE DARK ZONE [!]{rest}\n")
    print(f"{R}      -- Created with Horror -- Keep your soul safe --{rest}\n")

def blink_ascii(sd):
    art = sd + """GX1GX1"""

    for _ in range(4):  # يومض 4 مرات  
        clear()  
        print(f"\033[91m{art}\033[0m")  # أحمر  
        time.sleep(0.4)  
        clear()  
        print(f"\033[92m{art}\033[0m")  # أخضر  
        time.sleep(0.4)

# مثال للتشغيل
sd = ""
blink_ascii(sd)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_green(msg):
    print(f"\033[1;32m{msg}\033[0m")

def print_red(msg):
    print(f"\033[1;31m{msg}\033[0m")

def print_white(msg):
    print(f"\033[1;37m{msg}\033[0m")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_banner():
    scary_interface() # استخدام الواجهة الجديدة

def print_option(number, text):
    print(f"\033[44m \033[92m[{number}]\033[97m {text} \033[0m")

def print_exit_option(number, text):
    print(f"\033[41m \033[92m[{number}]\033[97m {text} \033[0m")

def show_menu():
    print_option("1", "الإبلاغ عن محتوى")
    print_option("2", "البريد العشوائي/المضايقة")
    print_option("3", "دون السن القانونية (أقل من 13)")
    print_option("4", "معلومات مزيفة")
    print_option("5", "خطاب كراهية")
    print_option("6", "محتوى إباحي")
    print_option("7", "منظمات إرهابية")
    print_option("8", "إيذاء النفس")
    print_option("9", "مضايقة (شخص أعرفه)")
    print_option("10", "عنف")
    print_option("12", "بلاغات عشوائية")
    print_option("13", "بلاغات عبر بروكسي")
    print_option("14", "احتيال/نصب")
    print_option("15", "تحديات خطيرة")
    print_option("16", "الإبلاغ عن سبام")
    print_exit_option("0", "خروج من الأداة")
    print("")  # سطر فارغ

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

# قائمة الأجهزة (50 جهاز)
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

# قائمة الدول (50 دولة)
countries = [
    "SA", "US", "GB", "CA", "AU", "DE", "FR", "IT", "ES", "BR",
    "RU", "CN", "JP", "KR", "IN", "ID", "TR", "NL", "SE", "NO",
    "DK", "FI", "PL", "UA", "CZ", "RO", "HU", "GR", "PT", "BE",
    "CH", "AT", "IE", "SG", "MY", "TH", "VN", "PH", "MX", "AR",
    "CL", "CO", "PE", "ZA", "EG", "NG", "KE", "MA", "DZ", "AE"
]

def get_report_params(r_type, target_ID, session):
    base_url = 'https://www.tiktok.com/aweme/v1/aweme/feedback/'
    device = random.choice(devices)
    country = random.choice(countries)
    region = country
    priority_region = country
    current_region = country
    common = (f"?aid=1233&app_name=tiktok_web&device_platform=web_mobile"
              f"&region={region}&priority_region={priority_region}&os=ios&"
              f"cookie_enabled=true&screen_width=375&screen_height=667&"
              f"browser_language=en-US&browser_platform=iPhone&"
              f"browser_name=Mozilla&browser_version=5.0+(iPhone;+CPU+iPhone+OS+15_1+like+Mac+OS+X)+"
              f"AppleWebKit/605.1.15+(KHTML,+like+Gecko)+InspectBrowser&"
              f"browser_online=true&app_language=ar&timezone_name=Asia%2FRiyadh&"
              f"is_page_visible=true&focus_state=true&is_fullscreen=false")
    params = {  
        1: {"reason": "399"}, 2: {"reason": "310"}, 3: {"reason": "317"},  
        4: {"reason": "3142"}, 5: {"reason": "306"}, 6: {"reason": "308"},  
        7: {"reason": "3011"}, 8: {"reason": "3052"}, 9: {"reason": "3072"},  
        10: {"reason": "303"}, 14: {"reason": "9004"}, 15: {"reason": "90064"},  
        16: {"reason": "9010"}  
    }  
    p = params.get(r_type)  
    url = (f"{base_url}{common}&history_len=14&reason={p['reason']}&report_type=user"  
           f"&object_id={target_ID}&owner_id={target_ID}&target={target_ID}"  
           f"&reporter_id={device['reporter_id']}&current_region={current_region}")  
    rep_headers = {  
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',  
        'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.5',  
        'Connection': 'keep-alive', 'Cookie': 'sessionid=' + session, 'Host': 'www.tiktok.com',  
        'Sec-Fetch-Dest': 'document', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'none',  
        'Sec-Fetch-User': '?1', 'Upgrade-Insecure-Requests': '1', 'User-Agent': generate_user_agent()  
    }  
    data = {"object_id": target_ID, "owner_id": target_ID, "report_type": "user", "target": target_ID}  
    return url, rep_headers, data

def send_report(session, report_url, headers, data, proxies=None):
    try:
        rep = requests.post(report_url, headers=headers, data=data, proxies=proxies, timeout=10)
        return expected_response in rep.text
    except Exception:
        return False

def get_random_report_type():
    return random.choice([1,2,3,4,5,6,7,8,9,10,14,15,16])

def validate_session(session):
    check_url = ('https://api16-normal-c-alisg.tiktokv.com/passport/account/info/v2/?scene=normal&aid=1233')
    headers = {'Host': 'api16-normal-c-alisg.tiktokv.com', 'User-Agent': generate_user_agent(), 'Cookie': 'sessionid=' + session}  
    try:  
        resp = requests.get(check_url, headers=headers, timeout=5)  
        return 'user_id' in resp.text and '"session expired' not in resp.text
    except Exception:  
        return False

def get_target_id(username):
    headers = {'Host': 'www.tiktok.com', 'User-Agent': generate_user_agent()}
    try:  
        req = requests.get(f'https://www.tiktok.com/@{username}?lang=en', headers=headers)  
        return re.findall(r'"user":{"id":"(.*?)"', req.text)[0]  
    except: return None

def main():
    display_banner()
    while True:  
        show_menu()  
        try:  
            option = input(Y+"Select Report Type ➥ ")  
            if option == "0": sys.exit(0)
            if option in [str(i) for i in [1,2,3,4,5,6,7,8,9,10,12,13,14,15,16]]:
                option = int(option); break
            else: print_red("Invalid option!")  
        except ValueError: print_red("Enter a number!")  
    
    random_mode = option in [12, 13]  
    proxy_mode = True    
    
    sessions = []  
    print(B+'\n[!] لصق السيزنات الآن (أدخل السيزنات ثم اكتب "done" في سطر جديد):')  
    while True:
        line = input(C + "➤ "); 
        if line.lower() == 'done': break
        if line.strip(): sessions.append(line.strip())
    
    if not sessions: sys.exit(1)
    print_white("Checking...")  
    valid_sessions = [s for s in sessions if validate_session(s)]  
    if not valid_sessions: print_red("No valid sessions!"); sys.exit(1)
    
    working_proxies = []  
    if proxy_mode:  
        print(B+'\n[!] لصق البركسيات الآن (أدخل البركسيات ثم اكتب "done" في سطر جديد):')  
        proxy_list = []
        while True:
            line = input(C + "Proxy ➤ "); 
            if line.lower() == 'done': break
            if line.strip(): proxy_list.append(line.strip())
        if proxy_list: working_proxies = check_proxies_concurrently(proxy_list)
    
    username = input(Y+"Enter target username ➥ ")  
    target_id = get_target_id(username)  
    if not target_id: print_red("Not found!"); sys.exit(1)
    
    successful, failed = 0, 0
    try:  
        while True:  
            for session in valid_sessions:  
                current_type = get_random_report_type() if random_mode else option  
                url, headers, data = get_report_params(current_type, target_id, session)  
                proxies = {"http": random.choice(working_proxies), "https": random.choice(working_proxies)} if working_proxies else None
                if send_report(session, url, headers, data, proxies): successful += 1
                else: failed += 1
                sys.stdout.write(f"\r{G}Success: {successful}{rest} | {R}Failed: {failed}{rest}")
                sys.stdout.flush(); time.sleep(2)
    except KeyboardInterrupt: print_red("\nStopped")

if __name__ == "__main__":
    main()

