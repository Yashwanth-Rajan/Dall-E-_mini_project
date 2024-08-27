import streamlit as st
from pytube import YouTube
import os

# Define the Streamlit app
st.title("YouTube Video Downloader")

# Text input for the user to paste the URL
video_url = st.text_input("Paste your URL")

# Folder Selector for the user to choose the output path
output_path = st.text_input("Choose the output folder path", type="default")

# Function to download the YouTube video
def download_youtube_video(video_url, output_path):
    try:
        # Create a YouTube object with the video URL
        yt = YouTube(video_url)

        # Get the highest resolution stream (first one in the list)
        video_stream = yt.streams.get_highest_resolution()

        # Download the video to the specified output path
        video_stream.download(output_path)

        st.text("Video downloaded successfully!")
    except Exception as e:
        st.text(f"Error: {str(e)}")

# Button to trigger the download
if st.button("Download"):
    if output_path:
        download_youtube_video(video_url, output_path)
    else:
        st.warning("Please choose the output folder path.")
