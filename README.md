# Image Resizer

It is a tool for an image resize. 

# How to use

You shoul use python 3.4 or upper

Install requirements
```
pip install -r requrements.txt
```  
 You can set up width, height or scale in percents of source size.
 If you set up scale  width and height will be ignored.
 If you don't set up scale and width or height both, a source file measure will be used.

```
python3 image_resize.py -h
usage: image_resize.py [-h] -i INPUT [-x WIDTH] [-y HEIGHT] [-s SCALE] -o
                       OUTPUT

Image resize tool.

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        source image
  -x WIDTH, --width WIDTH
                        width of result file
  -y HEIGHT, --height HEIGHT
                        height of result file
  -s SCALE, --scale SCALE
                        scale of result file in percents of source size
  -o OUTPUT, --output OUTPUT
                        result file name

```

# Example of using

Create an test.png in current folder with size 100x100
```
python3 image_resize.py -i /home/lucky/ssdtest-slat.png -o ./test.png -x 100 -y 100
```



# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
