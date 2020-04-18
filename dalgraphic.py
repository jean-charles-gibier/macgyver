from dal import Dal
import logging as lg
import constant
logger = lg.getLogger(__name__)
from pygame.constants import (QUIT, KEYDOWN, K_ESCAPE, K_RIGHT, K_LEFT, K_UP, K_DOWN)
from pygame.rect import Rect
import pygame


class DalGraphic(Dal):
    """ PyGame implementation """
    def init(self, mapgame):
        """inteface intialization"""
        if mapgame.map_type == constant.PYGAME_TYPE:
            pygame.init()
            lg.info('Taille de la fenetre : %d X %d', mapgame.length * constant.UNIT_SIZE,
                    (mapgame.height * constant.UNIT_SIZE) + constant.FOOTER_SIZE)
            fenetre = pygame.display.set_mode(
                (mapgame.length * constant.UNIT_SIZE,
                 (mapgame.height * constant.UNIT_SIZE) + constant.FOOTER_SIZE))
            img_icon = pygame.image.load(constant.IMG_ICON).convert_alpha()
            pygame.display.set_icon(img_icon)
            pygame.display.set_caption('The wonderful game')
            fenetre.fill((200, 200, 200))
            return fenetre

    def draw_map(self, fenetre, map_content):
        """draw map into a window."""
        mur = pygame.image.load(constant.IMG_WALL).convert()
        sol = pygame.Surface((constant.UNIT_SIZE, constant.UNIT_SIZE))

        y_unit = 0
        for raw in map_content:
            x_raw = 0
            for unit in raw:
                if unit == '#':
                    fenetre.blit(mur, (x_raw, y_unit))
                else:
                    fenetre.blit(sol, (x_raw, y_unit))
                x_raw = x_raw + constant.UNIT_SIZE
            y_unit = y_unit + constant.UNIT_SIZE
        return

    def load_item(self, fenetre, item):
        """load item
        exemple pygame.image.load ... """
        item.image = pygame.image.load(item.img_file).convert_alpha()

    def draw_item(self, fenetre, item):
        """display item """
        fenetre.blit(item.image.subsurface(Rect(
            10, 10, constant.UNIT_SIZE, constant.UNIT_SIZE)), (item.value_x, item.value_y))


    def draw_footer(self, fenetre):
        font = pygame.font.Font('freesansbold.ttf', 16)

        # create a text suface object
        text = font.render('Items :', True, (10, 10, 10), (200, 200, 200))

        # create a rectangular object for the
        # text surface object
        textrect = text.get_rect()

        # set the center of the rectangular object.
        textrect.center = (textrect.centerx + 1, constant.UNIT_SIZE *
                           constant.UNITS_PER_ROW + textrect.centery + 1)
        fenetre.blit(text, textrect)

    def clock(self):
        pygame.time.Clock().tick(30)

    def flip(self):
        pygame.display.flip()

    def event_get(self):
        return pygame.event.get()

    def event_quit(self, event):
        return event.type == QUIT

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
