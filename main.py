from pytube import YouTube
import requests
from bs4 import BeautifulSoup

def get_video_details(url):
    yt = YouTube(url)
    title = yt.title
    captions = yt.captions.get_by_language_code('en')
    return title, captions

def get_transcript(captions):
    transcript = captions.generate_srt_captions()
    return transcript

def download_subtitles(video_url):
    yt = YouTube(video_url)
    captions = yt.captions.get_by_language_code('en')
    if captions:
        transcript = captions.generate_srt_captions()
        with open(f"{yt.title}.srt", "w", encoding="utf-8") as file:
            file.write(transcript)
        print(f"Subtitles downloaded successfully: {yt.title}.srt")
    else:
        print("No captions available for this video.")

def main():
    url = input("Enter the YouTube video URL: ")
    try:
        title, captions = get_video_details(url)
        if captions:
            download_subtitles(url)
        else:
            print("No subtitles available for this video.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
