import pygame
from pygame.locals import *


def hex_to_rgb(hex_color):
    """
    Helper function to convert hex strings to RGB
    """
    hex_color = hex_color.lstrip('#')
    h_len = len(hex_color)
    return tuple(int(hex_color[i:i + h_len // 3], 16) for i in range(0, h_len, h_len // 3))


class Board:
    """
    Class that draws the current board and game state
    """
    def __init__(self, rows, cols, game_state, padding, tile_size, background_color, empty_tile_color,
                 background_tile_colors, tile_colors, font):
        self._rows = rows
        self._cols = cols
        self._padding = padding
        self._tile_size = tile_size
        self._background_color = background_color
        self._empty_tile_color = empty_tile_color
        self._background_tile_colors = background_tile_colors
        self._tile_colors = tile_colors
        self._font = pygame.font.SysFont(font[0], font[1], bold=True)
        self._width = cols*self._tile_size+(cols+1)*self._padding
        self._height = rows*self._tile_size+(rows+1)*self._padding
        self._grid = game_state
        self._surface = pygame.Surface((self._width, self._height))
        self._surface.fill(hex_to_rgb(self._background_color))

    def update_board(self, game_state):
        """
        Update the state of the board
        """
        self._grid = game_state

    def draw_board(self):
        """
        Draw the board without tiles
        """
        # Create one row
        row = pygame.Surface((self._width, self._tile_size+self._padding), pygame.SRCALPHA, 32)
        row = row.convert_alpha()
        for col_num in range(self._cols):
            tile = pygame.Surface((self._tile_size, self._tile_size))
            tile.fill(hex_to_rgb(self._empty_tile_color))
            row.blit(tile, (self._padding+col_num*(self._padding+self._tile_size), self._padding))
        # Add as many empty rows to the board as the specified number of rows
        for row_num in range(self._rows):
            self._surface.blit(row, (0, (self._padding+self._tile_size)*row_num))

    def draw_tile(self, row, col, tile_value):
        """
        Draw a tile on the board
        """
        tile = pygame.Surface((self._tile_size, self._tile_size))
        tile.fill(hex_to_rgb(self._background_tile_colors[tile_value]))
        text = self._font.render(str(tile_value), True, hex_to_rgb(self._tile_colors[tile_value]))
        text_width, text_height = text.get_size()
        tile.blit(text, ((self._tile_size-text_width)//2, (self._tile_size-text_height)//2))
        self._surface.blit(tile, (self._padding+(self._padding+self._tile_size)*col,
                                 self._padding+(self._padding+self._tile_size)*row))

    def draw_tiles(self):
        for row in range(self._rows):
            for col in range(self._cols):
                if self._grid[row][col] != 0:
                    self.draw_tile(row, col, self._grid[row][col])

    def get_board(self):
        return self._surface
