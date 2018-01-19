"""Warps image to square top-down view given corner coordinates

Expects grayscale image and corners in shape(4,2))"""

# Inspiration and code snippets from https://www.pyimagesearch.com

import numpy as np
import cv2

TARGET_RES = 400

def sort_corners(corners):
    """Sorts corners to (tl, tr, br, bl)."""
    rect = np.zeros((4,2), dtype = "float32")
    # the top-left point will have the smallest sum, whereas
    # the bottom-right point will have the largest sum
    s = np.sum(corners, axis=1)
    rect[0] = corners[np.argmin(s)]
    rect[2] = corners[np.argmax(s)]
    # now, compute the difference between the points, the
    # top-right point will have the smallest difference,
    # whereas the bottom-left will have the largest difference
    diff = np.diff(corners, axis = 1)
    rect[1] = corners[np.argmin(diff)]
    rect[3] = corners[np.argmax(diff)]
    return rect

def warp_to_gray(img, rect):
    """Actual transform, result is already cropped by process."""
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rows, cols= gray.shape
    assert (rows >= TARGET_RES and cols >= TARGET_RES), "input res too low"
    target_corners = np.float32([[0, 0], [TARGET_RES, 0], 
                                [TARGET_RES, TARGET_RES], [0, TARGET_RES]])
    M = cv2.getPerspectiveTransform(rect, target_corners)
    warped = cv2.warpPerspective(gray, M, (TARGET_RES, TARGET_RES))
    return warped

def equalize(gray):
    """adaptive histogram equalization"""
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    return clahe.apply(gray)

def main():
    pass

if __name__ == '__main__':
    main()