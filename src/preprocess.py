import numpy as np
import cv2

def equalize_and_crop(gray):
    # crop
    if gray.shape[0] == gray.shape[1]:
        cropped = gray
    elif gray.shape[0] > gray.shape[1]:
        vertical_crop = (gray.shape[0] - gray.shape[1])
        top_crop = bottom_crop = vertical_crop // 2
        if vertical_crop%2 != 0:
            bottom_crop = top_crop + 1
        cropped = gray[top_crop:-bottom_crop,:]
    else:
        print("we're in leftright branch")
        horizontal_crop = (gray.shape[1] - gray.shape[0])
        left_crop = right_crop = horizontal_crop // 2
        if horizontal_crop%2 != 0:
            right_crop = top_crop + 1
        cropped = gray[:,left_crop:-right_crop]
    #equalize
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    equalized = clahe.apply(cropped)
    return equalized