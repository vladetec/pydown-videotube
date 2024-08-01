from pytube import YouTube

def download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    #youtubeObject = youtubeObject.streams.filter(only_audio=True).first()
    try:
        youtubeObject.download()
        
    except:
        print("An error has occurred")
    print("Download is completed successfully")


link = input("Enter the YouTube video URL: ")
download(link)