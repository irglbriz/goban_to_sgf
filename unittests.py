"""Unittests for every module."""

import numpy as np
import cv2
from distutils import util

import sgf_parser
import find_corners_with_contours as fcwc
import warp
import read_position

# Test the parser by writing sample sgf and reading it again
testpos = np.full((19,19), 0)
testpos[5,6] = 1
testpos[7,8] = -1
sgf_parser.mat_to_sgf(testpos, "data/sgf/conversiontest.sgf")
testpos_looper = sgf_parser.sgf_to_mat("data/sgf/conversiontest.sgf")
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

# Test grid function
intersections_marked_bgr = cv2.cvtColor(equalized.copy(), cv2.COLOR_GRAY2RGB)
grid = read_position.calculate_grid_points()
for x in range(19):
    for y in range(19):
        intersections_marked_bgr[grid[x,y,0], grid[x,y,1], 1] = 255
cv2.imwrite('data/debug/intersections_marked.jpg', intersections_marked_bgr)
visual_check = input("Are intersections marked properly in " \
                    "'data/debug/intersections_marked.jpg?' \n").lower()
assert util.strtobool(visual_check), "Grid Calculation failed!"

# Test Sampling
smpl_target = equalized
cv2.imwrite('data/debug/median_blur.jpg', smpl_target)
point_sample_black = read_position.sample_using_point(smpl_target, (180,266))
print("Point sample black value is: {}".format(point_sample_black))

point_sample_empty = read_position.sample_using_point(smpl_target, (222,200))
print("Point sample empty value is: {}".format(point_sample_empty))

point_sample_white = read_position.sample_using_point(smpl_target, (200,266))
print("Point sample white value is: {}".format(point_sample_white))

samples = read_position.sample_using_grid(smpl_target, grid)
print("Sample mean is: {}".format(np.mean(samples)))
print("Sample median is: {}".format(np.median(samples)))
print("Sample minimum is: {}".format(np.min(samples)))
print("Sample maximum is: {}".format(np.max(samples)))

# Test reading position using grid and sample functions
scanned_position = read_position.intensity_to_mat(samples)
solution = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 1,-1,-1, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 1, 0, 0, 0, 0, 0, 1,-1, 0,-1, 0,-1,-1, 1, 0, 0],
                     [0, 0,-1,-1, 0, 1, 0, 0,-1, 1, 0,-1,-1, 0,-1, 1, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1, 1, 1, 0,-1, 0, 1, 0, 0],
                     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
                     [0, 0,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,-1,-1, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1, 1, 1, 1],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,-1,-1,-1, 1],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1,-1,-1, 1, 1, 1, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1, 1, 0, 1,-1, 0],
                     [0, 0,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1, 1, 1,-1, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1, 1,-1, 1, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1, 0,-1, 1,-1,-1, 0],
                     [0, 0,-1, 0, 0, 0, 0, 0, 0, 1, 0, 1,-1, 0,-1, 1, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 1, 0,-1, 0, 0, 1,-1, 1,-1, 1,-1, 0, 0],
                     [0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1,-1,-1, 1,-1,-1, 0, 0],
                     [0, 0, 0, 0, 0, 1,-1, 1,-1, 0,-1,-1, 1, 1, 1, 1,-1,-1, 0],
                     [0, 0, 0, 0, 0, 0, 1,-1, 0,-1,-1, 0,-1, 1, 1, 0, 1,-1, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0,-1, 0, 0,-1, 0, 1, 0, 1, 0, 1, 0]])
assert np.array_equal(scanned_position,solution), "Read Position Fail!"

# TODO: Test going all the way from picture to sgf with main module

# TODO: Fully automate tests

print("ALL UNIT TESTS PASSED!")