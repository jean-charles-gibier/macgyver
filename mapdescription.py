# coding: utf-8
import os
import constant


class MapDescription:
    """ Map description of the game """
    # name of file descriptor
    _path_name = ""
    # affecte implémentation PYGAME par defaut
    _map_type = constant.PYGAME_TYPE
    # text array that represents the race pver the map
    _map_content = []
    # computed height
    _height_map = 0
    # computed length
    _length_map = 0
    # array of tuples (x,y) of the path course
    _path_course = []
    # coord (x,y) items
    _xy_items = {}

    def __init__(self, path_name):
        """ init test if path name exists """
        self._path_name = path_name
        self._check_path_name()
        self._read_map()

    @property
    def path_name(self):
        """ getter path_name """
        return self._path_name

    @property
    def map_type(self):
        """ getter map_type """
        return self._map_type

    @property
    def map_content(self):
        """ getter map_content """
        return self._map_content

    @property
    def height(self):
        """ getter height_map """
        return self._height_map

    @property
    def length(self):
        """ getter length_map """
        return self._length_map

    @property
    def path_course(self):
        """ getter path_course """
        return self._path_course

    @property
    def xy_start_point(self):
        """ getter xy_start_point """
        return self._xy_items['S']

    @property
    def xy_end_point(self):
        """ getter xy_end_point """
        return self._xy_items['E']

    @property
    def xy_guardian(self):
        """ getter xy_guardian """
        return self._xy_items['G']

    @property
    def xy_tube(self):
        """ getter xy_tube """
        return self._xy_items['T']

    @property
    def xy_syringe(self):
        """ getter xy_syringe """
        return self._xy_items['Y']

    @property
    def xy_needle(self):
        """ getter xy_needle  """
        return self._xy_items['N']

    def _check_path_name(self):
        """ check if path_name is a valid resource"""
        if (os.path.exists(self._path_name) == False):
            raise (Exception("File map not accessible"))

    def _find_path_course(self):
        """ find path_course into map
        fill an array of tuples (x,y) that indicates the allowed path """
        y_unit = 0
        for raw in self.map_content:
            x_raw = 0
            for unit in raw.rstrip():
                if unit != '#':
                    self.path_course.append((x_raw, y_unit))
                    if unit != ' ':
                        self._xy_items[unit] = (x_raw, y_unit)
                x_raw = x_raw + 1
            y_unit = y_unit + 1

    def _read_map(self):
        """ read the content of file map in private array """
        try:
            with open(self._path_name) as f:
                self._map_content = f.readlines()
            self._height_map = len(self._map_content)
            self._length_map = len(self._map_content[0].rstrip())
            self._find_path_course()
        except IOError:
            # Log !!
            raise (Exception("File map not accessible"))
