import os


class MapDescription :
    """ Map description of the game """
    _path_name = ""
    # text par defaut
    _file_type = "text"

    def __init__(self, path_name):
        """ init test if path name exists """
        self._path_name = path_name
        self._check_path_name()
        self._read_map()

    @property
    def path_name(self):
        """ getter path_name """
        return self._path_name

    def _check_path_name(self):
        """ check if path_name is a valid resource"""
        if (os.path.exists(self._path_name) == False):
            raise(Exception("File map not accessible"))

    def _read_map(self):
        """ read the content of file map in private array """
        try:
            with open(self._path_name) as f:
                print(f.readlines())
                # Do something with the file
        except IOError:
            # Log !!
            raise(Exception("File map not accessible"))
