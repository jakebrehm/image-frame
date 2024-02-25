<div align="center">

<img src="https://raw.githubusercontent.com/jakebrehm/image-frame/master/img/banner.png" alt="Image Frame Banner" style="width: 100%; height: auto;"/>

<br>

<h1>Add colorful frames to your images and gifs.</h1>

<br>

<a href="https://github.com/jakebrehm/image-frame"><img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/jakebrehm/image-frame?color=darkgreen&logo=Git&logoColor=white&style=for-the-badge"></a>
<a href="https://raw.githubusercontent.com/jakebrehm/image-frame/master/license.txt"><img alt="GitHub license" src="https://img.shields.io/github/license/jakebrehm/image-frame?color=darkgreen&style=for-the-badge"></a>

<br>
</div>

<p align="center">
    <strong>Image Frame</strong> is a simple command line script that allows you to add borders to your image file.
</p>

<hr>

## Table of contents

* [What it does](#what-it-does)
* [Getting set up](#getting-set-up)
* [How to use it](#how-to-use-it)
* [Example usage](#example-usage)
* [Contributors](#contributors)

<hr>

## What it does

**Image Frame** takes any image file (including gifs) and adds a customizable colored frame/border around it. This is a technique that I personally use in a few of my readme files (see my [ManyMiles](https://github.com/jakebrehm/manymiles) repository) to add a bit of personality and color.

This is something that can be achieved through image editing software like Photoshop or other online services, but nearly all of them require payment to remove a watermark, work with certain file types like gifs, or remove file size limitations. This project aims to make the process as simple and painless as possible, and most importantly, *free*.

## Getting set up

The source code can be viewed on Github [here](https://github.com/jakebrehm/image-frame).

It is also assumed that Python is already installed on your machine.

### Cloning the repository

The first step to using **Image Frame** is to clone this repository. To do this, open a command line instance and change your working directory to the directory you'd like to clone the repository to.

```bash
cd "path/to/clone/repository/to"
```

Then, use the following command to clone the repository.

```
git clone https://github.com/jakebrehm/image-frame.git
```

Once that's done, change your working directory to the directory you just cloned.

```bash
cd "image-frame"
```

### Creating the virtual environment

Now, you can optionally create a virtual environment to run the project in. This will keep all of the dependencies for this project neatly tucked away from your system installation of Python, allowing for easy organization and uninstallation.

```
python3 -m venv env
```

If you chose to create the virtual environment, you need to activate it using `source env/bin/activate` (Unix) or `.\env\Scripts\activate` (Windows). You can deactivate the environment using `deactivate` whenever you'd like, but you'll need to reactive it if you use the project again.

### Installing dependencies

Now you can install all of the dependencies required to properly get the project up and running.

```
pip3 install -r requirements.txt
```

## How to use it

Start with your command line open and the cloned repository as your working directory. Then, simply run the `add_border.py` script as you would any other Python script, except with the extra `-i` argument: the filepath to the source image.

```bash
python3 add_border.py -i "path/to/image.png"
```

Some other optional arguments are also available, and can be listed using the help argument.

```bash
python3 add_border.py -h
```

If you'd rather use the code directly, you're also able to simply import the `add_border` function from the module.

```python
from add_border import add_border
help(add_border)
```

## Example usage

To add a border to `test.png` with an orange border and 5 pixels of padding with the progress bar disabled, and save the output as `test-bordered.png`:

```bash
python3 add_border.py -i "test.png" -o "test-bordered.png" -c "orange" -p 5 --disable-progress
```

To add a border to `test.gif` with a custom hex color `#035851`, 20 pixels of padding, and 80 milliseconds between each frame, and save with the auto-generated name `test-out.gif`:

```bash
python3 add_border.py -i "test.gif" -c "#035851" -p 20 -d 80
```

<hr>

## Contributors

- **Jake Brehm** - *main developer* - [Email](mailto:mail@jakebrehm.com) | [Github](http://github.com/jakebrehm) | [LinkedIn](http://linkedin.com/in/jacobbrehm)