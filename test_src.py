import time

from badapple.builtin_files import BA_BA, BA_MP4, BA_MP3, BA_WAV, ba_get

from src.anyplayer import get_player, VERSION, get_names, get_availables


def test(p: str, a: str) -> None:
    a = ba_get(a)
    # print(a)
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
    print()


# CMUS = 'cmus'
# ELISA = 'elisa'
# FFPLAY = 'ffplay'
# FILEMGR = 'filemgr'
# MPG123 = 'mpg123'  # mp3
# MPV = 'mpv'
# PLAYSOUND = 'playsound'  # mp3+wav
# PYAUDIO = 'pyaudio'  # mp3+wav
# SIMPLEAUDIO = 'simpleaudio'  # wav
# VLC = 'vlc'
# AUTO = 'auto'

print(VERSION)
ss = get_names()
print('get_names', ss)
print('get_availables', get_availables())
print()

for i in ss:
    time.sleep(1)
    if i in ['mpg123', 'cmus']:
        test(i, BA_MP3)
    elif i in ['simpleaudio']:
        test(i, BA_WAV)
    elif i in ['playsound', 'pyaudio']:
        test(i, BA_MP3)
        test(i, BA_WAV)
    else:
        test(i, BA_MP4)
        test(i, BA_MP3)
        test(i, BA_WAV)
    print('[%s] tested' % i)
    print()


# test(PLAYSOUND, BA_WAV)
# test(FFPLAY, BA_WAV)
# test(MPV, BA_WAV)
# test(VLC, BA_WAV)
# test(MPG123, BA_MP3)
# test(CMUS, BA_MP3)
# test(SIMPLEAUDIO, BA_WAV)
# test(PYAUDIO, BA_WAV)
# test(PLAYSOUND, BA_WAV)
# test(AUTO, BA_WAV)
