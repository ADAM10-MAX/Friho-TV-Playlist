import requests
import time
import random

# قائمة بـ User-Agents لمحاكاة متصفحات مختلفة وتجنب الحظر
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
]

def fetch_links():
    url = "https://ugeen.live/renew.html"
    headers = {"User-Agent": random.choice(USER_AGENTS)}
    
    try:
        # إضافة تأخير عشوائي لمحاكاة سلوك الإنسان
        time.sleep(random.uniform(5, 10)) 
        
        response = requests.get(url, headers=headers, timeout=15)
        
        if response.status_code == 200:
            # هنا ستضع الكود الخاص بـ Regex لاستخراج الروابط من HTML
            # سأحتاج منك جزءاً من كود المصدر (HTML) للصفحة لتزويدك بـ Regex دقيق
            print("تم الاتصال بنجاح. جاري معالجة البيانات...")
            
            # مثال لتحديث الملف
            with open("playlist.m3u", "w") as f:
                f.write(response.text) # قم بتعديل هذا الجزء لاحقاً
        else:
            print(f"فشل الاتصال: رمز الحالة {response.status_code}")
            
    except Exception as e:
        print(f"حدث خطأ أثناء الجلب: {e}")

if __name__ == "__main__":
    fetch_links()
