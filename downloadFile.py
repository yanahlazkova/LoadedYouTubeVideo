from pytube import YouTube
import windowError

# link = "https://youtu.be/tNSjC0sZiy8"

def download_video(link):
    
    try:
        yt = YouTube(link)
        yt.streams.get_highest_resolution().download("videos")
        # is_download = download_video(link)
        # return True # Download Complete!
    except:
        windowError("YouTube link is invalid")
     

def show_data_video(link):
    try:
        yt = YouTube(link)
        
        title = yt.title
        author = yt.author
        image = yt.thumbnail_url
        video = {"title": title, "author": author, "image": image}
        print("Title: ", yt.title)
        print("Video: ", yt.views)
        print("Url miniature: ", yt.thumbnail_url)
        print("Author: ", yt.author)
        return video
    except:
        windowError.open_window_error("YouTube link is invalid")

    
# show_data_video("https://youtu.be/tNSjC0sZiy8")