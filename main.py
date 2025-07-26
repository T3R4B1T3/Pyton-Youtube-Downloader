from downloader import download_video
from utils import create_download_folder

def main():
    while True:
        url = input("Please paste the YouTube video or playlist URL: ").strip()
        if not url:
            print("Error: URL cannot be empty. Please try again.")
            continue 
        break

    folder = create_download_folder()

    while True:
        download_playlist = input("Download entire playlist if URL is a playlist? (y/n): ").strip().lower()
        if download_playlist not in ('y', 'n'):
            print("Error: Please enter 'y' or 'n'.")
            continue
        download_playlist = (download_playlist == 'y')
        break

    download_video(url, folder, download_playlist)

if __name__ == "__main__":
    main()
