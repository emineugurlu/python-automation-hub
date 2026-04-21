import yt_dlp
import os

def download_video(url, download_path='downloads', only_audio=False):
    """
    Downloads a video or audio from YouTube using yt-dlp.
    """
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    ydl_opts = {
        'outtmpl': f'{download_path}/%(title)s.%(ext)s',
    }
    
    if only_audio:
        ydl_opts.update({
            'format': 'm4a/bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'm4a',
            }],
        })
    else:
        ydl_opts.update({
            'format': 'bestvideo+bestaudio/best',
        })

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"🚀 Starting download: {url}")
            ydl.download([url])
            print("✅ Download completed successfully!")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    video_url = input("Enter the YouTube URL: ")
    choice = input("Download as (1) Video or (2) Audio only? ")
    
    is_audio = True if choice == '2' else False
    download_video(video_url, only_audio=is_audio)