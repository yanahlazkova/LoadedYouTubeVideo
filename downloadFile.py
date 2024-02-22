from pytube import YouTube

link = "" # "https://youtu.be/tNSjC0sZiy8"
yt = ""
def download_video():
    yt = YouTube(link)
    
    # print("Video: ", dir(yt))
    #  print("ytcfg: ", yt.ytcfg)
    yt.streams.get_highest_resolution().download("videos")
     
# download_video(link)

def show_data_video(ref):
    link = ref
    yt = YouTube(ref)
    title = yt.title
    author = yt.author
    image = yt.thumbnail_url
    video = {"title": title, "author": author, "image": image}
    print("Title: ", yt.title)
    print("Video: ", yt.views)
    print("Url miniature: ", yt.thumbnail_url)
    print("Author: ", yt.author)
    return video

# show_data_video("https://youtu.be/tNSjC0sZiy8")