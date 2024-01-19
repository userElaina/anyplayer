from typing import Iterable

from .p_player import Player

__CLASS = dict()
__RELIAS = dict()
__RELIAS_FLAG = False


def add_player(
    cls: classmethod,
) -> None:
    assert cls.name not in __CLASS
    __CLASS[cls.name] = cls


def realias(player: str) -> str:
    global __RELIAS, __RELIAS_FLAG
    if not __RELIAS_FLAG:
        __RELIAS = {j: i for i in __CLASS for j in __CLASS[i].alias}
        __RELIAS_FLAG = True
    return __RELIAS.get(player, player)


def is_player(player: str) -> bool:
    return realias(player) in __CLASS


def get_player(player: str, audio: str, clk: float = 0.1) -> Player:
    assert is_player(player)
    player = realias(player)
    return __CLASS[player](audio, clk)


def get_available_player(
    player: str,
    audio: str,
    clk: float = 0.1,
    err: bool = False,
) -> Player:
    if not is_player(player):
        if err:
            raise ValueError('%s is not a player' % player)
        else:
            return None
    ans = get_player(player, audio, clk)
    if not ans.is_available():
        if err:
            raise ValueError('Player %s is not available' % player)
        else:
            return None
    return ans


def get_names() -> list:
    return list(__CLASS.keys())


def get_availables() -> list:
    return [i for i in __CLASS if get_player(i, '').is_available()]


for i in __RELIAS:
    assert __RELIAS[i] in __CLASS
