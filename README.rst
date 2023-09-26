anyplayer
---------

Play audio in any available way.

``ffplay`` ``mpv`` ``vlc`` ``mpg123`` ``cmus`` ``simpleaudio`` ``pyaudio`` ``playsound`` ``pydub`` ``auto``

**Install**: 

.. code-block:: shell

    python -m pip install anyplayer

**Demo**:

.. code-block:: python

    from anyplayer import get_player

    player = get_player('auto', './ba.mp3')

    player.start()

    player.wait()

**Recommended optional dependencies**: 

Only wav audio or no audio: Python module **simpleaudio**.

Multiple audio (& video) formats supported: command-line tool **FFmpeg**.
