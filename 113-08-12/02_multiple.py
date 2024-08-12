import yt_dlp

# 定義多個影片的 URL 列表
URLs = [
    'https://www.youtube.com/watch?v=-Rp7UPbhErE',
    'https://www.youtube.com/watch?v=WCLlFA9SiDI',
    'https://www.youtube.com/watch?v=Z_dQeAZcbLI',
    'https://www.youtube.com/watch?v=XThOPqouX4I'
]

DIR = 'C:\\Youtube'

# 迭代每個影片的 URL 進行下載
for URL in URLs:
    # 設定下載選項，選擇最低解析度
    ydl_opts = {
        'format': 'worst',  # 選擇最低解析度
        'outtmpl': f'{DIR}/%(title)s.%(ext)s',  # 定義文件名格式
    }

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
            print(f"Video '{video_title}' downloaded successfully with the lowest resolution!")
            print(f"Video ID: {video_id}")
            print(f"Downloaded format itag: {downloaded_format_id}")

    except Exception as e:
        print(f"An unexpected error occurred while downloading from {URL}: {e}")
