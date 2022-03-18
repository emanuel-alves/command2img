# command2img

## Motivation

This program was developed out of the need to capture a program's output as an image to insert into a report.

## Install

To install it, you can use the python package manager:

    pip install git+https://github.com/emanuel-alves/command2img.git

## Update

    pip install --upgrade -e git+https://github.com/emanuel-alves/command2img.


## Uninstall 

    pip uninstall command2img

## Usage


## Examples

### using exa (ls):    
    exa --icons --binary --header | command2img
![cat image](/images/cat.png)

### using exa (tree):
    exa --tree --icons | command2img
![cat image](/images/cat.png)

### using echo:
    echo "Example echo" | command2img
![cat image](/images/cat.png)

### using cat:
    cat README.md | command2img
![cat image](/images/cat.png)
