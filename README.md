# anyplayer

A simple, minimal-hassle, few-dependency Python audio playback solution.

Play audio using any of the optional dependencies you have installed.

`ffplay` `mpv` `vlc` `mpg123` `cmus` `simpleaudio` `pyaudio` `playsound` `filemgr` `elisa` (and `auto`)

## Usage Guidelines

### Installation

```sh
python -m pip install anyplayer
```

with any supported player:

```sh
python -m pip install "anyplayer[dev]"
```

### Simple Example

```py
from anyplayer import get_player

player = get_player('auto', './ba.mp3')
player.start()
player.wait()
```

## Optional Dependencies

`ffplay` `mpv` `vlc` `mpg123` `cmus` `simpleaudio` `pyaudio` `playsound` `filemgr` `elisa`

### FFmpeg

[FFmpeg](https://www.ffmpeg.org/) is a complete, cross-platform solution to record, convert and stream audio and video.

**Windows**: Download binaries from **BtbN/FFmpeg-Builds** [GitHub Releases](https://github.com/BtbN/FFmpeg-Builds/releases) (and add it to your system **PATH**).

**Linux**:

```sh
sudo pacman -Syu ffmpeg
# or
sudo apt install ffmpeg
```

### mpv

[mpv](https://mpv.io/) is a free, open source, and cross-platform media player.

**Windows**: Download binaries from [First-party builds](https://nightly.link/mpv-player/mpv/workflows/build/master) (and add it to your system **PATH**).

**Linux**:

```sh
sudo pacman -Syu mpv
# or
sudo apt install mpv
```

### VLC

[VLC](https://www.videolan.org/) is a free and open source cross-platform multimedia player and framework that plays most multimedia files as well as DVDs, Audio CDs, VCDs, and various streaming protocols.

**Linux**:

```sh
sudo pacman -Syu vlc
# or
sudo apt install vlc
```

### mpg123

[mpg123](https://www.mpg123.de/) is a fast console MPEG Audio Player and decoder library.

**Windows**: Download binaries from [First-party builds](https://www.mpg123.de/download.shtml) (and add it to your system **PATH**).

**Linux**:

```sh
sudo pacman -Syu mpg123
# or
sudo apt install mpg123
```

### cmus

[cmus](https://cmus.github.io/) is a small, fast and powerful console music player for Unix-like operating systems.

**Linux**:

```sh
sudo pacman -Syu cmus
```

### Notice

To use the optional player `cmus`, ensure `cmus` is running in a separate terminal session.

The optional module [`simpleaudio`](https://github.com/hamiltron/py-simple-audio) has been archived and unmaintained for over three years. It has known bugs and compatibility [issues](https://github.com/hamiltron/py-simple-audio/issues/72) with **Python 3.12** or later. (A segmentation fault will occur when audio playback is completed or aborted. This can be used if you are only playing once and have no other tasks after the playback stops.) Additionally, on **Windows**, ensure you call `multiprocessing.freeze_support()` immediately after the `if __name__ == '__main__':` line in the main module.

The optional module `pyaudio` may fail to play **64-bit** WAV files, as the `wave` module does not support **64-bit** WAV audio. Additionally, on **Linux**, `pyaudio` may produce significant noise during playback.

On **Windows**, `playsound` may fail when the same audio is played repeatedly.

`filemgr` directly invokes the default file manager and may not exit cleanly.

### Recommended Optional Dependencies

Multiple audio (& video) formats supported: command-line tool `FFmpeg` or `mpv`.

## To do

Optional Dependencies Documents

Test on **MacOS**
