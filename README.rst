anyplayer
=========

A simple, minimal-hassle, few-dependency Python audio playback solution.

Play audio using any of the optional dependencies you have installed.

**Options** (clink to see installation instructions):
`ffplay <#ffmpeg-recommended>`__ `mpv <#mpv-recommended>`__ `vlc <#vlc>`__
`mpg123 <#mpg123>`__ `cmus <#cmus>`__ `gst <#gst>`__ `aplay <#alsa-aplay>`__
`simpleaudio <#simpleaudio>`__ `pyaudio <#pyaudio>`__
`playsound <#playsound>`__ `filemgr <#file-manager>`__ `elisa <#elisa>`__
(and auto)

**Note**: If you prefer the most convenient audio playback on a modern
PC and don't mind the additional hard disk space (less than 256 MB),
choose the optional dependency `ffplay <#ffmpeg-recommended>`__.

Usage Guidelines
----------------

**Installation**:

.. code:: shell

   pip install anyplayer

**Simple Example**:

.. code:: python

   from anyplayer import get_player

   player = get_player('auto', './ba.mp3')
   player.start()
   player.wait()

Optional Dependencies
---------------------

`ffplay <#ffmpeg-recommended>`__ `mpv <#mpv-recommended>`__ `vlc <#vlc>`__
`mpg123 <#mpg123>`__ `cmus <#cmus>`__ `gst <#gst>`__ `aplay <#alsa-aplay>`__
`simpleaudio <#simpleaudio>`__ `pyaudio <#pyaudio>`__
`playsound <#playsound>`__ `filemgr <#file-manager>`__ `elisa <#elisa>`__

FFmpeg (Recommended)
~~~~~~~~~~~~~~~~~~~~

`FFmpeg <https://www.ffmpeg.org/>`__ is a complete, cross-platform
solution to record, convert and stream audio and video.

**Windows**: Download binaries from **BtbN/FFmpeg-Builds**
`GitHub Releases <https://github.com/BtbN/FFmpeg-Builds/releases>`__ (and add
it to your ``PATH``).

**Linux**:

.. code:: shell

   pacman -Syu ffmpeg
   # or
   apt install ffmpeg

mpv (Recommended)
~~~~~~~~~~~~~~~~~

`mpv <https://mpv.io/>`__ is a free, open source, and cross-platform
media player.

**Windows**: Download binaries from `First-party
builds <https://nightly.link/mpv-player/mpv/workflows/build/master>`__
(and add it to your ``PATH``).

**Linux**:

.. code:: shell

   pacman -Syu mpv
   # or
   apt install mpv

VLC
~~~

`VLC <https://www.videolan.org/>`__ is a free and open source
cross-platform multimedia player and framework that plays most
multimedia files as well as DVDs, Audio CDs, VCDs, and various streaming
protocols.

**Linux**:

.. code:: shell

   pacman -Syu vlc
   # or
   apt install vlc

mpg123
~~~~~~

`mpg123 <https://www.mpg123.de/>`__ is a fast console MPEG Audio Player
and decoder library.

**Windows**: Download binaries from
`First-party <https://www.mpg123.de/download.shtml>`__
(and add it to your ``PATH``).

**Linux**:

.. code:: shell

   pacman -Syu mpg123
   # or
   apt install mpg123

cmus
~~~~

`cmus <https://cmus.github.io/>`__ is a small, fast and powerful console
music player for Unix-like operating systems.

**Linux**:

.. code:: shell

   pacman -Syu cmus

**Note**: To use the optional player ``cmus``, ensure ``cmus`` is
running in a separate terminal session.

Gst
~~~

`gst-plugins-base-libs <https://archlinux.org/packages/extra/x86_64/gst-plugins-base-libs/>`__
is a multimedia graph framework.

**Linux**:

.. code:: shell

   pacman -Syu gst-plugins-base-libs

ALSA aplay
~~~~~~~~~~

`aplay <https://alsa.opensrc.org/Alsa-utils>`__ is an utility for the
playback of ``.wav``, ``.voc``, ``.au`` files. It's included in the
official alsa-utils package.

**Linux**:

.. code:: shell

   pacman -Syu alsa-utils

simpleaudio
~~~~~~~~~~~

The `simplaudio <https://github.com/hamiltron/py-simple-audio>`__
package provides cross-platform, dependency-free audio playback
capability for Python 3 on **OSX**, **Windows**, and **Linux**.

.. code:: shell

   pip install simplaudio
   # or
   pacman -Syu python-simpleaudio

**Note**: Unfortunately,
`simpleaudio <https://github.com/hamiltron/py-simple-audio>`__ has
been archived and unmaintained for over three years. It has known bugs
and compatibility
`issues <https://github.com/hamiltron/py-simple-audio/issues/72>`__ with
**Python 3.12** or later.

(A segmentation fault will occur when audio playback is completed or
aborted. This can be used if you are only playing once and have no other
tasks after the playback stops.)

Additionally, on **Windows**, ensure you call
``multiprocessing.freeze_support()`` immediately after the
``if __name__ == '__main__':`` line in the main module:

.. code:: python

   # main.py
   import multiprocessing
   ...
   if __name__ == '__main__':
       multiprocessing.freeze_support()
       ...

PyAudio
~~~~~~~

`PyAudio <https://people.csail.mit.edu/hubert/pyaudio/>`__ provides
Python bindings for PortAudio v19, the cross-platform audio I/O library.

.. code:: shell

   pip install pyaudio
   # or
   conda install pyaudio portaudio
   # or
   pacman -Syu python-pyaudio

**Note**: The optional module ``pyaudio`` may fail to play **64-bit**
WAV files, as the ``wave`` module does not support **64-bit** WAV audio.

Additionally, on **Linux**, ``pyaudio`` may produce significant noise
during playback.

playsound
~~~~~~~~~

`playsound <https://github.com/TaylorSMarks/playsound>`__ is a pure
**Python**, cross platform, single-function module with no dependencies
for playing sounds.

**Note**: However, as the original module is no longer maintained and
doesn't accept pull requests, we use
`playsound3 <https://github.com/sjmikler/playsound3>`__ as an
alternative.

.. code:: shell

   pip install playsound3

File Manager
~~~~~~~~~~~~

Invokes the default file manager directly.

**Windows**: ``explorer.exe``.

**Linux**: ``dolphin`` or ``xdg-open``.

**Note**: ``filemgr`` directly invokes the default file manager so may
not exit cleanly.

Elisa
~~~~~

`Elisa <https://apps.kde.org/elisa/>`__ is the default music player for
**KDE**.

To do
-----

More information specific to **OSX** (optional dependencies, testing,
...)
