## Synopsis

This project aims to convert a picture of a goban to a matching sgf file. 
It'll use machine learning models from [this](https://github.com/irglbriz/goban_data_set) project. 

## Code Example

```bash
python main.py ./photo.jpg
```
or
```bash
python main.py ./photos/
```

## Motivation

Go is one of my guilty pleasures and I often find myself taking pictures of interesting situations. With a tool like this it would be much easier to restore the position for later analysis. 

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