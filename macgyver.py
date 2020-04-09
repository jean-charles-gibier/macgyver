#! /usr/bin/env python3
# coding: utf-8

"""This script starts mc Guyver labyrinth parameter is :  file_name (discribing map)."""

import argparse
import constant
import os

from mapdescription import MapDescription

def parse_arguments():
    """Parse_arguments parsing args no parameter."""
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--datafile", help="""TXT file containing map of
        labyrinth""", default="default.txt")
    return parser.parse_args()

def read_map(map_name):
    """Check and read content of map."""
    map_path = constant.RESOURCE_PATH
    local_path = os.path.dirname(os.path.realpath(__file__))
    data_file = os.path.join( local_path, map_path, map_name)
    map_description = MapDescription(data_file)
    return map_description

def main():
    """Main entry no parameter."""
    args = parse_arguments()
    map_description = read_map(args.datafile)
    print(map_description.path_name)
    return

if __name__ == "__main__":
    main()
