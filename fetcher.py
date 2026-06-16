# كود fetcher.py المحدث
playlist_content = """#EXTM3U
#EXTINF:-1,⚽ beIN MAX 1 (8K)
http://ugeen.live:8080/Ugeen_VIPNQms83/LcKgtu/4540
#EXTINF:-1,⚽ beIN MAX 2 (8K)
http://ugeen.live:8080/Ugeen_VIPNQms83/LcKgtu/4541
#EXTINF:-1,⚽ beIN SPORTS 1 HD
http://ugeen.live:8080/Ugeen_VIPNQms83/LcKgtu/46
"""

with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write(playlist_content)
print("تم تحديث الملف بنجاح!")
