#! /usr/bin/env python3
# coding: utf-8

"""This script starts mc Guyver labyrinth parameter is :  file_name (discribing map)."""

import argparse

# test 4 pylint checks
def parse_arguments():
    """Parse_arguments parsing args no parameter."""
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--datafile", help="""TXT file containing map of
        labyrinth""", default="default.txt")
    return parser.parse_args()

def main():
    """Main entry no parameter."""
    args = parse_arguments()



    return args[0]

if __name__ == "__main__":
    main()
