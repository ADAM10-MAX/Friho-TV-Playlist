import requests
import random

# 1. قائمة البروكسيات (استبدلها ببروكسيات حقيقية)
proxies_list = [
    {"http": "http://user:pass@ip:port"},
    # أضف المزيد هنا
]

def fetch_data():
    url = "https://ugeen.live/renew.html"
    proxy = random.choice(proxies_list) # اختيار عشوائي للبروكسي
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    
    try:
        response = requests.get(url, headers=headers, proxies=proxy, timeout=10)
        if response.status_code == 200:
            # هنا ستكتب منطق استخراج الروابط (Regex)
            # ثم حفظ النتيجة في playlist.m3u
            print("تم جلب البيانات بنجاح")
    except Exception as e:
        print(f"فشل الاتصال: {e}")

fetch_data()
