## Synopsis

This project mainly aims to convert a picture of a goban to a matching sgf file. 

It will offer two modes for corner detection, contour based and neural net based. In order to train the neural net there will also be a blender scene to render training data which could be used as the basis for tackling other problems with a scarcity of training data or for visualisation purposes.

Currently working modules:
* parser.py
* find_corners_with_contours.py
* warp.py
* read_position.py
* main.py (will be extended)

So at the moment you transform like this:
[![basic.jpg](https://s19.postimg.org/6sf2s2ns3/basic.jpg)](https://postimg.org/image/5ddi3cmov/)
[![intersections_marked.jpg](https://s19.postimg.org/5sf68vhn7/intersections_marked.jpg)](https://postimg.org/image/okr1cge1b/)
[![Screen_Shot_2018-01-23_at_22.58.51.png](https://s19.postimg.org/fkhueo5gj/Screen_Shot_2018-01-23_at_22.58.51.png)](https://postimg.org/image/4858wvwrj/)

## Code Example

```bash
python main.py data/raw_test/basic.jpg data/sgf/basic.sgf
```
converts image to sgf file

## Motivation

After doing a course on deep neural nets introducing me to Python and Tensorflow I wanted to get my hands dirty with a project of my own. 

Go is my guilty pleasure and I often find myself taking pictures of interesting problems, but am too lazy to set up the position again later for analysis. 

I figured since the preexisting solutions struggle with corner detection why not try to automate that as well as possible. This should present an opportunity to learn some OpenCV, Blender and another machine learning framework like Pytorch or Keras on the way. 

## Installation

You need to have Blender (tested with 2.7.9) installed and use Anaconda to create the environment from the yaml file.

```bash
git clone https://github.com/irglbriz/goban_to_sgf
cd goban_to_sgf
conda env create -f environment.yml
source activate goban_to_sgf
```

## Tests

The working modules should have tests in the 'unittests.py' module.
Please be aware that currently running them requires user interaction.

## Contributors

Since I need a solo project for my portfolio, I will finish this to basic functionality on my own. After that I am open to collaboration, especially with an artist for more beautiful renders or with a go playing website to implement this as a web service. 

## License

This project is published under the MIT License - check the 'LICENSE' file.