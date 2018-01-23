"""Reads game position from normalized input and saves as sgf file"""

import numpy as np
import cv2

import parser

def estimate_stone_size(img):
    """Estimates radius of stones in pixels"""
    # edge case empty board
    # must be less than grid step size
    # use hughe circles?
    return 18   # guess while in development

def estimate_grid_step_size(img, boardsize=19):
    """Estimates distance of row/col lines in pixels"""
    # edge case rather full board
    # only can change so much based on how wide 'frame' is
    # use huge lines?
    # constrained: min stone size, max board size/19
    return 21   # guess while in development

def calculate_grid_points(resolution=400, grid_step_size=21, boardsize=19):
    """Returns matrix of grid coordinates"""
    # best use center of image as center of grid matrix
    # as frame width is unclear
    
    grid = np.zeros((boardsize,boardsize,2), dtype=np.uint16)
    corner = (resolution // 2) - ((boardsize // 2) * grid_step_size)
    for x in range(boardsize):
        for y in range(boardsize):
            # since stones have thickness for perspective correction
            # move grid one or two pixels towards top
            grid[x,y,0] = corner + (x * grid_step_size) - 1
            grid[x,y,1] = corner + (y * grid_step_size)
    return grid

def sample_using_point(img, pos=(200,200), stone_size=18):
    """Returns average intensity around 'pos'"""
    window_shift = stone_size // 4                  #4
    window_length = 2 * window_shift + 1            #9
    window_pixels = window_length * window_length   #81
    aggregate = int(0)
    for x in range(window_length):
        for y in range(window_length):
            sample_x = pos[0] - window_shift + x
            sample_y = pos[1] - window_shift + y
            aggregate += img[sample_x,sample_y]
    return aggregate / window_pixels

def sample_using_grid(img, grid):
    """Returns intensity matrix by sampling pixels around grid points"""
    stone_size = estimate_stone_size(img)
    samples = np.zeros((grid.shape[0],grid.shape[1]),np.dtype(float))
    for x in range(samples.shape[0]):
        for y in range(samples.shape[1]):
            pos = grid[x,y]
            samples[x,y] = sample_using_point(img, pos, stone_size)
    return samples

def calculate_intensity_thresholds(samples):
    """Calculates reasonable intensity values to classify samples"""
    median = np.median(samples)
    minimum = np.min(samples)
    maximum = np.max(samples)
    lower = minimum + (0.4 * (median - minimum))
    higher = maximum - (0.7 * (maximum - median))
    return lower, higher

def intensity_to_move(value, lower, higher):
    """Returns -1, 0 or 1 for white stone, empty or black"""
    if (value < lower):
        return 1
    if (value > higher):
        return -1
    else:
        return 0

def intensity_to_mat(samples):
    """Returns matrix of position inferred from intensity samples"""
    position = np.zeros((19,19), np.int)
    lower, higher = calculate_intensity_thresholds(samples)
    for x in range(samples.shape[0]):
        for y in range(samples.shape[1]):
            position[x,y] = intensity_to_move(samples[x,y], lower, higher)
    return position
