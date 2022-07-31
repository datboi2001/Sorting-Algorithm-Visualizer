import math
from typing import List, Tuple

import pygame
from pygame.font import SysFont


class DrawInformation:
    """
    DrawInformation is a class that deals with drawing the pygame window.
    It contains attributes necessary for drawing the window
    """
    pygame.init()
    BLACK: Tuple[int, int, int] = (0, 0, 0)
    WHITE: Tuple[int, int, int] = (255, 255, 255)
    GREEN: Tuple[int, int, int] = (0, 255, 0)
    RED: Tuple[int, int, int] = (255, 0, 0)
    BLUE: Tuple[int, int, int] = (0, 0, 255)
    BACKGROUND_COLOR: Tuple[int, int, int] = BLACK
    SIDE_PAD: int = 100
    TOP_PAD: int = 150

    GRADIENTS: List[Tuple[int, int, int]] = [
        (128, 128, 128),
        (160, 160, 160),
        (192, 192, 192)
    ]
    FONT: SysFont = pygame.font.SysFont("arial", 30)
    LARGE_FONT: SysFont = pygame.font.SysFont("arial", 40)

    def __init__(self, width: int, height: int, array: List[int]):
        # Attributes will be set in set_list
        self.start_x = None
        self.block_height = None
        self.block_width = None
        self.max_val = None
        self.min_val = None
        self.array = None
        # Set width and height of window
        self.width: int = width
        self.height: int = height

        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithm Visualizer by Datthew Nguyen")
        self.set_list(array)

    def set_list(self, array: List[int]) -> None:
        """
        Set attributes related to array. Calculate the width and height of each block,
        which represents a number in the list. Calculate the starting x coordinate of each block.
        :param array: An array of integers
        :return: None
        """
        self.array: List[int] = array
        self.min_val: int = min(array)
        self.max_val: int = max(array)
        self.block_width: int = round((self.width - self.SIDE_PAD) / len(array))
        self.block_height: int = math.floor((self.height - self.TOP_PAD) / (self.max_val - self.min_val))
        self.start_x: int = self.SIDE_PAD // 2
