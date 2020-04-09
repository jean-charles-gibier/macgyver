import os


class MapDescription :
    """ Map description of the game """
    _path_name = ""
    # text par defaut
    _file_type = "text"
    # text representation of the map
    _file_map = []

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
    def file_map(self):
        """ getter file_map """
        return self._file_map

    def _check_path_name(self):
        """ check if path_name is a valid resource"""
        if (os.path.exists(self._path_name) == False):
            raise(Exception("File map not accessible"))

    def _read_map(self):
        """ read the content of file map in private array """
        try:
            with open(self._path_name) as f:
                self._file_map = f.readlines()
                # print(f.readlines())
        except IOError:
            # Log !!
            raise(Exception("File map not accessible"))
