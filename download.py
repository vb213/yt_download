from pytubefix import YouTube
from pytubefix.cli import on_progress

# Function to download video
def download_video(url, save_path):
    try:
        # Create YouTube object
        yt = YouTube(url, on_progress_callback = on_progress)
        print(yt.title)
        # Get the highest resolution stream
        stream = yt.streams.get_highest_resolution() #filter(res="1080p").first()

        print(f"Downloading: {yt.title}")
        # Download the video
        stream.download(save_path)
        print(f"Video downloaded successfully and saved to: {save_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # URL of the YouTube video
    video_url = "https://www.youtube.com/watch?v=ekSpvQes9oI&list=PLdsjPDfuWbVi1Ef7wsTdt1tb6XoY3obV3&index=3" #input("Enter the YouTube video URL: ")

    # Path where the video will be saved
    save_directory = "."

    # Download the video
    download_video(video_url, save_directory)
