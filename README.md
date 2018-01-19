## Synopsis

This project mainly aims to convert a picture of a goban to a matching sgf file. 

It will offer two modes for corner detection, contour based and neural net based. In order to train the neural net there will also be a blender scene to render training data which could be used as the basis for tackling other problems with a scarcity of training data or for visualisation purposes.

Currently working modules:
* parser.py
* find_corners_with_contours.py
* warp.py

## Code Example

TODO: Make this a reality:

```bash
python main.py -convert image.jpg tsumego.sgf
```
converts image to sgf file

```bash
python main.py -render pos.sgf render.jpg
```
renders position from sgf file using blender

## Motivation

After doing a course on deep neural nets introducing me to Python and Tensorflow I wanted to get my hands dirty with a project of my own. 

Go is my guilty pleasure and I often find myself taking pictures of interesting problems, but am too lazy to set up the position again later for analysis. 

I figured since all the preexisting solutions to read a go position needed manual entry of corners why not try to automate that as well. It also presented an opportunity to learn some OpenCV, Blender and another machine learning framework like Pytorch or Keras on the way. 

## Installation

You need to have Blender (tested with 2.7.9) installed and use Anaconda to create the environment from the yaml file.

```bash
git clone https://github.com/irglbriz/goban_to_sgf
cd goban_to_sgf
conda env create -f environment.yml
source activate goban_to_sgf
```

## API Reference

TODO: Settle on and document API

## Tests

The working modules should have tests in the 'unittests.py' module.
Please be aware that currently running them requires user interaction.

## Contributors

Currently just me - Tristan Kraus. 

## License

This project is published under the MIT License - see LICENSE.md