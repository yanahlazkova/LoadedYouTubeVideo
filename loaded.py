from pytube import YouTube

# link = "https://youtu.be/tNSjC0sZiy8"

def download_video(ref):
    yt = YouTube(ref)
    title = yt.title
    author = yt.author
    video = {"title": title, "author": author}
    print("Title: ", yt.title)
    print("Video: ", yt.views)
    print("Url miniature: ", yt.thumbnail_url)
    print("Author: ", yt.author)
    
    # print("Video: ", dir(yt))
    #  print("ytcfg: ", yt.ytcfg)
    #  yt.streams.get_highest_resolution().download("videos")
    return video
     
# download_video(link)