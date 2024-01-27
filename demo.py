from anyplayer import get_player

player = get_player('auto', '../.ignore-archive/anyplayerarchive/badapple.mp3')
player.start()
player.wait()
