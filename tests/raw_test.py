import sys
sys.path.append('..')
sys.path.append('.')

import mapdescription

def test_something():
    assert True

def test_default_file_map():
    test_path = 'D:\\work\\source\\repos\\macgyver\\resources\\default.txt'
    mad = mapdescription.MapDescription(test_path)
    assert mad.path_name == test_path