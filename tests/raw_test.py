from core import constant, mapgame


def test_something():
    assert True


def test_default_file_map():
    """ Test map resource """
    test_path = 'resources/default.txt'
    mad = mapgame.MapGame(test_path)
    assert mad.path_name == test_path
    # check if we really got a 15x15 sized array
    assert len(mad.map_content) == constant.UNITS_PER_ROW and len(mad.map_content[0].rstrip()) == constant.UNITS_PER_ROW


if __name__ == "__main__":
    test_default_file_map()
