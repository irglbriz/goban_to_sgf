"""Pulls the whole process together

Entry point for invocation from shell
"""

import argparse
import generate_samples
import find_corners_with_nn
import find_corners_with_contours
import warp
import read_position



def main():
    parser = argparse.ArgumentParser(description="bridge between jpg and sgf")
    parser.add_argument("target", help="input picture")
    # parser.add_argument("-r", "--resolution", type=int, choices =[200,300,400], 
    #                     default=400, help="output resolution")
    # parser.add_argument("-d", "--debug", help="press key to go to next frame",
    #                     action="store_true")
    args = parser.parse_args()

    TARGET_FILE = args.target
    # TARGET_RES = args.resolution
    # DEBUG = args.debug

if __name__ == '__main__':
    main()