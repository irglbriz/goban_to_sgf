
# This script works together with a blender scene to generate labeled training
# data. More specifically, it renders a goban with a random position and
# outputs both the rendered image(s) and correpsonding labels for the 
# coordinates of the sorted corners in that rendered image.

# Invoke this script from command line like this:
# blender data/blender/scene.blend --background --python generate_samples.py


import bpy  # python interface for blender
import numpy as np
import random


NUM_RENDERS = 1


def generate_random_game_pos():
    pos = np.zeros((19, 19))
    for x in pos:
        for y in pos:
            pos[x][y] = random.randint(-1, 1)
    return pos


def put_stones():
    pass


def camera_pos():
    pass


def light_pos():
    pass


def render_scene():
    pass


def main():
    pass


if __name__ == '__main__':
    main()