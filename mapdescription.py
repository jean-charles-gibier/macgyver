# coding: utf-8
import os
import constant


class MapDescription:
    """ Map description of the game """
    # name of file descriptor
    _path_name = ""
    # affecte implémentation PYGAME par defaut
    _file_type = constant.PYGAME_TYPE
    # text array that represents the race pver the map
    _file_map = []
    # computed height
    _height_map = 0
    # computed length
    _length_map = 0
    # array of tuples (x,y) of the path course
    _path_course = []

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
    def file_type(self):
        """ getter file_type """
        return self._file_type

    @property
    def file_map(self):
        """ getter file_map """
        return self._file_map

    @property
    def height(self):
        """ getter height_map """
        return self._height_map

    @property
    def length(self):
        """ getter length_map """
        return self._length_map

    def _check_path_name(self):
        """ check if path_name is a valid resource"""
        if (os.path.exists(self._path_name) == False):
            raise (Exception("File map not accessible"))

    def _find_path_course(self):
        """ find path_course into map """
        y_unit = 0
        for raw in self.file_map:
            x_raw = 0
            for unit in raw:
                if unit == '#':
                    self.path_course.append((x_raw, y_unit))

    @property
    def path_course(self):
        """ getter path_course """
        return self._path_course

    def _read_map(self):
        """ read the content of file map in private array """
        try:
            with open(self._path_name) as f:
                self._file_map = f.readlines()
            self._height_map = len(self._file_map)
            self._length_map = len(self._file_map[0].rstrip())
            self._find_path_course()
        except IOError:
            # Log !!
            raise (Exception("File map not accessible"))
