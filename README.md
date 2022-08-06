___

# SongSynthsizer

Takes in a `wav` of lyrics and a `wav` file of music, and combines the two into a song `wav`.

## How to use
Place data the data into the `data` folder. Name vocal files `data/clip{i}-vocals.wav` and instrumental files
`data/clip{i}-music.wav` where $i$ is a natural number. A pair of vocal and music files with the same $i$ will be
combined into a song `mp3` file if you run `python sync-audio.py`. The output will be named `clip{i}-song.wav`, and it
can be found in the `ouput` folder.

## Installation
Follow the steps, assuming you have conda:
```
conda create -n sync python=3.8
pip install numpy pydub
```
Then, run: 
```
brew install ffmpeg # macOS

# -OR- 

apt-get install ffmpeg libavcodec-extra # Linux
```

If you have Windows, consider upgrading to another OS. But in the meantime, follow instructions to install `ffmpeg` on 'https://github.com/jiaaro/pydub#installation'. It is a dependency of `pydub`

