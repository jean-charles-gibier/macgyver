''' item and personages description '''
import constant


class Item:
    ''' item definition '''
    def __init__(self, pos_x=0, pos_y=0, img_file=""):
        #        # Sprite de base
        # Position du sprite
        self.case_x = pos_x
        self.case_y = pos_y
        self.value_x = pos_x * constant.UNIT_SIZE
        self.value_y = pos_y * constant.UNIT_SIZE
        self.img_file = img_file
        self.image = None

    def exclude(self, pos):
        ''' Eclude an item or a perso and place it in footer area '''
        self.value_y = constant.UNIT_SIZE * constant.UNITS_PER_ROW
        self.value_x = ((constant.UNIT_SIZE * constant.UNITS_PER_ROW) // 2) + \
                        ((constant.UNIT_SIZE + 10) * pos)
        self.img_file = ""
