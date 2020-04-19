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
  -i {Graphic,Text}, --interface {Graphic,Text}
                        Display interface : 'text' or 'graphic'
````
# fonctionalités
Les fonctionalités requise pour cet exercice sont [décrites ici](https://openclassrooms.com/fr/projects/156/assignment)

En exploitant les services de l'interface graphique pygame, le programme va lire un fichier texte (argument '--datafile') 
de 15x15 caractères séparés par des "retour chariot". Chaque ligne du texte représente une ligne du jeu .<br>
Chaque caractère de la ligne représentera un des éléments suivants au choix :
- une case de jeu standard (char ' ' espace ou Ascii 0x20)
- un élément de mur (char '#' hastag)
- la case de départ (char 'S' )
- la case d'arrivée' (char 'E' )

Ce fichier est situé dans le repertoire 'resources'.
Le programme interprète le plan du fichier et place 3 items (Aiguille, Tube, Ether) plus un personnage (Gardien), au hasard sur les cases accessibles du plan.<br>

(les items seront disposés de manière à ne pas bloquer le jeu : le garde ne devra pas bloquer l'accès aux items à collecter)

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

En fin de partie les items collecté et le garde anihilé apparaissent dans la barre du bas.

![Rendu](https://raw.githubusercontent.com/jean-charles-gibier/macgyver/develop/docs/Exemple2.png)


##Mode de fonctionnement rudimentaire :

Pour démontrer le bon découplage des modules "vue" et "controle" dans la conception, le programme
implémente un mode "Text" proposant un animation "old terminal".
Ce mode reprend les mêmes principes de jeu en remplacant les sprites par des caractères les symbolisant.

Exemple :

![Rendu](https://raw.githubusercontent.com/jean-charles-gibier/macgyver/develop/docs/Exemple3.png)


# TODO
generer un parcours aléatoire (plateau 15 x 15 par defaut)

ajouter animation

gerer les evenements clavier par listener

animer le garde
