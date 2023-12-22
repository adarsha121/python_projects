from pytube import YouTube

print("Adarsha Welcomes you to YouTube Downloader!")

link = input("Enter the YouTube link: ")

yt = YouTube(link)

print("Title: ", yt.title)
print("Number of views: ", yt.views)

# Get all streams that include both video and audio
streams = yt.streams.filter(progressive=True, file_extension='mp4')

# Create a dictionary mapping resolutions to streams
resolutions = {stream.resolution: stream for stream in streams}

# Print all available resolutions
print("Available resolutions:")
for resolution in resolutions:
    print(resolution)

# Ask the user to choose a resolution
chosen_resolution = input("Enter the desired resolution: ")

# Download the video in the chosen resolution
resolutions[chosen_resolution].download()
print("Done") # print when download is complete
input("Press Enter to exit...") # wait for user to press Enter