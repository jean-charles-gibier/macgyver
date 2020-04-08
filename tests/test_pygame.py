# -*- coding: utf-8 -*-
import pygame
import time
import os
local_dir = os.path.dirname(os.path.realpath(__file__))
pygame.display.init()
ecran = pygame.display.set_mode((640, 480)) #Crée la fenêtre de tracé
image = pygame.image.load(local_dir + "/pomme.png") #charge une image à partir d'un fichier
ecran.blit(image, (0,0)) #Colle l'image en haut à gauche de la fenêtre de tracé (ici, l'ecran)
pygame.display.flip() #L'affichage devient effectif : l'image est rendue visible.
time.sleep(1)
pygame.quit()
