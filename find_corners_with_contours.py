"""Outputs corners of goban via contour search."""

# Inspiration and code snippets from https://www.pyimagesearch.com

import numpy as np
import cv2

def load_img(pathname):
    img = cv2.imread(pathname)
    rows, cols, ch = img.shape
    print('image loaded with resolution {0}'.format(img.shape))
    return img


def find_corners(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    blurred = cv2.GaussianBlur(gray, (5,5), 0)

    edged = cv2.Canny(blurred, 400, 1800, apertureSize=5, L2gradient=True)
    # MIN threshold throws out edges below, MAX threshold marks edges
    # as certain over it and keeps edges connected to those between the 
    # thresholds. 
    # Seems to work better with sobel kernel size '5' instead of '3'.
    # Canny already seems to output closed contours, so better not mess with it
    # by applaying closing kernel

    # find contours (i.e. the 'outlines') in the image:
    (_, cnts, _) = cv2.findContours(edged.copy(), 
                                    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    #sort by area and keep only largest for better performance
    cnts = sorted(cnts, key = cv2.contourArea, reverse=True)[:10]    

    # loop over the contours
    area_prev = 0.0
    for c in cnts:
        # approximate the contour
        peri = cv2.arcLength(c, closed=True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, closed=True) #0.02
        # if the approximated contour has four points assume it is the goban
        if (len(approx) == 4 and cv2.contourArea(approx) > area_prev):
            area_prev = cv2.contourArea(approx)
            corners = approx
            #break

    corners = np.reshape(corners,(4,2))
    return corners

def mark_corners(img, corners):
    """Marks corner pixels green.
    """
    for (col,row) in corners:
        img[row,col] = [0,255,0] #green in BGR
    return img

def main():
    pass

if __name__ == '__main__':
    main()