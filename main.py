import os

# winreg
try:
    from winreg import *
except ImportError:
    print("Trying to Install required module: winreg\n")
    os.system('py -m pip install winreg')
from winreg import *

# youtube_dl
try:
    import youtube_dl
except ImportError:
    print("Trying to Install required module: youtube_dl\n")
    os.system('py -m pip install youtube_dl')
import youtube_dl

# pyperclip
try:
    import pyperclip
except ImportError:
    print("Trying to Install required module: pyperclip\n")
    os.system('py -m pip install pyperclip')
import pyperclip

# other modules
import time
import sys

sys.path.append(os.path.abspath("SO_site-packages"))

# Start of the program
print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
print("YouTube downloader from clipboard")
print("Version: v.1.2")
print("Autor: JohnoCZ")
print("https://github.com/Johno95CZ/YouTube-Downloader")
print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")

# Define folder
# Define folder
print("\nDo you want to change folder? (Current: Downloads folder)")
print("y/n")
answear = input()
if answear == "y":
    print("\nWrite there a path to the folder where you want to save .mp3 files:")
    folder = input()
else:
    with OpenKey(HKEY_CURRENT_USER, 'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders') as key:
        folder = QueryValueEx(key, '{374DE290-123F-4565-9164-39C4925E467B}')[0]
print("\nEverything is ready now! Program is now listening to the clipboard...")

# Settings of youtube_dl
ydl_opts = {
    'format': 'bestaudio',
    'outtmpl': folder + '\%(title)s.%(ext)s',
    'reactrictfilenames': True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}


# Function for downloading mp3
def download(url):
    print("[*] Downloading...")
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        print("[*] ERROR...")
        print(e)
    print("[*] Done!")


# Function for checking if text is YouTube link
def check_link(url):
    if "youtube.com" in url:
        download(url)
    if "youtu.be" in url:
        download(url)


# Checking if is the clipboard has been changed
recent_value = ""
while True:
    tmp_value = pyperclip.paste()
    if tmp_value != recent_value:
        recent_value = tmp_value
        check_link(recent_value)
    time.sleep(0.1)