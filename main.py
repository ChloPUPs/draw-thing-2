"""
    The main file
"""

import pygame as pg
from pygame import Clock, Surface, Event, Color
import sys

from canvas_utils import Line, Point

def update(mouse_pos_info: dict[str, tuple[int, int]], mouse_down: bool, drawn_lines: list[Line]) -> None:
    """
        Called every frame. Used for physics and logic!!
    """

    for e in pg.event.get():
        handle_events(e, drawn_lines)
    
    if not is_mouse_pos_same(mouse_pos_info["current_pos"], mouse_pos_info["last_pos"]) and mouse_down:
        add_line(drawn_lines, mouse_pos_info["current_pos"], mouse_pos_info["last_pos"])

def draw(surface: Surface, drawn_lines: list[Line]) -> None:
    """
        Called every frame. Used for drawing stuff!!!
    """

    surface.fill([0, 0, 0])

    draw_lines(drawn_lines, surface)

def handle_events(e: Event, drawn_lines: list[Line]) -> None:
    """
        Gets an event as a parameter and handles it by doing stuff with it **JUST READ THE FUNCTION NAME**
    """

    if e.type == pg.QUIT:
        pg.quit()
        sys.exit()
    elif e.type == pg.MOUSEBUTTONDOWN:
        if e.button == 1:
            set_mouse_down(True)
    elif e.type == pg.MOUSEBUTTONUP:
        if e.button == 1:
            set_mouse_down(False)
    elif e.type == pg.KEYDOWN:
        if e.key == pg.K_BACKSPACE:
            drawn_lines.clear()

def is_mouse_pos_same(current_mouse_pos: tuple[int, int], last_mouse_pos: tuple[int, int]) -> bool:
    """
        Returns True the if the mouse position is the same
    """

    return current_mouse_pos == last_mouse_pos

def add_line(drawn_lines: list[Line], current_mouse_pos: tuple[int, int], last_mouse_pos: tuple[int, int]) -> None:
    """
        Adds line to the drawn_lines list
    """

    pos1 = Point(current_mouse_pos[0], current_mouse_pos[1])
    pos2 = Point(last_mouse_pos[0], last_mouse_pos[1])

    color: Color = Color(255, 255, 255)

    drawn_lines.append(Line(pos1, pos2, color))

def draw_lines(drawn_lines: list[Line], surface: Surface) -> None:
    """
        draws all lines in drawn_lines
    """

    for line in drawn_lines:
        line.draw(surface)

def set_mouse_down(value: bool) -> None:
    global mouse_down

    mouse_down = value

pg.init()

# Important Things

SCREEN_WIDTH: int = 640
SCREEN_HEIGHT: int = 480

SCREEN: Surface = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

CLOCK: Clock = Clock()
FRAMERATE: float = 60.0

mouse_pos_info: dict[str, tuple[int, int]] = {
    "last_pos": (0, 0),
    "current_pos": (0, 0)
}

mouse_down = False

# Game Things

drawn_lines: list[Line] = []

# Event Loop

while True:
    mouse_pos_info["current_pos"] = pg.mouse.get_pos()

    update(mouse_pos_info, mouse_down, drawn_lines)
    draw(SCREEN, drawn_lines)

    mouse_pos_info["last_pos"] = mouse_pos_info["current_pos"]

    CLOCK.tick(FRAMERATE)
    pg.display.flip()
