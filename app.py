import streamlit as st
import moviepy.editor as mp

def main():
    st.title("Video and Audio Manipulation App")

    # Upload video file
    video_file = st.file_uploader("Upload a video file", type=["mp4", "mov"])

    if video_file:
        st.video(video_file)

        # Button to extract audio
        if st.button("Extract Audio"):
            audio = extract_audio(video_file)
            st.audio(audio, format='audio/mp3', start_time=0)

def extract_audio(video_file):
    # Convert uploaded video to a temporary file
    with open(video_file.name, "wb") as f:
        f.write(video_file.getbuffer())

    # Load video file
    video = mp.VideoFileClip(video_file.name)

    # Extract audio
    audio = video.audio

    # Save audio to a file (you can upload this to cloud storage later)
    audio_file = "extracted_audio.mp3"
    audio.write_audiofile(audio_file)

    return audio_file

if __name__ == "__main__":
    main()