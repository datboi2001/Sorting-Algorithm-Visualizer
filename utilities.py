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


def blit_text(surface, text, pos, font, color=pygame.Color('white')):
    words = [word.split(" ") for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.


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

    title = draw_info.LARGE_FONT.render(f"{algo_name} - {'Ascending' if ascending else 'Descending'} at {fps} FPS"
                                        f" with array of size {len(draw_info.array)}", 1,
                                        draw_info.RED)
    draw_info.window.blit(title, (draw_info.width / 2 - title.get_width() / 2, 5))

    text = "R: RESET | SPACE: START_SORTING | A: ASCENDING | D: DESCENDING |" \
           " Right arrow: Increase speed | Left arrow: Decrease speed |" \
            " Up arrow: Increase size| Down arrow: Decrease size" \
           " I: INSERTION SORT | B: BUBBLE SORT | M: MERGE SORT | Q: QUICK SORT"
    blit_text(draw_info.window, text, (35, 55), draw_info.FONT)
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