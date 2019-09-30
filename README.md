## Synopsis

This project aims to convert a picture of a go game position to a matching sgf file. 

It uses machine learning models from [this](https://github.com/irglbriz/goban_data_set) project. 

## Code Example

Convert single photo:
```bash
python src/main.py ~/tuff_position.jpg
```
Convert batch of photos:
```bash
python src/main.py ~/tournament_shots/
```
Make sure that all goban corners are in center portion of the photo!

## Motivation

Go is one of my guilty pleasures and I often find myself taking pictures of interesting situations. With a tool like this it is much easier to restore a position for computer analysis. 

## Installation

Use Anaconda to create the environment from the yaml file.

```bash
git clone https://github.com/irglbriz/goban_to_sgf
cd goban_to_sgf
conda env create -f environment.yml
source activate goban_to_sgf
```

## Tests

Insufficient test coverage, but low priority at the moment. 

## Contributors

I'm working solo on this project.

## License

This project is published under the MIT License - check the 'LICENSE' file.