#! /usr/bin/env python3
# coding: utf-8
import pygame
import constant
from pygame.locals import *
from constant import *


class Item:
    def __init__(self, pos_x=0, pos_y=0, img_file=""):
        #        # Sprite de base
        # Position du sprite
        self.case_x = pos_x
        self.case_y = pos_y
        self.x = pos_x * constant.UNIT_SIZE
        self.y = pos_y * constant.UNIT_SIZE
        self.img_file = img_file

    def display(self, fenetre):
        """display current item on main window"""
        self.image = pygame.image.load(self.img_file).convert_alpha()
        fenetre.blit(self.image.subsurface(Rect(10,10,20,20)), (self.x, self.y))

class Perso(Item):
    """Classe permettant de créer un personnage"""

    def __init__(self, pos_x=0, pos_y=0, img_file=""):
        super().__init__(pos_x, pos_y, img_file)

    #        # Sprite du personnage
#        self.image = pygame.image.load(droite).convert_alpha()
        # Position du personnage en cases et en pixels
#        self.case_x = 0
#        self.case_y = 0
#        self.x = 0
#        self.y = 0
        # Direction par défaut
#        self.direction = self.droite
        # Niveau dans lequel le personnage se trouve

    def deplacer(self, direction):
        """Methode permettant de déplacer le personnage"""

        # Déplacement vers la droite
        if direction == 'droite':
            # Pour ne pas dépasser l'écran
            if  False : # self.case_x < (nombre_sprite_cote - 1):
                # On vérifie que la case de destination n'est pas un mur
                if self.niveau.structure[self.case_y][self.case_x + 1] != 'm':
                    # Déplacement d'une case
                    self.case_x += 1
                    # Calcul de la position "réelle" en pixel
                    self.x = self.case_x # * taille_sprite
            # Image dans la bonne direction
            self.direction = self.droite

        # Déplacement vers la gauche
        if direction == 'gauche':
            if self.case_x > 0:
                if self.niveau.structure[self.case_y][self.case_x - 1] != 'm':
                    self.case_x -= 1
                    self.x = self.case_x  # * taille_sprite
            self.direction = self.gauche

        # Déplacement vers le haut
        if direction == 'haut':
            if self.case_y > 0:
                if self.niveau.structure[self.case_y - 1][self.case_x] != 'm':
                    self.case_y -= 1
                    self.y = self.case_y # * taille_sprite
            self.direction = self.haut

        # Déplacement vers le bas
        if direction == 'bas':
            if False : #self.case_y < (nombre_sprite_cote - 1):
                if self.niveau.structure[self.case_y + 1][self.case_x] != 'm':
                    self.case_y += 1
                    self.y = self.case_y * taille_sprite
            self.direction = self.bas

