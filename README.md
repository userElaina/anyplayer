## anyplayer

A simple, minimal-hassle, few-dependency Python audio playback solution.

Play audio using any of the optional dependencies you have installed.

`ffplay` `mpv` `vlc` `mpg123` `cmus` `simpleaudio` `pyaudio` `playsound` `filemgr` `elisa` (and `auto`)

##### Installation

```sh
python -m pip install anyplayer
```

with any supported player:

```sh
python -m pip install anyplayer[dev]
```

##### Simple Example

```py
from anyplayer import get_player

player = get_player('auto', './ba.mp3')
player.start()
player.wait()
```

##### Notice

To use the `cmus` player, you need to start `cmus` in a separate terminal session first.

The optional module [`simpleaudio`](https://github.com/hamiltron/py-simple-audio) has been archived and unmaintained for over three years. It has known bugs and compatibility [issues](https://github.com/hamiltron/py-simple-audio/issues/72) with **Python 3.12** or later.

On **Linux**, `pyaudio` may produce noticeable noise.

On **Windows**, `playsound` may fail when the same audio is played repeatedly.

`filemgr` directly invokes the default file manager and may not exit cleanly.

##### Recommended Optional Dependencies

Multiple audio (& video) formats supported: command-line tool `FFmpeg` or `mpv`.

##### To do

Optional Dependencies Documents

Test on **MacOS**
