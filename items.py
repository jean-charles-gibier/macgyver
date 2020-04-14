#! /usr/bin/env python3
# coding: utf-8
import pygame
import constant
from pygame.locals import *


class Item:
    def __init__(self, pos_x=0, pos_y=0, img_file=""):
        #        # Sprite de base
        # Position du sprite
        self.case_x = pos_x
        self.case_y = pos_y
        self.x = pos_x * constant.UNIT_SIZE
        self.y = pos_y * constant.UNIT_SIZE
        self.img_file = img_file
        self.image = pygame.image.load(self.img_file).convert_alpha()
#        self.background = pygame.Surface((constant.UNIT_SIZE, constant.UNIT_SIZE))


    def display(self, fenetre):
        """display current item on main window"""
        fenetre.blit(self.image.subsurface(Rect(10,10,constant.UNIT_SIZE,constant.UNIT_SIZE)), (self.x, self.y))

class Perso(Item):
    """Classe permettant de créer un personnage"""

    def __init__(self, pos_x=0, pos_y=0, img_file=""):
        super().__init__(pos_x, pos_y, img_file)


    def deplacer(self, direction, autorized_pos):
        """Methode permettant de déplacer le personnage"""

        # Déplacement vers la droite
        if direction == 'droite' and (self.case_x + 1, self.case_y) in autorized_pos:
            self.case_x += 1
            self.x += constant.UNIT_SIZE

        # Déplacement vers la gauche
        if direction == 'gauche'and (self.case_x - 1, self.case_y) in autorized_pos:
            self.case_x -= 1
            self.x -= constant.UNIT_SIZE

        # Déplacement vers le haut
        if direction == 'haut'and (self.case_x, self.case_y - 1) in autorized_pos:
            self.case_y -= 1
            self.y -= constant.UNIT_SIZE

        # Déplacement vers le bas
        if direction == 'bas' and (self.case_x, self.case_y + 1) in autorized_pos:
            self.case_y += 1
            self.y += constant.UNIT_SIZE

    def compare_pos(self, other_item):
        if (isinstance(other_item, Item) or isinstance(other_item, Perso)):
            return ((self.x, self.y) == (other_item.x, other_item.y))
        elif (isinstance(other_item, tuple)):
            return ((self.case_x, self.case_y) == (other_item[0], other_item[1]))
        else:
            raise  Exception('cannot compare')
