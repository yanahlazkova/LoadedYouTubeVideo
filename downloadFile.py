from pytube import YouTube
import windowError

link = ""#"https://youtu.be/tNSjC0sZiy8"
yt = ""
def download_video(link):
    try:
        
        yt = YouTube(link)
        is_download = yt.streams.get_highest_resolution().download("videos")
        # download_video(link)
        return is_download # Download Complete!
    except:
        windowError.open_window_error("YouTube link is invalid")
     

def show_data_video(ref):
    try:
        link = ref
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