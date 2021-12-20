from DrawInformation import DrawInformation
import random
import pygame
from typing import List


def generate_starting_list(n: int, min_val: int, max_val: int) -> List[int]:
    """

    :param n: number of elements
    :param min_val: Minimum value
    :param max_val: Maximum value
    :return: A list that contains elements between min_val and max_val exclusively
    """
    array = []
    for _ in range(n):
        val = random.randint(min_val, max_val)
        array.append(val)
    return array


def draw(draw_info: DrawInformation, algo_name: str, ascending: bool, fps: int) -> None:
    """
    Draw the window using the draw_info object
    :param draw_info: DrawInformation object
    :param algo_name: Name of the sorting algorithm
    :param ascending: A boolean that indicates if the algorithm is being sorted ascending order or descending order
    :param fps: Frames per second.
    :return: None
    """
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)

    title = draw_info.LARGE_FONT.render(f"{algo_name} - {'Ascending' if ascending else 'Descending'} at {fps} FPS", 1,
                                        draw_info.RED)
    draw_info.window.blit(title, (draw_info.width / 2 - title.get_width() / 2, 5))

    controls = draw_info.FONT.render("R: RESET | SPACE: START_SORTING | A: ASCENDING | D: DESCENDING", 1,
                                     draw_info.WHITE)
    draw_info.window.blit(controls, (draw_info.width / 2 - controls.get_width() / 2, 45))

    controls = draw_info.FONT.render("->: INCREASE SPEED | <-: DECREASE SPEED", 1,
                                     draw_info.WHITE)
    draw_info.window.blit(controls, (draw_info.width / 2 - controls.get_width() / 2, 75))

    sorting = draw_info.FONT.render("I: INSERTION SORT | B: BUBBLE SORT | M: MERGE SORT | Q: QUICK SORT ", 1,
                                    draw_info.WHITE)
    draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 105))
    draw_list(draw_info)
    pygame.display.update()


def draw_list(draw_info: DrawInformation, color_positions=None, clear_bg=False) -> None:
    """

    :param draw_info: DrawInformation object
    :param color_positions: A dictionary where they key is the index of an array and the value is the color of the value
    at that index
    :param clear_bg: A boolean to indicate whether to clear the background of the UI when the program is redrawing
    :return:
    """
    if color_positions is None:
        color_positions = {}
    if clear_bg:
        clear_rect = (draw_info.SIDE_PAD // 2, draw_info.TOP_PAD, draw_info.width - draw_info.SIDE_PAD,
                      draw_info.height - draw_info.TOP_PAD)
        pygame.draw.rect(draw_info.window, draw_info.BACKGROUND_COLOR, clear_rect)
    array = draw_info.array
    for i, val in enumerate(array):
        x = draw_info.start_x + i * draw_info.block_width
        y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height
        color = draw_info.GRADIENTS[i % 3]
        if i in color_positions:
            color = color_positions[i]
        pygame.draw.rect(draw_info.window, color, (x, y, draw_info.block_width, draw_info.height))
    if clear_bg:
        pygame.display.update()