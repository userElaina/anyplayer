import time
import multiprocessing
from badapple.builtin_files import BA_MP4, BA_MP3, BA_WAV, ba_get
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


FFPLAY = 'ffplay'
MPV = 'mpv'
VLC = 'vlc'
MPG123 = 'mpg123'  # mp3
CMUS = 'cmus'  # mp3 mp4
ELISA = 'elisa'
FILEMGR = 'filemgr'
SIMPLEAUDIO = 'simpleaudio'  # wav
PYAUDIO = 'pyaudio'  # mp3+wav
PLAYSOUND = 'playsound'  # mp3+wav
AUTO = 'auto'

if __name__ == '__main__':
    multiprocessing.freeze_support()

    print(VERSION)
    ss = get_names()
    print('get_names', ss)
    print('get_availables', get_availables())
    print()

    for i in ss:
        time.sleep(1)
        if i in [MPG123, CMUS]:
            test(i, BA_MP3)
        elif i in [SIMPLEAUDIO]:
            test(i, BA_WAV)
        elif i in [PLAYSOUND, PYAUDIO]:
            test(i, BA_MP3)
            test(i, BA_WAV)
        else:
            test(i, BA_MP4)
            test(i, BA_MP3)
            test(i, BA_WAV)
        print('[%s] tested' % i)
        print()
