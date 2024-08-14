import yt_dlp

URL = 'https://youtu.be/rTKqSmX9XhQ?si=WhDVWvpA99WcSESp'
DIR = 'C:\\Youtube'

# 下载1080p视频
ydl_opts_video = {
    'format': 'bestvideo[ext=mp4][height<=2160]',  # 选择1080p视频
    'outtmpl': f'{DIR}/video.mp4',  # 保存路径和文件名
}

try:
    with yt_dlp.YoutubeDL(ydl_opts_video) as ydl:
        info_dict_video = ydl.extract_info(URL, download=True)
        video_itag = info_dict_video.get("format_id", None)
        print(f"Video downloaded: {DIR}\\video.mp4")
        print(f"Video itag: {video_itag}")
except Exception as e:
    print(f"An unexpected error occurred while downloading video: {e}")

# 下载音频
ydl_opts_audio = {
    'format': 'bestaudio[ext=mp4]',  # 选择最佳音频
    'outtmpl': f'{DIR}/audio.mp4',  # 保存路径和文件名
}

try:
    with yt_dlp.YoutubeDL(ydl_opts_audio) as ydl:
        info_dict_audio = ydl.extract_info(URL, download=True)
        audio_itag = info_dict_audio.get("format_id", None)
        print(f"Audio downloaded: {DIR}\\audio.mp4")
        print(f"Audio itag: {audio_itag}")
except Exception as e:
    print(f"An unexpected error occurred while downloading audio: {e}")
