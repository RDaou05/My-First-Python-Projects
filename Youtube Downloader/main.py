import os
import time
from subprocess import call
import getpass
print("Please wait a few seconds while the nessecary modules are being installed...")
call("pip install pytube", shell=True)
import pytube

def initalize_and_download_video():
    global video

    url = input("\n[+] Please enter your URL: ")

    try:
        youtube = pytube.YouTube(url)
        video = youtube.streams.first()
    except Exception as e:
        print(e)
        print("[+] That was an incorrect url. Please try again")
        time.sleep(1)
        initalize_and_download_video()


def save_file():
    global username
    username = getpass.getuser()
    path_of_folder = r"C:\Users\%s\Youtube Downloads" % username
    if os.path.isdir(path_of_folder) == False:
        os.mkdir(path_of_folder)
    video.download(path_of_folder)


def directions():
    print("[+] File Has been sucsessfully downloaded!\n")
    print(
        f"[+] To see your file...\n\n[+] Open your files app\n[+] Go to Windows (C:)\n[+] Go to users\n[+] Go to {username}\n[+] Go to Youtube Downloads\n\n[+] Then you should see your youtube file"
    )
    # This lets the user read the diretions without the window closing
    time.sleep(1000)


initalize_and_download_video()
save_file()
directions()
