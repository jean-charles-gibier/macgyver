from dal import Dal
import logging as lg
logger = lg.getLogger(__name__)
# import constant


class DalText(Dal):
    """ PyGame implementation """
    def init(self, map_game):
        """inteface intialization ne sert pas à gd chose en mode texte"""
        return format(type(self))

    def load_figure(self):
        """load figure of item
        exemple pygame.image.load ... """
        pass

    def display_figure(self):
        """display figure of item
        exemple blit ... """
        pass

    def draw_map(self, fenetre, map_content):
        y_unit = 0
        for raw in map_content:
            x_raw = 0
            for unit in raw:
                if unit == '#':
                    print('#', end='')
                else:
                    print(' ', end='')
                x_raw = x_raw + 1
                print('')
            y_unit = y_unit + 1
        return

    def draw_footer(self, fenetre):
        pass

    def event_get(self):
        return _Getch()

    def clock(self):
        pass

    def flip(self):
        pass


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

getch = _Getch()
