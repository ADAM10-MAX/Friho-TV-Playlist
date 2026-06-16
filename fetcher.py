import json
import re

def convert_m3u_to_json():
    with open("playlist.m3u", "r", encoding="utf-8") as f:
        content = f.read()

    # استخراج الأسماء والروابط
    channels = []
    # البحث عن نمط #EXTINF والسطر الذي يليه
    matches = re.findall(r'#EXTINF:-1,(.*?)\n(http.*?://.*?)\n', content)
    
    for name, url in matches:
        channels.append({"name": name.strip(), "url": url.strip()})

    # حفظ النتيجة في ملف JSON
    with open("links.json", "w", encoding="utf-8") as f:
        json.dump(channels, f, ensure_ascii=False, indent=4)
    print("تم تحويل الروابط إلى صيغة JSON بنجاح!")

if __name__ == "__main__":
    convert_m3u_to_json()
