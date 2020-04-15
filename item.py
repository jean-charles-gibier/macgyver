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

    def display(self, fenetre):
        """display current item on main window"""
        fenetre.blit(self.image.subsurface(Rect(10, 10, constant.UNIT_SIZE, constant.UNIT_SIZE)), (self.x, self.y))
