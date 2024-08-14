import yt_dlp
import ffmpeg
import os

URL = 'https://youtu.be/rTKqSmX9XhQ?si=WhDVWvpA99WcSESp'
DIR = 'c:\\Youtube'

# 下载1080p视频
ydl_opts_video = {
    'format': 'bestvideo[height<=1080][ext=mp4]',  # 选择1080p的视频流
    'outtmpl': f'{DIR}/video.mp4',  # 视频保存路径和文件名
}

# 下载音频
ydl_opts_audio = {
    'format': 'bestaudio[ext=mp4]/bestaudio',  # 选择最佳音频流，优先使用m4a格式
    'outtmpl': f'{DIR}/audio.mp4',  # 音频保存路径和文件名
}

try:
    # 下载视频
    with yt_dlp.YoutubeDL(ydl_opts_video) as ydl:
        info_video = ydl.extract_info(URL, download=True)
        video_itag = info_video.get('format_id', None)
        print(f"Video downloaded: {DIR}\\video.mp4")
        print(f"Video itag: {video_itag}")

    # 下载音频
    with yt_dlp.YoutubeDL(ydl_opts_audio) as ydl:
        info_audio = ydl.extract_info(URL, download=True)
        audio_itag = info_audio.get('format_id', None)
        print(f"Audio downloaded: {DIR}\\audio.mp4")
        print(f"Audio itag: {audio_itag}")

    # 使用ffmpeg合并视频和音频
    video_input = ffmpeg.input(os.path.join(DIR, 'video.mp4'))
    audio_input = ffmpeg.input(os.path.join(DIR, 'audio.mp4'))
    output_path = os.path.join(DIR, 'output.mp4')

    # 将视频和音频合并到一个文件中
    ffmpeg.output(video_input, audio_input, output_path).run(capture_stdout=True)
    print(f"Video and audio merged: {output_path}")

    # 删除临时文件
    os.remove(os.path.join(DIR, 'video.mp4'))
    os.remove(os.path.join(DIR, 'audio.mp4'))
    print("Temporary files removed.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
