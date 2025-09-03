"""
    The file containing the Line class
"""

from .point import Point
from pygame import Color, Surface
import pygame as pg

class Line:
    """
        This class is used for lines.
    """

    def __init__(self, pos1: Point, pos2: Point, color: Color) -> None:
        self.pos1: Point = pos1
        self.pos2: Point = pos2

        self.color: Color = color
    
    def draw(self, surface: Surface):
        """
            Draws self to surface.
        """

        pg.draw.line(surface, self.color, [int(self.pos1.x), int(self.pos1.y)], [int(self.pos2.x), int(self.pos2.y)])
