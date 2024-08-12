import yt_dlp

URL = 'https://youtu.be/rTKqSmX9XhQ?si=WhDVWvpA99WcSESp'
#URL = 'https://www.youtube.com/watch?v=cTK7cozOcB4'
DIR = 'C:\\Youtube'

# 設定下載選項，選擇最低解析度
ydl_opts = {
    'format': 'worst',  # 選擇最低解析度
    #'format': 'bestvideo+bestaudio',  # 選擇最高解析度
    'outtmpl': f'{DIR}/%(title)s.%(ext)s',  # 定義文件名格式
}

# 使用 yt-dlp 下載影片
try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # 提取影片資訊並下載
        info_dict = ydl.extract_info(URL, download=True)
        
        # 取得影片的 ID
        video_id = info_dict.get("id", None)
        
        # 取得影片的標題
        video_title = info_dict.get("title", None)
        
        # 取得已下載格式的 itag
        downloaded_format_id = info_dict.get("format_id", None)
        
    if video_id and downloaded_format_id:
        print(f"Video '{video_title}' 成功下載最低解析度影片!")
        print(f"Video ID: {video_id}")
        print(f"Downloaded format itag: {downloaded_format_id}")

except Exception as e:
    print(f"非預期錯誤發生: {e}")
