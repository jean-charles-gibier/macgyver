import argparse
from sys import stdout
import logging as lg
logger = lg.getLogger(__name__)


def parse_arguments():
    """Parse_arguments parsing args
     parameters :
        --datafile : name of file map without extension """
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--datafile", help="""TXT file containing map of
        labyrinth""", default="default.txt")
    return parser.parse_args()


def set_logger():
    """set log environement."""
    # Set logging stuff
    fh = lg.StreamHandler(stdout)
    formatter = lg.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(message)s')
    fh.setFormatter(formatter)
    logger = lg.getLogger()

    logger.addHandler(fh)
    logger.setLevel(lg.DEBUG)

