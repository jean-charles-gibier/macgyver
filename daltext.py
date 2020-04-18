from pprint import pprint

import constant
from dal import Dal
import logging as lg
logger = lg.getLogger(__name__)
from time import sleep
from pygame import event
from pygame.constants import (QUIT, KEYDOWN, K_ESCAPE, K_RIGHT, K_LEFT, K_UP, K_DOWN)


class DalText(Dal):
    """ PyGame implementation """
    def init(self, map_game):
        """inteface intialization ne sert pas à gd chose en mode texte"""
        return map_game.map_content

    def load_item(self, fenetre, item):
        """load  item not used in mode text """
        pass

    def draw_item(self, fenetre, item):
        """display figure of item ... """
        switcher = {
            constant.IMG_MCGYVER: "M",
            constant.IMG_GARDIEN: "G",
            constant.IMG_AIGUILLE:"A",
            constant.IMG_ETHER: "E",
            constant.IMG_TUBE: "T"
        }
        letter = switcher.get(item.img_file, " ")
        l = list(fenetre[item.case_y])
        l[item.case_x] = letter
        fenetre[item.case_y] = "".join(l)

    def draw_map(self, fenetre, map_content):
        print('')
        y_unit = 0
        for raw in map_content:
            x_raw = 0
            for unit in raw:
                print(unit, end='')
                x_raw = x_raw + 1
            y_unit = y_unit + 1
        print('')
        print('')
        return

    def draw_footer(self, fenetre):
        pass

    def event_get(self):
        getch = _Getch()
        return [getch]

    def clock(self):
        sleep(0.1)

    def flip(self):
        import os
        from sys import platform
        clear = lambda: os.system((platform == "win32" and 'cls') or 'clear')  #  Linux / windows  System
        clear()

    def event_quit(self, event):
        pass

    def event_keydown_escape(self, event):
        pass

    def event_keydown_right(self, event):
        pass

    def event_keydown_left(self, event):
        pass

    def event_keydown_up(self, event):
        pass

    def event_keydown_down(self, event):
        pass

class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""

    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self):
        return self.impl()

class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()

