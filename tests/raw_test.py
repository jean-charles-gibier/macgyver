import sys
sys.path.append('..')
sys.path.append('.')

import mapdescription

def test_something():
    assert True

def test_default_file_map():
    """ Test map resource """
    test_path = 'D:\\work\\source\\repos\\macgyver\\resources\\default.txt'
    mad = mapdescription.MapDescription(test_path)
    assert mad.path_name == test_path
    # check if we really got a 15x15 sized array
    assert len(mad.file_map) == 15 and len(mad.file_map[0]) == 15

if __name__ == "__main__":
    test_default_file_map()
