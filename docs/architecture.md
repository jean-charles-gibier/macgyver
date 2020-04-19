## Architecture / disposition du projet

````
+---macgyver                                       | Racine Projet
    |   .gitignore                                 |
    |   macgyver.py                                | Main program
    |   pylintrc                                   | ressouces validation pylint
    |   README.md                                  | 
    |   requirements.txt                           |
    |   __init__.py                                |
    |                                              |
    +---core                                       |
    |   |   constant.py                            |
    |   |   mapgame.py                             |
    |   |   utils.py                               |
    |   |   __init__.py                            |
    |   |                                          |
    |   +---dal                                    |
    |   |       dal.py                             |
    |   |       dalgraphic.py                      |
    |   |       daltext.py                         |
    |   |       __init__.py                        |
    |   |                                          |
    |   +---item                                   |
    |           item.py                            |
    |           perso.py                           |
    |           __init__.py                        |
    |                                              |
    +---docs                                       |
    |       Exemple1.png                           |
    |       Exemple2.png                           |
    |       Exemple3.png                           |
    |       usage.txt                              |
    |                                              |
    +---resources                                  |
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
    +---tests                                      |
            pomme.png                              |
            raw_test.py                            |
            test_log.py                            |
            test_pygame.py                         |
````
