from yt_dlp import YoutubeDL

def progress_hook(d):
    if d['status'] == 'downloading':
        percent = d.get('_percent_str', 'N/A').strip()
        print(f"Downloading... {percent}", end='\r')
    elif d['status'] == 'finished':
        print("\nDownload finished, processing file...")

def download_video(url: str, folder: str, download_playlist: bool):
    ydl_opts = {
        'outtmpl': f"{folder}/%(playlist_index)s - %(title)s.%(ext)s" if download_playlist else f"{folder}/%(title)s.%(ext)s",
        'format': 'best[ext=mp4]/best',
        'noplaylist': not download_playlist,
        'progress_hooks': [progress_hook],
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"Download completed to: {folder}")
    except Exception as e:
        print(f"An error occurred: {e}")
