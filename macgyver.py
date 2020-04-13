#! /usr/bin/env python3
# coding: utf-8

"""This script starts mc Guyver labyrinth parameter is :  file_name (discribing map)."""
import pygame
from pygame.locals import *
from pprint import pprint as print, pprint
from sys import stdout
import logging as lg
import argparse
import constant
import random
import os

from mapdescription import MapDescription
from items import *


def parse_arguments():
    """Parse_arguments parsing args
     parameters :
        --datafile : name of file map without extension """
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--datafile", help="""TXT file containing map of
        labyrinth""", default="default.txt")
    return parser.parse_args()


def set_logger():
    """set log environement."""
    # Set logging stuff
    fh = lg.StreamHandler(stdout)
    formatter = lg.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(message)s')
    fh.setFormatter(formatter)
    logger = lg.getLogger()
    logger.addHandler(fh)
    logger.setLevel(lg.DEBUG)


def read_map(map_name):
    """Check and read content of map."""
    map_path = constant.RESOURCE_PATH
    local_path = os.path.dirname(os.path.realpath(__file__))
    data_file = os.path.join(local_path, map_path, map_name)
    map_description = MapDescription(data_file)
    return map_description


def draw_map(map, fenetre):
    """draw map into a window."""
    mur = pygame.image.load(constant.IMG_WALL).convert()
    sol = pygame.Surface((constant.UNIT_SIZE, constant.UNIT_SIZE))

    y_unit = 0
    for raw in map.map_content:
        x_raw = 0
        for unit in raw:
            if unit == '#':
                fenetre.blit(mur, (x_raw, y_unit))
            else:
                fenetre.blit(sol, (x_raw, y_unit))
            x_raw = x_raw + constant.UNIT_SIZE
        y_unit = y_unit + constant.UNIT_SIZE
    return


def env_decorator(fonction):
    """Just 4 test decorator feature :
    we just multiply the number of colums/rows by pixels size """

    def wrapper(*args, **kw):
        #       pprint(args)
        #       modified = [n * constant.UNIT_SIZE for n in args]
        return fonction(*args, **kw)

    return wrapper


@env_decorator
def init_graphical_env(map):
    """Set graphical envirpnnement type ."""
    if (map.map_type == constant.PYGAME_TYPE):
        pygame.init()
        lg.info('Taille de la fenetre : %d X %d', map.height * constant.UNIT_SIZE, map.length * constant.UNIT_SIZE)
        fenetre = pygame.display.set_mode((map.height * constant.UNIT_SIZE, map.length * constant.UNIT_SIZE))
        return fenetre

def dispatch_items(map):
    """" repartir les différent items dans l'aire du jeu en prenant soin
    que la disposition ne bloque pas le joueur """
    # set guard perso
    McGyver = Perso(map.xy_start_point[0], map.xy_start_point[1], constant.IMG_MCGYVER)
    # how many places
    nb_pos = len(map.possible_path)
    p1 = random.choice(range((int)(nb_pos/2), nb_pos))
    Guard = Perso((map.possible_path[p1])[0], (map.possible_path[p1])[1], constant.IMG_GARDIEN)
    p2 = random.choice(range(4, p1))
    Needle = Item((map.possible_path[p2])[0], (map.possible_path[p2])[1], constant.IMG_AIGUILLE)
    p3 = random.choice(range(3, p2))
    Ether = Item((map.possible_path[p3])[0], (map.possible_path[p3])[1], constant.IMG_ETHER)
    p4 = random.choice(range(2, p3))
    Tube = Item((map.possible_path[p4])[0], (map.possible_path[p4])[1], constant.IMG_TUBE)

    return McGyver, Guard, Needle, Ether, Tube

def main():
    """Main entry no parameter."""
    args = parse_arguments()
    # prepare les logs
    set_logger()
    # lit le fichier map
    map_description = read_map(args.datafile)
    lg.info('Map description loaded: %s', map_description.path_name)

    fenetre = init_graphical_env(map_description)
    lg.info('Graphical env set : %s', map_description.path_name)

    (McGyver, Guard, Needle, Ether, Tube) = dispatch_items(map_description)
    lg.info('Dispatch items set')

    # main loop
    continuer = 1
    while continuer:
        draw_map(map_description, fenetre)
        McGyver.display(fenetre)
        Guard.display(fenetre)
        Needle.display(fenetre)
        Ether.display(fenetre)
        Tube.display(fenetre)
        pygame.display.flip()
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():

            # Boucle event
            if event.type == QUIT:
                continuer = 0

            elif event.type == KEYDOWN:
                # Si l'utilisateur presse Echap ici, on revient seulement au menu
                if event.key == K_ESCAPE:
                    continuer = 0

                # Todo a gerer par event / listener
                elif event.key == K_RIGHT:
                    McGyver.deplacer('droite', map_description.path_course)
                elif event.key == K_LEFT:
                    McGyver.deplacer('gauche', map_description.path_course)
                elif event.key == K_UP:
                    McGyver.deplacer('haut', map_description.path_course)
                elif event.key == K_DOWN:
                    McGyver.deplacer('bas', map_description.path_course)
    return


if __name__ == "__main__":
    main()
