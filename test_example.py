from anyplayer import get_player

player = get_player('auto', '../.ignore-archive/ba-archive/badapple.wav')
player.start()
player.wait()
