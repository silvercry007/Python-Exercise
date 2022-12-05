from pytube import Playlist

#Enter link of the playlist
p = Playlist("")
print(f'Downloading: {p.title}')

#get_by_itag(137) for 1080p as highest resolution is 4k, it will take too much memory. any video above 720p will have audio and video file separate.
#you can also download to a specific path by metioning file in download()
#get_by_itag(251) for 160kpbs audio file.
#if you want ot download only 720p then no need to download the audio as YT uses DASH (dynamic adaptive streaiming for http)
#get_by_tag(22) for 720p

for video in p.videos:
    video.streams.get_by_itag(137).download()
    print("Video Downloaded: ", video.title)
    
for video in p.videos:
    video.streams.get_by_itag(251).download()
    print("Audio Downloaded: ", video.title)
    
print("All Videos are downloaded")
    