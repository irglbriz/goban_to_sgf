## Synopsis

This project aims to convert a picture of a goban to a matching sgf file. 

## Code Example

```bash
python main.py photo.jpg position.sgf
```
converts image to sgf file

## Motivation

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

TODO: Need to be adapted to new project org and should work without user interaction

## Contributors

I'm working solo on this project.

## License

This project is published under the MIT License - check the 'LICENSE' file.