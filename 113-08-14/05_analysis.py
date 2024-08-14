import yt_dlp

URL = 'https://youtu.be/rTKqSmX9XhQ?si=WhDVWvpA99WcSESp'

# 设置 yt_dlp 选项
ydl_opts = {
    'format': 'all',  # 不限制格式，以便列出所有可用流
    'skip_download': True,  # 跳过下载，只提取信息
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # 提取视频信息
        info_dict = ydl.extract_info(URL, download=False)
        
        # 打印所有可用流的信息，并标注 video only 或 audio only
        formats = info_dict.get('formats', [])
        for res in formats:
            # 获取 vcodec 和 acodec 字段
            vcodec = res.get('vcodec', 'none')
            acodec = res.get('acodec', 'none')
            
            # 检查是否为 video only 或 audio only
            is_video_only = vcodec != 'none' and acodec == 'none'
            is_audio_only = vcodec == 'none' and acodec != 'none'
            
            # 设置标注
            label = ""
            if is_video_only:
                label = " [video only]"
            elif is_audio_only:
                label = " [audio only]"

            # 检查是否为 progressive
            is_progressive = vcodec != 'none' and acodec != 'none'
            
            # 设置标注
            label = ""
            if is_video_only:
                label = " [video only]"
            elif is_audio_only:
                label = " [audio only]"
            if is_progressive:
                label += " [progressive]"
            else:
                label += " [non-progressive]"
            
            # 打印流信息，包括 codec 信息和 progressive/non-progressive 信息
            print(f"Format ID: {res['format_id']}, Ext: {res['ext']}, Resolution: {res.get('resolution', 'N/A')}, "
                  f"Video Codec: {vcodec}, Audio Codec: {acodec}, Note: {res.get('format_note', 'N/A')}{label}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
