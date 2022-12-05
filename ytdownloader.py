from pytube import YouTube
from sys import argv

# import pytube module and use argv built in library, add link of the video after the command (means it uses the first argument)

# you can also remove the argument and directly enter the link in the code

link = argv[1]

yt = YouTube(link)

# to check if we can get the exact video from title and view count

print("Title: ", yt.title)

print("View: ", yt.views)

#you can use .get_by_reolution("x") to change the resolution you want to download in

yd = yt.streams.get_highest_resolution()

#Enter the path in which you want to download the video.

#if no path is given it will download in the main folder.

yd.download()

