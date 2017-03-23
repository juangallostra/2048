import logic as l
import board as b
import pygame
from pygame.locals import *
import sys
import constants as const

rows = 4
cols = 4
black = 0, 0, 0


pygame.init()
pygame.display.set_caption("2048")

SIZE = width, height = cols * const.TILE_SIZE + (cols + 1) * const.PADDING,\
                       rows * const.TILE_SIZE + (rows + 1) * const.PADDING
screen = pygame.display.set_mode(SIZE)

twenty_forty_eight = l.TwentyFortyEight(rows, cols, const.OFFSETS)
board = b.Board(rows, cols, twenty_forty_eight.get_game_state(), const.PADDING, const.TILE_SIZE,
                const.BACKGROUND_COLOR, const.BACKGROUND_COLOR_EMPTY_TILE, const.BACKGROUND_TILE_COLORS,
                const.TILE_COLORS, const.FONT)

screen.fill(black)
# Main loop
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                twenty_forty_eight.move(const.LEFT)
                board.update_board(twenty_forty_eight.get_game_state())
            elif event.key == pygame.K_RIGHT:
                twenty_forty_eight.move(const.RIGHT)
                board.update_board(twenty_forty_eight.get_game_state())
            elif event.key == pygame.K_UP:
                twenty_forty_eight.move(const.UP)
                board.update_board(twenty_forty_eight.get_game_state())
            elif event.key == pygame.K_DOWN:
                twenty_forty_eight.move(const.DOWN)
                board.update_board(twenty_forty_eight.get_game_state())

    board.draw_board()
    board.draw_tiles()
    screen.blit(board.get_board(), (0, 0))
    pygame.display.update()
    pygame.display.flip()
