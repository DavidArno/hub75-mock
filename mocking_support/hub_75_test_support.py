import sys
from typing import Any, NamedTuple

ColorSet = NamedTuple('ColorSet', [('rgb', int), ('index', int)])

ColorIndexes = dict[tuple[int, int, int], ColorSet]

BLACK = 0

_module:Any = sys.modules[__name__]


class Hub75TestRun:
    def __init__(self, width:int, height:int):
        self.start_call_count = 0
        self.stop_call_count = 0

        self.matrix_indexes = []
        for i in range(2):
            self.matrix_indexes.append(self._create_matrix(width, height, BLACK))

    def _create_matrix(self, width:int, height:int, color:int) -> list:
        matrix = []
        for _ in range(height):
            matrix.append(self._create_row(width, color))

        return matrix

    def _create_row(self, width:int, color:int):
        row = []
        for _ in range(width):
            row.append(color)

        return row

################################################################################
# color handling functions
# These are to support the hub75.color() and hub75.color_hsv() functions
#
# NOTE: this functionality should be used with care if you run parallel tests
#       as they are not compatible with such a testing approach 
################################################################################
def default_color_indexes() -> ColorIndexes:
    return { (0,0,0): ColorSet(BLACK, 0) }

def reset_color_indexes() -> None:
    _module.color_indexes = default_color_indexes()

def to_hub75Color(r:int, g:int, b:int) -> int:
    return int((r << 16) + (g << 8) + b)

def add_rgb_and_index_to_colors(r:int, g:int, b:int, index:int):
    _module.color_indexes[(r, g, b)] = ColorSet(to_hub75Color(r, g, b), index)

def add_rgb_gamma_corrected_color_and_index_to_colors(
    r:int, 
    g:int, 
    b:int, 
    gamma_corrected_color:int, 
    index:int
):
    _module.color_indexes[(r, g, b)] = ColorSet(gamma_corrected_color, index)
    
color_indexes:ColorIndexes = default_color_indexes()

