## Architecture / disposition du projet

````
+---macgyver                                       | Racine Projet
    |   .gitignore                                 |
    |   macgyver.py                                | Main program
    |   pylintrc                                   | Ressouces validation pylint
    |   README.md                                  | Ce fichier
    |   requirements.txt                           | Listes des dépendances
    |                                              |
    +---core                                       | Modules du projet
    |   |   constant.py                            | Fchier des constantes 
    |   |   mapgame.py                             | Objet MapGame definissant la carte du jeu
    |   |   utils.py                               | Utilitaires
    |   |   __init__.py                            |
    |   |                                          |
    |   +---dal                                    | dal => pour Display Abstract Layer
    |   |       dal.py                             | classe abstraite dal
    |   |       dalgraphic.py                      | implementation graphique de dal
    |   |       daltext.py                         | implementation texte de dal
    |   |       __init__.py                        |
    |   |                                          |
    |   +---item                                   | description des perso et objets du jeu
    |           item.py                            | classe mere
    |           perso.py                           | Perso (est un item qui se déplace)
    |           __init__.py                        |
    |                                              |
    +---docs                                       | ressources readme
    |       Exemple1.png                           |
    |       Exemple2.png                           |
    |       Exemple3.png                           |
    |       usage.txt                              |
    |                                              |
    +---resources                                  | Sprites / images etc.
    |       aiguille.png                           |
    |       aiguille2.png                          |
    |       big_rooms.txt                          |
    |       decorations.png                        |
    |       default.txt                            |
    |       equipment-32x32.png                    |
    |       ether.png                              |
    |       ether2.png                             |
    |       floor-tiles-20x20.png                  |
    |       Gardien.png                            |
    |       icon.png                               |
    |       items.png                              |
    |       license.txt                            |
    |       lifebar-32x32.png                      |
    |       MacGyver.png                           |
    |       mur-20x20.png                          |
    |       personnages.png                        |
    |       README.md                              |
    |       seringue.png                           |
    |       structures.png                         |
    |       test01.txt                             |
    |       Thumbs.db                              |
    |       tile-crusader-logo.png                 |
    |       tube_plastique.png                     |
    |       tube_plastique2.png                    |
    |                                              |
    +---tests                                      |  tests (tentative)
            pomme.png                              |
            raw_test.py                            |
            test_log.py                            |
            test_pygame.py                         |
````
