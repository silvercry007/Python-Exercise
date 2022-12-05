import moviepy.editor as mpe

#To merge the audio and video if you download 1080p and above using DASH.
#add the video file path

video = mpe.VideoFileClip("")

#add audio file path
audio = mpe.AudioFileClip("")


final_clip = video.set_audio(audio)
#path where clip will be saved
final_clip.write_videofile("")
