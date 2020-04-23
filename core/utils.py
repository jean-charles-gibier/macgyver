import argparse
import logging as lg
import sys
from sys import (stdout, path)

logger = lg.getLogger(__name__)


def parse_arguments():
    """Parse_arguments parsing args
     parameters :
        --datafile : name of file map without extension """
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--datafile", help="""TXT file containing map of
        labyrinth""", default="default.txt")
    parser.add_argument("-i", "--interface", help="""Display interface :
        'text' or 'graphic'""", default="Graphic", choices=['Graphic', 'Text'])
    return parser.parse_args()


def set_logger():
    """set log environement."""
    # Set logging stuff
    fh = lg.StreamHandler(stdout)
    formatter = lg.Formatter('%(asctime)s - %(levelname)s -'
                             ' %(filename)s - %(funcName)s - %(message)s')
    fh.setFormatter(formatter)
    logger = lg.getLogger()

    logger.addHandler(fh)
    logger.setLevel(lg.DEBUG)


def build_display(module_dal_path, interface_type):
    """generate and return a display class """
    dal_prefix = "Dal"
    sys.path.append(module_dal_path)
    class_name = dal_prefix + interface_type
    module_display = class_name.lower()
    lg.info('Implementation : %s', module_display)
    module = __import__(module_display)
    class_ = getattr(module, class_name)
    return  class_()
