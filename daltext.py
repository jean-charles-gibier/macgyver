from pprint import pprint

import constant
from dal import Dal
import logging as lg
logger = lg.getLogger(__name__)
from time import sleep
from pygame import event
from pygame.constants import (QUIT, KEYDOWN, K_ESCAPE, K_RIGHT, K_LEFT, K_UP, K_DOWN)


class DalText(Dal):

    # local text array that copy content of text map
    _map_cache = []

    """ PyGame implementation """
    def init(self, map_game):
        """inteface intialization ne sert pas à gd chose en mode texte"""
        # we copy the map 2 the cache
        self._map_cache = map_game.map_content
        return map_game.map_content

    def load_item(self, fenetre, item):
        """load  item not used in mode text """
        self.draw_item(fenetre, item)

    def draw_item(self, fenetre, item):
        """display figure of item ... """

        switcher = {
            constant.IMG_MCGYVER: "M",
            constant.IMG_GARDIEN: "G",
            constant.IMG_AIGUILLE:"A",
            constant.IMG_ETHER: "E",
            constant.IMG_TUBE: "T"
        }
        # identify perso/item by img filename :-(
        letter = switcher.get(item.img_file, " ")

        # clean old item
        y_unit = 0
        for raw in self._map_cache:
            self._map_cache[y_unit] = raw.replace(letter, ' ')
            y_unit = y_unit + 1

        # place the new one
        l = list(self._map_cache[item.case_y])
        l[item.case_x] = letter
        self._map_cache[item.case_y] = "".join(l)


    def draw_map(self, fenetre, map_content):
        # in text mode we just clear the screen
        # the map will be shown at flip step
        import os
        from sys import platform
        clear = lambda: os.system((platform == "win32" and 'cls') or 'clear')  #  Linux / windows  System
        clear()

    def draw_footer(self, fenetre):
        pass

    def event_get(self):
        getch = _Getch()
        value = getch()
        obj_ret = None
        # sequences touches windows
        if value == b'\x1b':
            value = getch()
            if value == b'\x1b':
                obj_ret = event.Event(KEYDOWN, {'unicode': '\x1b', 'key': 27, 'mod': 0, 'scancode': 9, 'window': None})
        elif value == b'\xe0':
            value = getch()
            if value == b'P':
                obj_ret = event.Event(KEYDOWN, {'key': 274, 'mod': 0, 'scancode': 104, 'window': None})
            elif value == b'H':
                obj_ret = event.Event(KEYDOWN, {'key': 273, 'mod': 0, 'scancode': 98, 'window': None})
            elif value == b'K':
                obj_ret = event.Event(KEYDOWN, {'key': 276, 'mod': 0, 'scancode': 100, 'window': None})
            elif value == b'M':
                obj_ret = event.Event(KEYDOWN, {'key': 275, 'mod': 0, 'scancode': 102, 'window': None})
        elif value == '\x1b':
            # sequences Xterm / ansi
            value = getch()
            if value == '[':
                value = getch()
                if value == 'A':
                    obj_ret = event.Event(KEYDOWN, {'key': 273, 'mod': 0, 'scancode': 98, 'window': None})
                elif value == 'B':
                    obj_ret = event.Event(KEYDOWN, {'key': 274, 'mod': 0, 'scancode': 104, 'window': None})
                elif value == 'C':
                    obj_ret = event.Event(KEYDOWN, {'key': 275, 'mod': 0, 'scancode': 102, 'window': None})
                elif value == 'D':
                    obj_ret = event.Event(KEYDOWN, {'key': 276, 'mod': 0, 'scancode': 100, 'window': None})
                else:
                    pass
            elif value == '\x1b':
                obj_ret = event.Event(KEYDOWN, {'unicode': '\x1b', 'key': 27, 'mod': 0, 'scancode': 9, 'window': None})
            else:
                pass
        else:
            # sequences inconnues
            pass

        return [obj_ret]

    def clock(self):
        # sleep(0.1)
        pass

    def flip(self):
        print('')
        y_unit = 0
        for raw in self._map_cache:
            x_raw = 0
            for unit in raw:
                print(unit, end='')
                x_raw = x_raw + 1
            y_unit = y_unit + 1
        print('')
        print('')

    def event_quit(self, event):
        pass

    def event_keydown_escape(self, event):
        return event.type == KEYDOWN and event.key == K_ESCAPE

    def event_keydown_right(self, event):
        return event.type == KEYDOWN and event.key == K_RIGHT

    def event_keydown_left(self, event):
        return event.type == KEYDOWN and event.key == K_LEFT

    def event_keydown_up(self, event):
        return event.type == KEYDOWN and event.key == K_UP

    def event_keydown_down(self, event):
        return event.type == KEYDOWN and event.key == K_DOWN

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

class FakeEvent :
   def __init__( self, key_code):
       self.type = KEYDOWN
       self.key = key_code
