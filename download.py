from pytubefix import YouTube
from pytubefix.cli import on_progress
import sys

# Function to download video
def download_video(url, save_path):
    try:
        # Create YouTube object
        yt = YouTube(url, on_progress_callback = on_progress)
        print(yt.title)
        # Get the highest resolution stream
        stream_low = yt.streams.get_highest_resolution() #filter(res="1080p").first()
        stream_high = yt.streams.filter(res="1080p").first()

        print(f"Downloading: {yt.title}")
        # Download the video
        stream_low.download(save_path + "/low")
        if stream_high:
            stream_high.download(save_path + "/high")
        print(f"Video downloaded successfully and saved to: {save_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # URL of the YouTube video
    video_url = sys.argv[1] #input("Enter the YouTube video URL: ")

    # Path where the video will be saved
    save_directory = "."

    # Download the video
    download_video(video_url, save_directory)
