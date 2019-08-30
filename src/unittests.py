"""Unittests for every module."""

import numpy as np
import cv2
from distutils import util

import sgf_parser
import find_corners as fc
import preprocess
import read_position
import warp

# TODO: Test crop

# TODO: Test warp

# TODO: Test finding corners

# Test sorting corners
test_sorted_solution = np.array([[110, 95],
                                 [890, 120],
                                 [800, 900],
                                 [100, 850]])
test_unsorted = test_sorted_solution.copy()
np.random.shuffle(test_unsorted)
test_sorted = warp.sort_corners(test_unsorted)
assert np.array_equal(test_sorted, test_sorted_solution), "Sort corners fail!"

# TODO: Test sampling

# TODO: Test classifying fields

# Test the parser by writing sample sgf and reading it again
testpos = np.full((19, 19), 0)
testpos[5, 6] = 1
testpos[7, 8] = -1
sgf_parser.mat_to_sgf(testpos, "data/sgf/conversiontest.sgf")
testpos_looper = sgf_parser.sgf_to_mat("data/sgf/conversiontest.sgf")
assert np.array_equal(testpos, testpos_looper), "Parser Fail!"

# TODO: Test going all the way from picture to sgf with main module automatically

print("ALL UNIT TESTS PASSED!")