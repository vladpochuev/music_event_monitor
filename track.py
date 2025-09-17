from enum import Enum


class Track(object):
    def __init__(self, title=None, artist=None, state=None):
        self.title = title
        self.artist = artist
        self.state = state


class State(Enum):
    NONE = "NONE(0)"
    STOPPED = "STOPPED(1)"
    PAUSED = "PAUSED(2)"
    PLAYING = "PLAYING(3)"
    FAST_FORWARDING = "FAST_FORWARDING(4)"
    REWINDING = "REWINDING(5)"
    BUFFERING = "BUFFERING(6)"
    ERROR = "ERROR(7)"
    CONNECTING = "CONNECTING(8)"
    SKIPPING_TO_PREVIOUS = "SKIPPING_TO_PREVIOUS(9)"
    SKIPPING_TO_NEXT = "SKIPPING_TO_NEXT(10)"
    SKIPPING_TO_QUEUE_ITEM = "SKIPPING_TO_QUEUE_ITEM(11)"
