from pytube import YouTube
link = "https://www.youtube.com/watch?v=vzLYScIhMjM"
yt = YouTube(link)
print ("Title: {yt.title}",yt.title)
print ("Number of views: {yt.views}",yt.views)
video = yt.streams.all()
vid = list(enumerate(video))


for i in video:
    print(i)

strm = int(input("Enter the number of stream: "))
video[strm].download()





print ("done.")