import subprocess
import os

CHANNEL = input("Enter YouTube channel handle (without @): ")
CHANNEL_NAME = input("Enter YouTube channel display name: ")

SAVE_DIR = "../thumbnails"
SAVE_DIR_FORMAT = f"{SAVE_DIR}/%(channel)s/%(title)s.%(ext)s"

def getThumbs(url):
    print(f"Thumbnails will be saved to: {SAVE_DIR_FORMAT.split('/')[0]} folder.")

    command = [
        "yt-dlp",
        "--write-thumbnail",
        "--skip-download",
        "--output",
        SAVE_DIR_FORMAT,
        "--no-warnings",
        url
    ]

    try:
        result = subprocess.run(command, 
                                check=True, 
                                capture_output=False, 
                                text=True)
        
        if result.returncode == 0:
            print("\nDownload successfully completed.")
        else:
            print(f"\nfailed: {result.returncode}.")

    except FileNotFoundError:
        print("'yt-dlp' command not found.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")
    except Exception as e:
        print(f"Error: {e}")


if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

CHANNEL_URL = f"https://www.youtube.com/@{CHANNEL}".strip()

getThumbs(CHANNEL_URL)
