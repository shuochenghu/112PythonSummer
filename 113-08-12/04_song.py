import yt_dlp

URL = 'https://youtu.be/rTKqSmX9XhQ?si=WhDVWvpA99WcSESp'
DIR = 'C:\\Youtube'

# 設定下載選項，選擇音訊格式
ydl_opts = {
    'format': 'bestaudio/best',  # 選擇最佳音訊格式
    'outtmpl': f'{DIR}/%(title)s.%(ext)s',  # 定義文件名格式
    'postprocessors': [{  # 音訊轉換
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',  # 將音訊轉換為 mp3 格式
        'preferredquality': '192',
    }],
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # 提取影片資訊並下載
        info_dict = ydl.extract_info(URL, download=True)
        
        # 取得已下載格式的 itag
        downloaded_format = next((f for f in info_dict['formats'] if f['ext'] == 'm4a'), None)
        if downloaded_format:
            downloaded_itag = downloaded_format.get("format_id", None)
            print(f"Downloaded format itag: {downloaded_itag}")
        else:
            print("Failed to retrieve itag for the downloaded format.")
    
    print(f"Audio downloaded successfully to {DIR}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
