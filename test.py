import time

from badapple.builtin_files import BA_BA, BA_MP4, BA_MP3, BA_WAV, ba_get

from src.anyplayer import get_player, VERSION, get_names, get_availables


def test(p: str, a: str) -> None:
    a = ba_get(a)
    print(a)
    player = get_player(p, a)
    print(player)
    print('is_available', player.is_available())
    if not player.is_available():
        return
    player.start()
    print('started')
    print('is_alive', player.is_alive())
    try:
        for i in range(6):
            time.sleep(0.5)
            print(i+1, 'is_alive', player.is_alive())
    except KeyboardInterrupt:
        pass
    finally:
        print('before is_alive', player.is_alive())
        player.terminate()
        if player.is_alive():
            print(0.5)
            time.sleep(0.5)
        print('after is_alive', player.is_alive())
    print('end')


__FFPLAY = 'ffplay'
__MPV = 'mpv'
__VLC = 'vlc'
__MPG123 = 'mpg123'  # mp3
__CMUS = 'cmus'
__SIMPLEAUDIO = 'simpleaudio'  # wav
__PYAUDIO = 'pyaudio'  # mp3+wav
__PLAYSOUND = 'playsound'  # mp3+wav
__PYDUB = 'pydub'  # simpleaudio-pyaudio-ffplay
__AUTO = 'auto'

print(VERSION)
print('get_names', get_names())
print('get_availables', get_availables())

# for i in get_names():
#     test(i, BA_WAV)

test(__PLAYSOUND, BA_WAV)
test(__PYDUB, BA_WAV)
test(__FFPLAY, BA_WAV)
test(__MPV, BA_WAV)
test(__VLC, BA_WAV)
test(__MPG123, BA_MP3)
test(__CMUS, BA_MP3)
test(__SIMPLEAUDIO, BA_WAV)
test(__PYAUDIO, BA_WAV)
test(__PLAYSOUND, BA_WAV)
test(__PYDUB, BA_WAV)
test(__AUTO, BA_WAV)
