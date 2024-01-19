from anyplayer import get_player

player = get_player('auto', './archive/badapple.mp3')
player.start()
player.wait()
