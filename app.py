import streamlit as st
import moviepy.editor as mp
from moviepy.Clip import Clip

# MoviePyの進捗バーを無効化するためのダミー関数
def dummy_tqdm_bar(*args, **kwargs):
    pass

Clip.logger = dummy_tqdm_bar  # MoviePyの進捗バーを無効化

def main():
    st.title("動画と音声の操作アプリ")

    # 動画ファイルのアップロード
    video_file = st.file_uploader("動画ファイルをアップロードしてください", type=["mp4", "mov"])

    if video_file:
        st.video(video_file)

        # 音声抽出ボタン
        if st.button("音声を抽出する"):
            audio = extract_audio(video_file)
            st.audio(audio, format='audio/mp3', start_time=0)

def extract_audio(video_file):
    # アップロードされた動画を一時ファイルに保存
    with open(video_file.name, "wb") as f:
        f.write(video_file.getbuffer())

    # 動画ファイルを読み込み
    video = mp.VideoFileClip(video_file.name)

    # 音声を抽出
    audio = video.audio

    # 音声をファイルに保存（後でクラウドストレージにアップロードすることができます）
    audio_file = "extracted_audio.mp3"
    audio.write_audiofile(audio_file)

    return audio_file

if __name__ == "__main__":
    main()