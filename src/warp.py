"""Warps image to square top-down view given corner coordinates
Expects grayscale image and corners in shape(4,2))"""

import numpy as np
import cv2

TARGET_RES = 380 # 19x20 - goban is 19x19, patches will be 20x20

def sort_corners(corners):
    rect = np.zeros((4, 2), dtype="float32")
    # the top-left point will have the smallest sum, whereas
    # the bottom-right point will have the largest sum
    s = np.sum(corners, axis=1)
    rect[0] = corners[np.argmin(s)]
    rect[2] = corners[np.argmax(s)]
    # now, compute the difference between the points, the
    # top-right point will have the smallest difference,
    # whereas the bottom-left will have the largest difference
    diff = np.diff(corners, axis=1)
    rect[1] = corners[np.argmin(diff)]
    rect[3] = corners[np.argmax(diff)]
    return rect

def warp(img, rect):
    target_corners = np.float32([[0, 0], [TARGET_RES, 0],
                                [TARGET_RES, TARGET_RES], [0, TARGET_RES]])
    M = cv2.getPerspectiveTransform(rect, target_corners)
    warped = cv2.warpPerspective(img, M, (TARGET_RES, TARGET_RES))
    return warped

def top_down_view(img, corners):
    rect = sort_corners(corners)
    result = warp(img, rect)
    return result