from core import constant
from core.item.item import Item


class Perso(Item):
    """Classe permettant de créer un personnage"""

    def __init__(self, pos_x=0, pos_y=0, img_file=""):
        super().__init__(pos_x, pos_y, img_file)

    def deplacer(self, direction, autorized_pos):
        """Methode permettant de déplacer le personnage"""

        # Déplacement vers la droite
        if direction == 'droite' and (self.case_x + 1, self.case_y) in autorized_pos:
            self.case_x += 1
            self.value_x += constant.UNIT_SIZE

        # Déplacement vers la gauche
        if direction == 'gauche' and (self.case_x - 1, self.case_y) in autorized_pos:
            self.case_x -= 1
            self.value_x -= constant.UNIT_SIZE

        # Déplacement vers le haut
        if direction == 'haut' and (self.case_x, self.case_y - 1) in autorized_pos:
            self.case_y -= 1
            self.value_y -= constant.UNIT_SIZE

        # Déplacement vers le bas
        if direction == 'bas' and (self.case_x, self.case_y + 1) in autorized_pos:
            self.case_y += 1
            self.value_y += constant.UNIT_SIZE

    def compare_pos(self, other_item):
        if isinstance(other_item, Item) or isinstance(other_item, Perso):
            return (self.value_x, self.value_y) == (other_item.value_x, other_item.value_y)
        elif isinstance(other_item, tuple):
            return (self.case_x, self.case_y) == (other_item[0], other_item[1])
        else:
            raise Exception('cannot compare')
