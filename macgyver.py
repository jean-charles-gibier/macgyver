#! /usr/bin/env python3
# coding: utf-8
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d","--datafile",help="""TXT file containing map of
        labyrinth""")

def main():
    args = parse_arguments()

if __name__ == "__main__":
    main()