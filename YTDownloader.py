import pytube

print("=================================================")
print("***           YouTube Downloader             ***")
print("=================================================\n")

url = input("Enter the URL for your YouTube video: ")

# Not sure what type of object this is
youtube = pytube.YouTube(url)

print("Select format:")
print("(1) High resolution video")
print("(2) Low resolution video")
print("(3) Audio only")
format = ''
while format !='1' and format !='2' and format !='3':
    format = input("***\nType 1, 2, or 3: ")

if int(format) == 1:
    video = youtube.streams.get_highest_resolution()
    filetype = '.mp4'
if int(format) == 2:
    video = youtube.streams.get_lowest_resolution()
    filetype = '.mp4'
if int(format) == 3:
    video = youtube.streams.get_audio_only()
    filetype = '.mp4 (audio only)'


# Leaving parentheses blank would save to current directory
video.download('/home/pi/Downloads')

# This would create a subfolder called "Videos" in the current directory
# video.download("./Videos")

print(f"\nDownload complete: {video.title}{filetype}")