from pytube import YouTube
import tkinter as tk #pyqt
from tkinter import filedialog
from sys import argv


#allow the user to select a filepath
def selectdirectory():
    root = tk.Tk()
    root.withdraw() # we don't want a full GUI, so keep the root window from appearing
    directory = filedialog.askdirectory(title = "Where would you like the video to be saved?")
    root.quit()
    return directory

    

link = argv[1]
yt = YouTube(link)

print("Downloading...\nTitle: ", yt.title,"\nChannel: ",yt.author,"\n")

try:
    directory = selectdirectory()
    yd = yt.streams.get_highest_resolution()
    yd.download(directory)

except:
    print("No video found at ",argv[1]," or  no bad file path please try again");