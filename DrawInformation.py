import pygame
from typing import List
import math


class DrawInformation:
    """
    DrawInformation is a class that deals with drawing the pygame window.
    It contains attributes necessary for drawing the window
    """
    pygame.init()
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    BLUE = 0,0,255
    BACKGROUND_COLOR = BLACK
    SIDE_PAD = 100
    TOP_PAD = 150

    GRADIENTS = [
        (128, 128, 128),
        (160, 160, 160),
        (192, 192, 192)
    ]
    FONT = pygame.font.SysFont(None, 30)
    LARGE_FONT = pygame.font.SysFont(None, 40)

    def __init__(self, width: int, height: int, array: List[int]):
        # Attributes will be set in set_list
        self.start_x = None
        self.block_height = None
        self.block_width = None
        self.max_val = None
        self.min_val = None
        self.array = None
        # Set width and height of window
        self.width = width
        self.height = height

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
        self.block_width = round((self.width - self.SIDE_PAD) / len(array))
        self.block_height = math.floor((self.height - self.TOP_PAD) / (self.max_val - self.min_val))
        self.start_x = self.SIDE_PAD // 2
