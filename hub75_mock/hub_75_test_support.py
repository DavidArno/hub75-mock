from collections import namedtuple
import sys

ColorSet = namedtuple('ColorSet', 'rgb index')
_module = sys.modules[__name__]

class UndefinedColorError(Exception):
    pass

class Hub75TestRun:
    def __init__(self):
        self.reset()

    def reset(self):
        self._test_color_indexes = { (0, 0, 0): 0 }
        self._start_call_count = 0
        self._stop_call_count = 0

    def set_colour_index(self, r, g, b, index):
        self._test_color_indexes[(r, g, b)] = index

    @property
    def start_call_count(self):
        return self._start_call_count

    @property
    def stop_call_count(self):
        return self._stop_call_count

def default_color_indexes():
    return { (0,0,0): ColorSet(0, 0) }

def default_test_run():
    return Hub75TestRun()

def reset():
    _module.color_indexes = default_color_indexes()
    _module.hub75TestRun = default_test_run()

color_indexes = default_color_indexes()
hub75TestRun = default_test_run()
