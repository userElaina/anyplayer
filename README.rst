anyplayer
=========

Play audio in any available way.

``ffplay`` ``mpv`` ``vlc`` ``mpg123`` ``cmus`` ``simpleaudio`` ``pyaudio`` ``playsound`` ``auto``

Installation
------------

.. code-block:: shell

    python -m pip install anyplayer

with any supported player:

.. code-block:: shell

    python -m pip install anyplayer[dev]

Simple Example
--------------

.. code-block:: python

    from anyplayer import get_player

    player = get_player('auto', './ba.mp3')
    player.start()
    player.wait()

Recommended Optional Dependencies
---------------------------------

Only wav audio or no audio: Python module ``simpleaudio``.

Multiple audio (& video) formats supported: command-line tool ``FFmpeg``.
