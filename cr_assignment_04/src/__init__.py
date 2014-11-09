__author__ = 'Fernando Morillo, Joschka Rick'

from PIL import Image


IMAGE_PATH = '../Assignment_4_Grid_Map.png'
LASER_RANGE = 1500
PIXEL_RESOLUTION = 4
OPENING_ANGLE = 270
ANGULAR_RESOLUTION = 2


def read_png(png_file_path):
    img = Image.open(png_file_path)
    raw_data = img.tostring()

    data = [[0 for y in range(img.size[1])] for x in range(img.size[0])]
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            try:
                data[x][y] = raw_data[x * img.size[0] + y]
            except IndexError as e:
                print("Error while writing index=", (x * img.size[0] + y), "to [x=", x, ", y=", y, "]")

    return data, img.size


def trace_ray(origin, destination, data):
    pass


def get_laserscan(pose):
    pass


def main():
    data, size = read_png(IMAGE_PATH)
    pass


if __name__ == "__main__":
    main()