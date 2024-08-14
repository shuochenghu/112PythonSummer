import yt_dlp

URL = 'https://youtu.be/rTKqSmX9XhQ?si=WhDVWvpA99WcSESp'
DIR = 'C:\\Youtube'

# 設定下載選項，選擇最高解析度並確保格式為MP4
ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=mp4]/best[ext=mp4]',  # 選擇最高解析度並確保為MP4格式
    'outtmpl': f'{DIR}/%(title)s.%(ext)s',  # 定義文件名格式
    'merge_output_format': 'mp4',  # 確保合併後的格式為MP4
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
        print(f"Video '{video_title}' downloaded successfully in MP4 format!")
        print(f"Video ID: {video_id}")
        print(f"Downloaded format itag: {downloaded_format_id}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
