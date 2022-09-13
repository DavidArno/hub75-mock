################################################################################
#
################################################################################
from hub75_mock import hub_75_test_support

class Hub75():
    def start(self):
        hub_75_test_support.hub75TestRun._start_call_count += 1

    def stop(self):
        hub_75_test_support.hub75TestRun._stop_call_count += 1

def color(r, g, b):
    rgb = (r, g, b)
    if rgb in hub_75_test_support.color_indexes:
        return hub_75_test_support.color_indexes[rgb]
    else:
        raise hub_75_test_support.UndefinedColorError()

