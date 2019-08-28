"""Outputs corners of goban via segmentation by u-net and contour search."""

import numpy as np
import cv2

UNET_RES = 512

def segment_with_unet(img, graph, session, model):
    img = cv2.resize(img, dsize=(UNET_RES, UNET_RES), 
                          interpolation=cv2.INTER_LINEAR)
    img = (img / 255.) - 0.5
    img = np.expand_dims(img, axis=2) #keras wants color channel dim
    img = (np.expand_dims(img, axis=0)) #keras expects batch shape
    with graph.as_default():
        with session.as_default():
            segmented = model.predict(img)
    segmented = np.squeeze(segmented) #drop batch and color dim
    segmented = (segmented > 0.5) * 1.
    return segmented

def contour_corner_search(segmented):
    gray = (segmented * 255.).astype('uint8') 
    # find contours (i.e. the 'outlines') in the image:
    _, cnts, _ = cv2.findContours(gray.copy(), 
                                  cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # sort by area and keep only largest ten for better performance
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:10]    
    # loop over the contours
    area_prev = 0.0
    for c in cnts:
        # approximate the contour
        peri = cv2.arcLength(c, closed=True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, closed=True)  # 0.02
        # if the approximated contour has four points assume it is the goban
        if (len(approx) == 4 and cv2.contourArea(approx) > area_prev):
            area_prev = cv2.contourArea(approx)
            corners = approx
    corners = np.reshape(corners, (4, 2))
    return corners

def find_corners(img, graph, session, model):
    segmented = segment_with_unet(img, graph, session, model)
    corners = contour_corner_search(segmented)
    return corners