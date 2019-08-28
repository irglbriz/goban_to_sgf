import numpy as np
import cv2

def equalize_and_crop(gray):
    #equalize
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    img = clahe.apply(gray)
    
    #crop
    if photo.shape[0] == photo.shape[1]:
        return img
    elif photo.shape[0] > photo.shape[1]:
        vertical_crop = (photo.shape[0] - photo.shape[1])
        top_crop = bottom_crop = vertical_crop // 2
        if vertical_crop%2 != 0:
            bottom_crop = top_crop + 1
        return img[top_crop:bottom_crop,:]
    else:
        horizontal_crop = (photo.shape[1] - photo.shape[0])
        left_crop = right_crop = horizontal_crop // 2
        if horizontal_crop%2 != 0:
            right_crop = top_crop + 1
        return img[:,left_crop:right_crop]