import os
import numpy as np
from pydub import AudioSegment


if __main__ == "__name__":

    if not os.path.isdir("output"):
        os.mkdir("output")

    n_clips = len([f for f in os.listdir("data") if f.endswith("vocals.wav")])
    
    if n_clips == 0:
        print("NO VOCALS FOUND. PLACE DATA IN THE `data` folder with names",
            "f\"data/clip{i}-vocals.wav\" and f\"data/clip{i}-music.wav\"",
            "where i is a natural number.")
        assert False

    for i in range(n_clips):
        vocals = AudioSegment.from_wav(f"data/clip{i}-vocals.wav")
        music = AudioSegment.from_wav(f"data/clip{i}-music.wav")
        output = music.overlay(vocals, position=0)
        
        output.export(f"output/clip{i}-song.wav", format="wav")