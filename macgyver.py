#! /usr/bin/env python3
# coding: utf-8

"""This script starts mc Guyver labyrinth parameter is :  file_name (discribing map)."""
import utils
import random
from perso import *
from item import *
from mapgame import MapGame
import logging as lg
logger = lg.getLogger(__name__)


def draw_footer(fenetre):
    """draw footer into a window."""
    font = pygame.font.Font('freesansbold.ttf', 16)

    # create a text suface object
    text = font.render('Items :', True, (10,10,10), (200,200,200))

    # create a rectangular object for the
    # text surface object
    textRect = text.get_rect()

    # set the center of the rectangular object.
    textRect.center = (textRect.centerx + 1 , constant.UNIT_SIZE * constant.UNITS_PER_ROW + textRect.centery + 1)
    fenetre.blit(text, textRect)
    return


def init_graphical_env(map):
    """Set graphical envirpnnement type ."""
    if (map.map_type == constant.PYGAME_TYPE):
        pygame.init()
        lg.info('Taille de la fenetre : %d X %d', map.length * constant.UNIT_SIZE, (map.height * constant.UNIT_SIZE) + constant.FOOTER_SIZE)
        fenetre = pygame.display.set_mode((map.length * constant.UNIT_SIZE, (map.height * constant.UNIT_SIZE) + constant.FOOTER_SIZE))
        img_icon = pygame.image.load(constant.IMG_ICON).convert_alpha()
        pygame.display.set_icon(img_icon)
        pygame.display.set_caption('The wonderful game')
        fenetre.fill( (200, 200, 200))
        return fenetre

def dispatch_items(map):
    """" dispatch the different items in the play area taking care
    that the layout does not block the player """
    # set McGyver personage
    McGyver = Perso(map.xy_start_point[0], map.xy_start_point[1], constant.IMG_MCGYVER)
    # how many boxes are accessible
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
    args = utils.parse_arguments()
    # prepare les logs
    utils.set_logger()
    # lit le fichier map
    map_game = MapGame(args.datafile)
    lg.info('Map description loaded: %s', map_game.path_name)

    fenetre = init_graphical_env(map_game)
    lg.info('Graphical env set : %s', map_game.path_name)

    (McGyver, Guard, Needle, Ether, Tube) = dispatch_items(map_game)
    lg.info('Dispatch items set')

    # collected items
    collected_items = []

    # main loop
    continuer = 1
    while continuer:
        map_game.draw_map(fenetre)
        draw_footer(fenetre)
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
                # Si l'utilisateur presse Echap ici, on sort
                if event.key == K_ESCAPE:
                    continuer = 0
                elif event.key == K_RIGHT:
                    McGyver.deplacer('droite', map_game.path_course)
                elif event.key == K_LEFT:
                    McGyver.deplacer('gauche', map_game.path_course)
                elif event.key == K_UP:
                    McGyver.deplacer('haut', map_game.path_course)
                elif event.key == K_DOWN:
                    McGyver.deplacer('bas', map_game.path_course)

                # check items
                if McGyver.compare_pos(Guard):
                    lg.info('On rencontre le garde ')
                    if len(collected_items) == 3:
                        lg.info('Ok Garde endormi ')
                        Guard.y = constant.UNIT_SIZE * constant.UNITS_PER_ROW
                        Guard.x = ((constant.UNIT_SIZE * constant.UNITS_PER_ROW) // 2) + ((constant.UNIT_SIZE + 10) * 4)
                    else:
                        lg.info('You loose !')

                elif McGyver.compare_pos(Needle):
                    lg.info('On rencontre l''aiguille ')
                    collected_items.append(Needle)
                    Needle.y = constant.UNIT_SIZE * constant.UNITS_PER_ROW
                    Needle.x = (constant.UNIT_SIZE * constant.UNITS_PER_ROW) // 2

                elif McGyver.compare_pos(Ether):
                    collected_items.append(Ether)
                    lg.info('On rencontre la bouteille d''ether ')
                    Ether.y = constant.UNIT_SIZE * constant.UNITS_PER_ROW
                    Ether.x = ((constant.UNIT_SIZE * constant.UNITS_PER_ROW) // 2) + (constant.UNIT_SIZE + 10)

                elif McGyver.compare_pos(Tube):
                    collected_items.append(Tube)
                    lg.info('On rencontre le tube ')
                    Tube.y = constant.UNIT_SIZE * constant.UNITS_PER_ROW
                    Tube.x = ((constant.UNIT_SIZE * constant.UNITS_PER_ROW) // 2) + ((constant.UNIT_SIZE + 10) * 2)

                elif McGyver.compare_pos((map_game.xy_end_point[0], map_game.xy_end_point[1])):
                    if len(collected_items) == 3:
                        lg.info('You win !')
    return


if __name__ == "__main__":
    main()
