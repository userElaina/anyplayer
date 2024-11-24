## anyplayer

A simple, minimal-hassle, few-dependency Python audio playback solution.

Play audio using any of the optional dependencies you have installed.

`ffplay` `mpv` `vlc` `mpg123` `cmus` `simpleaudio` `pyaudio` `playsound` `filemgr` `elisa` (and `auto`)

#### Installation

```sh
python -m pip install anyplayer
```

with any supported player:

```sh
python -m pip install "anyplayer[dev]"
```

#### Simple Example

```py
from anyplayer import get_player

player = get_player('auto', './ba.mp3')
player.start()
player.wait()
```

#### Notice

To use the optional player `cmus`, ensure `cmus` is running in a separate terminal session.

The optional module [`simpleaudio`](https://github.com/hamiltron/py-simple-audio) has been archived and unmaintained for over three years. It has known bugs and compatibility [issues](https://github.com/hamiltron/py-simple-audio/issues/72) with **Python 3.12** or later. (A segmentation fault will occur when audio playback is completed or aborted. This can be used if you are only playing once and have no other tasks after the playback stops.) Additionally, on **Windows**, ensure you call `multiprocessing.freeze_support()` immediately after the `if __name__ == '__main__':` line in the main module.

The optional module `pyaudio` may fail to play **64-bit** WAV files, as the `wave` module does not support **64-bit** WAV audio. Additionally, on **Linux**, `pyaudio` may produce significant noise during playback.

On **Windows**, `playsound` may fail when the same audio is played repeatedly.

`filemgr` directly invokes the default file manager and may not exit cleanly.

#### Recommended Optional Dependencies

Multiple audio (& video) formats supported: command-line tool `FFmpeg` or `mpv`.

#### To do

Optional Dependencies Documents

Test on **MacOS**
