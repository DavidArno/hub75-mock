################################################################################
#
################################################################################
from typing import Any, NewType
from mocking_support import hub_75_test_support

class Hub75():
    def __init__(self, width:int, height:int, _:Any):
        self._test_run = hub_75_test_support.Hub75TestRun(width, height)

    def start(self) -> None:
        hub_75_test_support.Hub75TestRun.start_call_count += 1

    def stop(self) -> None:
        hub_75_test_support.Hub75TestRun.stop_call_count += 1

    def set_color(self, x, y, color) -> None:
        pass

    def flip_and_clear(self, color) -> None:
        pass

    @property
    def test_run(self) -> hub_75_test_support.Hub75TestRun:
        return self._test_run


def color(r:int, g:int, b:int) -> int:
    rgb = (r, g, b)
    return hub_75_test_support.color_indexes[rgb].rgb \
        if rgb in hub_75_test_support.color_indexes \
        else hub_75_test_support.to_hub75Color(r, g, b)
