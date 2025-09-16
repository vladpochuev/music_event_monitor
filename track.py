from enum import Enum


class Track(object):
    def __init__(self, title=None, artist=None, state=None):
        self.title = title
        self.artist = artist
        self.state = state


class State(Enum):
    STOPPED = "STOPPED(1)"
    PAUSED = "PAUSED(2)"
    PLAYING = "PLAYING(3)"
