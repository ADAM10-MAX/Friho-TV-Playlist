import requests

# رابط الموقع الذي تستخرج منه البيانات
URL = "https://ugeen.live/renew.html" 
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def fetch_links():
    try:
        # إرسال طلب للموقع
        response = requests.get(URL, headers=HEADERS)
        if response.status_code == 200:
            # هنا ستضع الكود الخاص باستخراج النصوص (Regex)
            # بعد الاستخراج، نقوم بكتابة الروابط في ملف m3u
            with open("playlist.m3u", "w") as f:
                f.write(response.text) # مثال بسيط
            print("تم تحديث القائمة بنجاح")
    except Exception as e:
        print(f"حدث خطأ: {e}")

fetch_links()
