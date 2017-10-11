import argparse
from PIL import Image


def get_new_size(scale, width, height, current_width, current_height):
    if scale:
        result_width = round(current_width * scale / 100)
        result_height = round(current_height * scale / 100)
    else:
        result_width = width if width else current_width
        result_height = height if height else current_height
    return result_width, result_height


def resize_image(source_img, result_img, scale, width, height):
    img = Image.open(source_img)
    new_img = img.resize(get_new_size(scale, width, height, *img.size))
    new_img.save(result_img)


def get_args():
    parser = argparse.ArgumentParser(description='Image resize tool.')
    parser.add_argument('-i', '--input', help='source image',
                        required=True)
    parser.add_argument('-x', '--width', help='width of result file',
                        required=False, type=int)
    parser.add_argument('-y', '--height', help='height of result file',
                        required=False, type=int)
    parser.add_argument('-s', '--scale',
                        help='scale of result file in percents of source size',
                        required=False, type=int)
    parser.add_argument('-o', '--output', help='result file name',
                        required=True)
    return parser.parse_args()


if __name__ == '__main__':
    args = get_args()
    resize_image(args.input, args.output, args.scale, args.width, args.height)
