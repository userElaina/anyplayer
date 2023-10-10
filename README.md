## anyplayer

Play audio in any available way.

`ffplay` `mpv` `vlc` `mpg123` `cmus` `simpleaudio` `pyaudio` `playsound` `pydub` `auto`

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

##### Recommended Optional Dependencies

Only wav audio or no audio: Python module `simpleaudio`.

Multiple audio (& video) formats supported: command-line tool `FFmpeg`.
