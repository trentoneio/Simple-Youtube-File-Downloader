from pytube import YouTube
from sys import argv

link = argv[1]
directory = argv[2]
yt = YouTube(link,
             use_oauth=True,
             allow_oauth_cache=True)

print("Downloading...\nTitle: ", yt.title,"\nChannel: ",yt.author,"\n")

try:
    yd = yt.streams.get_highest_resolution()
    yd.download(directory)
    print(f"Done! Saved to {directory}")

except:
    print("No video found at ",argv[1]," or bad file path please try again");