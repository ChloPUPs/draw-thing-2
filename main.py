"""
    The main file
"""

import pygame as pg
from pygame import Clock, Surface, Event
import sys

from canvas_utils import Line

def update(current_mouse_pos: tuple[int, int], last_mouse_pos: tuple[int, int]) -> None:
    """
        Called every frame. Used for physics and logic!!
    """

    for e in pg.event.get():
        handle_events(e)
    
    if not is_mouse_pos_same(current_mouse_pos, last_mouse_pos):
        print("a")

def draw() -> None:
    """
        Called every frame. Used for drawing stuff!!!
    """

def handle_events(e: Event) -> None:
    """
        Gets an event as a parameter and handles it by doing stuff with it **JUST READ THE FUNCTION NAME**
    """

    if e.type == pg.QUIT:
        pg.quit()
        sys.exit()

def is_mouse_pos_same(current_mouse_pos: tuple[int, int], last_mouse_pos: tuple[int, int]) -> bool:
    """
        Returns True the if the mouse position is the same
    """

    return current_mouse_pos == last_mouse_pos

pg.init()

# Important Things

SCREEN_WIDTH: int = 640
SCREEN_HEIGHT: int = 480

SCREEN: Surface = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

CLOCK: Clock = Clock()
FRAMERATE: float = 60.0

last_mouse_pos: tuple[int, int] = (0, 0)
current_mouse_pos: tuple[int, int] = (0, 0)

# Game Things

drawn_lines: list[Line] = []

# Event Loop

while True:
    current_mouse_pos = pg.mouse.get_pos()

    update(current_mouse_pos, last_mouse_pos)
    draw()

    last_mouse_pos = current_mouse_pos

    CLOCK.tick(FRAMERATE)
    pg.display.flip()
