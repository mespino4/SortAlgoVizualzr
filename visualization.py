# visualization.py

import pygame
import math
import constants

class DrawInformation:

    def __init__(self, width, height, lst, infobar=None):
        self.width = width
        self.height = height
        self.infobar = infobar  

        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithm Visualizer")
        self.set_list(lst)
        
        pygame.font.init()
        self.FONT = pygame.font.SysFont('comicsans', 30)
        self.LARGE_FONT = pygame.font.SysFont('comicsans', 40)

        # Define GREEN and RED attributes
        self.GREEN = constants.GREEN
        self.RED = constants.RED

    def set_list(self, lst):
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)

        # Adjusted the starting x-coordinate for drawing
        self.start_x = constants.SIDE_PAD
        # Adjusted the block width to avoid overlapping with the sidebar
        self.block_width = round((self.width - constants.SIDE_PAD) / len(lst))
        self.block_height = math.floor((self.height - constants.TOP_PAD) / (self.max_val - self.min_val))

    def draw_list(self, color_positions={}, clear_bg=False):
        lst = self.lst

        if clear_bg:
            clear_rect = (constants.SIDE_PAD//2, constants.TOP_PAD, 
                            self.width - constants.SIDE_PAD, self.height - constants.TOP_PAD)
            pygame.draw.rect(self.window, constants.BACKGROUND_COLOR, clear_rect)

        for i, val in enumerate(lst):
            x = self.start_x + i * self.block_width
            y = self.height - (val - self.min_val) * self.block_height

            color = constants.GRADIENTS[i % 3]

            if i in color_positions:
                color = color_positions[i] 

            pygame.draw.rect(self.window, color, (x, y, self.block_width, self.height))

        if clear_bg:
            pygame.display.update()
