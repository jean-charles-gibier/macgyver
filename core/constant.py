# -*- coding: utf-8 -*- #
''' Constants & paths'''
import os
RESOURCE_PATH = os.path.join(os.getcwd(), "resources")

# size
UNIT_SIZE = 20
FOOTER_SIZE = 20
UNITS_PER_ROW = 15

# type d'environnement
PYGAME_TYPE = 0
TEXT_TYPE = 1

# Listes des images du jeu
IMG_ICON = RESOURCE_PATH + "/icon.png"
IMG_WALL = RESOURCE_PATH + "/mur-20x20.png"
IMG_BACK = RESOURCE_PATH + "/fond.jpg"
IMG_START = RESOURCE_PATH + "/depart.png"
IMG_FINISH = RESOURCE_PATH + "/arrivee.png"
IMG_MCGYVER = RESOURCE_PATH + "/MacGyver.png"
IMG_GARDIEN = RESOURCE_PATH + "/Gardien.png"
IMG_AIGUILLE = RESOURCE_PATH + "/aiguille2.png"
IMG_ETHER = RESOURCE_PATH + "/ether2.png"
IMG_TUBE = RESOURCE_PATH + "/tube_plastique2.png"

# Z_MacGyver parce que tri alpha et que
# MacGyver doit être affiché le dernier
ID_MCGYVER = 'Z_MacGyver'
ID_GARDIEN = 'Gardien'
ID_AIGUILLE = 'Aiguille'
ID_ETHER = 'Ether'
ID_TUBE = 'Tube'
