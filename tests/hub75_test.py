from mocking_support import hub_75_test_support
import hub75

def test_to_rgb_int_handles_red_green_and_blue_correctly():
    red = 226
    green = 94
    blue = 107

    assert hub_75_test_support.to_hub75Color(red, green, blue) == 0xE25E6B

def test_color_function_handles_indexed_and_non_indexed_colours():
    hub_75_test_support.reset_color_indexes()
    hub_75_test_support.add_rgb_gamma_corrected_color_and_index_to_colors(255, 255, 255, 1234, 1)
    hub_75_test_support.add_rgb_and_index_to_colors(0x30, 0x30, 0x30, 2)
    white = hub75.color(255, 255, 255)
    grey1 = hub75.color(9, 9, 9)
    grey2 = hub75.color(0x30, 0x30, 0x30)

    assert white == 1234
    assert grey1 == 0x090909
    assert grey2 == 0x303030
     
def test_can_create_matrix_of_specific_size_and_all_pixels_default_to_black():
    matrix = hub75.Hub75(8, 8, None)
    color_count = 0
    displayed_matrix = matrix.test_run.matrix_indexes[0]
    backing_store_matrix = matrix.test_run.matrix_indexes[1]
    for x in range(8):
        for y in range(8):
            color_count += abs(displayed_matrix[x][y])
            color_count += abs(backing_store_matrix[x][y])

    assert color_count == 0