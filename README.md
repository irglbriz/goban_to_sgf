## Synopsis

This project aims to convert a picture of a goban to a matching sgf file. 

At the moment you transform like this:
![basic.jpg](https://github.com/irglbriz/goban_to_sgf/blob/master/data/raw_test/partly/basic.jpg?raw=true)
![ScreenShot.png](https://github.com/irglbriz/goban_to_sgf/blob/master/data/ScreenShot.png?raw=true)
(sgf editor not part of project, just used for visualization)

The current approach struggles with two main issues:

Contour search for corner detection doesn't work well under hard conditions, eg. with flat angles, objects occluding the edge of the board, etc.. In order to alleviate this I'm considering implementing a mode with graphic UI for manual corner selection/correction and possibly starting another project to train a classifier trained on automatically rendered (and thus easily labelled) data. 

The simplistic black/white/free classifier for individual stones based on simple average brightness also struggles with difficult lighting situations, eg. reflections on stones, shadows etc.. In oder to alleviate this issue I'm considering to train a simple classifier either on manually labelled data or on automatically rendered (and thus easily labelled) data. 

## Code Example

```bash
python main.py data/raw_test/basic.jpg data/sgf/basic.sgf
```
converts image to sgf file

## Motivation

I wanted to get my hands dirty with a project of my own to find out more about the issues a computer vision pipeline runs into in a 'real world' setting.

Go is my guilty pleasure and I often find myself taking pictures of interesting situations. With a tool like this it would be much easier to set up the position again later for further analysis. 

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