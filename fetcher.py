import requests
import time
import random
import re

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
]

def fetch_links():
    url = "https://ugeen.live/renew.html"
    headers = {"User-Agent": random.choice(USER_AGENTS)}
    
    try:
        time.sleep(random.uniform(5, 10)) 
        response = requests.get(url, headers=headers, timeout=15)
        
        if response.status_code == 200:
            content = response.text
            
            # نمط البحث (Regex) لاستخراج روابط البث (مثال عام)
            # سنبحث عن أي رابط ينتهي بـ .m3u أو يحتوي على مسار البث
            links = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', content)
            
            # تصفية الروابط فقط التي تخص البث (مثلاً التي تحتوي على ugeen.live)
            stream_links = [link for link in links if "ugeen.live" in link]
            
            if stream_links:
                with open("playlist.m3u", "w", encoding="utf-8") as f:
                    f.write("#EXTM3U\n")
                    for link in stream_links:
                        f.write(f"#EXTINF:-1,Channel\n{link}\n")
                print(f"تم العثور على {len(stream_links)} رابط وحفظهم في playlist.m3u")
            else:
                print("لم يتم العثور على روابط بث في الصفحة.")
        else:
            print(f"فشل الاتصال: {response.status_code}")
            
    except Exception as e:
        print(f"خطأ: {e}")

if __name__ == "__main__":
    fetch_links()
