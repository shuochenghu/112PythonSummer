import yt_dlp

PLAYLIST_URL = 'https://youtube.com/playlist?list=PLJIxQEea9fRY50FL5RXVYXW6-KFt5W1pX&si=GZQ_BAztYy9sTPSp'
DIR = 'C:\\Youtube'

# 設定下載選項，選擇最高解析度的影音檔
ydl_opts = {
    'format': 'worst',  # 選擇最低解析度的影音檔
    'outtmpl': f'{DIR}/%(playlist_title)s/%(title)s.%(ext)s',  # 定義文件名格式，按播放清單分類
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # 下載整個播放清單
        ydl.download([PLAYLIST_URL])
    print(f"Playlist downloaded successfully to {DIR}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
