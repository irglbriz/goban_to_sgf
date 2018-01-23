"""Pulls the whole process together

Entry point for invocation from shell
"""
import numpy as numpy
import cv2
import argparse

import find_corners_with_contours as fcwc
import warp
import read_position
import sgf_parser



def main():
    parser = argparse.ArgumentParser(description="bridge between jpg and sgf")
    parser.add_argument("path_to_img", help="photo of goban")
    parser.add_argument("path_to_sgf", help="output file")
    args = parser.parse_args()
    INPUT_FILE = args.path_to_img
    OUTPUT_FILE = args.path_to_sgf

    photo = fcwc.load_img(INPUT_FILE)
    corners = fcwc.find_corners(photo)
    sorted_corners = warp.sort_corners(corners)
    warped = warp.warp_to_gray(photo, sorted_corners)
    equalized = warp.equalize(warped)
    grid = read_position.calculate_grid_points()
    samples = read_position.sample_using_grid(equalized, grid)
    scanned_position = read_position.intensity_to_mat(samples)
    sgf_parser.mat_to_sgf(scanned_position, OUTPUT_FILE)


if __name__ == '__main__':
    main()