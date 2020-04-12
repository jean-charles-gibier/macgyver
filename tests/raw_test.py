import sys
sys.path.append('..')
sys.path.append('.')

import mapdescription
import constant

def test_something():
    assert True

def test_default_file_map():
    """ Test map resource """
    test_path = 'resources/default.txt'
    mad = mapdescription.MapDescription(test_path)
    assert mad.path_name == test_path
    # check if we really got a 15x15 sized array
    assert len(mad.file_map) == constant.UNITS_PER_ROW and len(mad.file_map[0].rstrip()) == constant.UNITS_PER_ROW

if __name__ == "__main__":
    test_default_file_map()
