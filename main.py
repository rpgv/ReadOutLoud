import wave
from piper import PiperVoice, SynthesisConfig
import sounddevice as sd
import soundfile as sf
import streamlit as st
import time



def convert_and_play(text, speed=0.90):
    syn_config = SynthesisConfig(
    volume=0.5,  # half as loud
    length_scale=speed,  # twice as slow
    noise_scale=1.0,  # more audio variation
    noise_w_scale=1.0,  # more speaking variation
    normalize_audio=False, # use raw audio from voice
)
    voice = PiperVoice.load("./en_US-amy-medium.onnx")
    with wave.open("output.wav", "wb") as wav_file:
        voice.synthesize_wav(text, wav_file, syn_config=syn_config)
    data, fs = sf.read("output.wav", dtype='float32')  
    sd.play(data, fs)

    return data, fs

def stop_audio():
    sd.stop()

def input_box():
    text = st.text_input("ReadOutLoud", placeholder="Input your text")
    speed = st.select_slider(
    "Select a speaking speed",
    options=[0.5, 0.6, 0.7,0.8,0.9,1.0,1.5,2.0])
    if st.button("Read", type="primary"):
        st.write("Now reading:", text)
        convert_and_play(text, speed)
        if st.button('Stop', on_click=stop_audio):pass
          


if __name__ == '__main__':
    input_box()
    # play_audio('Hello there !')
