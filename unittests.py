"""Unittests for every module."""

import numpy as np
import cv2
from distutils import util

import parser
import find_corners_with_contours as fcwc
import warp

# Test the parser by writing sample sgf and reading it again:
testpos = np.full((19,19), 0)
testpos[5,6] = 1
testpos[7,8] = -1
parser.mat_to_sgf(testpos, "data/sgf/conversiontest.sgf")
testpos_looper = parser.sgf_to_mat("data/sgf/conversiontest.sgf")
assert np.array_equal(testpos, testpos_looper), "Parser Fail!"

# Test finding corners by contours with easy sample
photo = fcwc.load_img("data/raw_test/basic.jpg")
corners = fcwc.find_corners(photo)
marked = fcwc.mark_corners(photo, corners)
cv2.imwrite('data/debug/marked.jpg', marked)
visual_check = input("Do green pixels show close to corners in " \
                    "'data/debug/marked.jpg'? \n").lower()
assert util.strtobool(visual_check), "Search by contours failed!"

# Test sorting corners
test_sorted_solution = np.array([[110, 95],
                                 [890, 120],
                                 [800, 900],
                                 [100, 850]])
test_unsorted = test_sorted_solution.copy()
np.random.shuffle(test_unsorted)
test_sorted = warp.sort_corners(test_unsorted)
assert np.array_equal(test_sorted, test_sorted_solution), "Sort corners fail!"

# Test warping
warped = warp.warp_to_gray(photo, warp.sort_corners(corners))
cv2.imwrite('data/debug/warped.jpg', warped)
visual_check = input("Is there a usable topdown view in " \
                    "'data/debug/warped.jpg?' \n").lower()
assert util.strtobool(visual_check), "Warp failed!"

# Test equalization
equalized = warp.equalize(warped)
cv2.imwrite('data/debug/equalized.jpg', equalized)
visual_check = input("Is there a version with more even contrast in " \
                    "'data/debug/equalized.jpg?' \n").lower()
assert util.strtobool(visual_check), "Equalization failed!"

# TODO: Test reading position from preprocessed image

# TODO: Test going all the way from picture to sgf with main module

# TODO: Test generating a sample render with blender

# TODO: Test finding corners by neural net

print("ALL UNIT TESTS PASSED!")