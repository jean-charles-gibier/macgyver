import abc


class Dal(abc.ABC):
    """Dal stands for display abstraction layer
    the purpose is to release the relationships between
     'control' modules  and  'pygame' and eventually
     to allow other 'view' implementation."""
    def __init__(self):
        super().__init__()

    @abc.abstractmethod
    def init(self, map_game):
        """inteface intialization type insterface : graphic / text """
        pass

    @abc.abstractmethod
    def load_item(self, fenetre, item):
        """load  item
        exemple pygame.image.load ... """
        pass

    @abc.abstractmethod
    def draw_item(self, fenetre, item):
        """display figure of item
        exemple blit ... """
        pass

#   def display_text(self):
#        """display text"""
#        pass

    @abc.abstractmethod
    def draw_map(self, fenetre, map_content):
        pass

    @abc.abstractmethod
    def draw_footer(self, fenetre):
        pass

    @abc.abstractmethod
    def clock(self):
        pass

    @abc.abstractmethod
    def flip(self):
        pass

    @abc.abstractmethod
    def event_get(self):
        pass

    @abc.abstractmethod
    def event_quit(self, event):
        pass

    @abc.abstractmethod
    def event_keydown_escape(self, event):
        pass

    @abc.abstractmethod
    def event_keydown_right(self, event):
        pass

    @abc.abstractmethod
    def event_keydown_left(self, event):
        pass

    @abc.abstractmethod
    def event_keydown_up(self, event):
        pass

    @abc.abstractmethod
    def event_keydown_down(self, event):
        pass
