# macgyver
Cours python Openclassrooms 1ere mission

# description des fonctionalités
## usage
````
usage: macgyver.py [-h] [-d DATAFILE]

optional arguments:
  -h, --help            show this help message and exit
  -d DATAFILE, --datafile DATAFILE.TXT
                        file containing map of labyrinth
````
# fonctionalités
En exploitant les services de l'interface graphique pygame, le programme va lire un fichier texte (argument '--datafile') 
de 15x15 caractères séparés par des "retour chariot". Chaque ligne du texte représente une ligne du jeu et chaque caractère de la ligne représente au choix :
- une case de jeu standard (char ' ' espace ou Ascii 0x20)
- un élément de mur (char '#' hastag)
- la case de départ (char 'S' )
- la case d'arrivée' (char 'E' )

Ce fichier est situé dans le repertoire 'resources'.
Le programme interprète le plan du fichier et place 3 items (Aiguille, Tube, Ether) plus un personnage (Gardien) sur les cases accessibles du plan.<br>
(les items seront disposés de manière à ne pas bloquer le jeu : le garde ne devra pas bloquer l'accès aux items à collecter )

Exemple :
````
#             #
#             #
# ######### ###
#       #     S
####### #######
#     #       #
# #   #       #
# #   #       #
# #   #       #
# ### ###### ##
# #           #
# #############
#             #
#             #
############E##
````
Donne le rendu :

![Rendu](https://raw.githubusercontent.com/jean-charles-gibier/macgyver/develop/docs/Exemple1.png)


# TODO
Ajouter une abstraction/implementation pour par exemple utiliser une interface textuelle

generer un parcours aléatoire (plateau 15 x 15 par defaut)

ajouter animation

gerer les evenements clavier par listener

animer le garde
