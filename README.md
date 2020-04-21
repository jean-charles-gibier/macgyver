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
Les fonctionalités requises pour cet exercice sont [décrites ici](https://openclassrooms.com/fr/projects/156/assignment)

Pour exploiter l'interface graphique pygame, le programme va lire un fichier texte (argument '--datafile') 
de 15x15 caractères séparés par des "retour chariot". Chaque ligne de ce fichier représente une ligne du jeu .<br>
Dans cette ligne, chaque caractère symbolise un des éléments suivants (au choix) :
- une case de jeu standard (char ' ' espace ou Ascii 0x20)
- un élément de mur (char '#' hastag)
- la case de départ (char 'S' )
- la case d'arrivée' (char 'E' )

Ce fichier texte est situé dans le repertoire 'resources'.
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


## Demonstration du respect du motif [MVC](https://fr.wikipedia.org/wiki/Mod%C3%A8le-vue-contr%C3%B4leur)

````
-i {Graphic,Text}, --interface {Graphic,Text}<br>
````
Le découplage des modules "modele", "vue" et "controleur" est mis en oeuvre dans les options de démarrage du programme :<br>
L'option "-i Text" propose l'implémentation d'un mode "Text" avec une animation "old school" dans le style terminal TTY.<br>
Ce mode reprend les principes du jeu "version graphique" en remplacant les sprites par des caractères symboliques et en réaffichant la matrice ainsi constituée 15x15 à chaque appui sur le clavier.<br>

Exemple :

![Rendu](https://raw.githubusercontent.com/jean-charles-gibier/macgyver/develop/docs/Exemple3.png)


```` 
 -d DATAFILE, --datafile DATAFILE.TXT<br>
````
Le découplage des modules "modele" et "controleur" est quand à lui implicite :<br>
Le choix d'un fichier texte servant à mapper la configuration du jeu  démontre l'indépendance des données par rapport au fonctionnement du jeu. Une autre source de données lui serait (à priori :grimacing:) facilement substituable.


## Architecture 

L'architecture (ok c'est un grand mot) de ce projet est [définie ICI](https://github.com/jean-charles-gibier/macgyver/blob/master/docs/architecture.md) 

## Demarche

La description des problèmes / solutions / contournements dans la conception / réalisation de ce projet est [décrite ICI](https://github.com/jean-charles-gibier/macgyver/blob/master/docs/P03_02_Demarche.pdf) 


## TODO

Sugestions pour une nouvelle version:
- Générer un parcours aléatoire (plateau 15 x 15 par defaut)
- Ajouter animation des personages (gare  et Mc Gyver) 2 ou 3 sprites => 1 par rafraichissement en alternance 
- Gérer les evenements clavier par listener
- Afficher explicitement les cases "départ" et "arrivée" (nouvelle clzsse heritée de items => item non récupérable)
