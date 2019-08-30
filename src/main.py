"""Pulls the whole process together

Entry point for invocation from shell
"""
import numpy as np
import cv2
import os
import re
import argparse

import preprocess
import init_models
import find_corners as fc
import warp
import read_position as rp
import sgf_parser

MIN_RES = 1000
UNET_RES = fc.UNET_RES

def main():
    parser = argparse.ArgumentParser(description="convert photo of goban to sgf file")
    parser.add_argument("input_path", help="path to photo or folder with photos")
    args = parser.parse_args()

    assert os.path.exists(args.input_path)
    queue = []
    if os.path.isfile(args.input_path):
        queue.append(args.input_path)
    else:
        for file in os.listdir(args.input_path):
            if re.match(r'^.*\.(jpg|png)$', file.lower()):
                queue.append(args.input_path+file)
    print(f'processing queue: {queue}')
        
    # we keep two models loaded at the same time so we don't have to reload for batch processing
    graph0, session0, model0 = init_models.init_seg_model()
    graph1, session1, model1 = init_models.init_class_model()

    for filename in queue:
        print(f"Processing {filename} ...")
        # All processing is done in gray
        gray = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
        assert gray.shape[0] >= MIN_RES and gray.shape[1] >= MIN_RES, "Input resolution too low!"

        img = preprocess.equalize_and_crop(gray)
        print(f'cropped to: {img.shape}')
        assert img.shape[0] == img.shape[1], "Not quadratic after cropping!"
        cv2.imwrite('debug/cropped.jpg', img)
        
        corners = fc.find_corners(img, graph0, session0, model0)
        assert corners.shape == (4,2), "Wrong corners shape!"
        # rescale coordinates
        corners = corners * img.shape[0] / UNET_RES
        assert np.min(corners) >= 0 and np.max(corners) <= img.shape[0], "Corner coordinates out of bound!"
        print(f'found the following corners: \n{corners}')

        warped = warp.top_down_view(img, corners)
        cv2.imwrite('debug/warped.jpg', warped)

        position = rp.read_position(warped, graph1, session1, model1)

        sgf_parser.mat_to_sgf(position, filename.rsplit('.', 1)[0]+'.sgf')

if __name__ == '__main__':
    main()