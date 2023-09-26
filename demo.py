from anyplayer import get_player

player = get_player('auto', './ba.mp3')
player.start()
player.wait()
