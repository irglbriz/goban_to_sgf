## Synopsis

This project aims to convert a picture of a goban to a matching sgf file. 

Currently it uses contour search for corner detection. This doesn't work well under hard conditions, eg. with flat angles, objects occluding the edge of the board, etc.. In order to alleviate this I'm considering starting another project to train a neural net and/or offer a mode with manual corner selection. 

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

Since I'm trying to transition to a programming position I wanted to get my hands dirty with a project of my own. 

Go is my guilty pleasure and I often find myself taking pictures of interesting problems, but am too lazy to set up the position again later for analysis. 

## Installation

Use Anaconda to create the environment from the yaml file.

```bash
git clone https://github.com/irglbriz/goban_to_sgf
cd goban_to_sgf
conda env create -f environment.yml
source activate goban_to_sgf
```

## Tests

Please be aware that currently running unittests.py requires user interaction.

## Contributors

I'm working solo on this project, but I am grateful for the work put in all the libraries I am using. Some inspiration and code snippets were taken from https://www.pyimagesearch.com.

## License

This project is published under the MIT License - check the 'LICENSE' file.