import os

def create_download_folder() -> str:
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    folder = os.path.join(desktop, "YouTube Downloads")
    os.makedirs(folder, exist_ok=True)
    return folder
