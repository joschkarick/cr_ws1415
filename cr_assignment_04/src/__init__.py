__author__ = 'Fernando Morillo, Joschka Rick'

from PIL import Image
import math as m


IMAGE_PATH = '../Assignment_4_Grid_Map.png'
CM_PER_PIXEL = 4
PX_PER_CM = 1 / CM_PER_PIXEL
LASER_RANGE_CM = 1500
LASER_RANGE_PX = LASER_RANGE_CM * PX_PER_CM
OPENING_ANGLE = 270
ANGULAR_RESOLUTION = 2
SAMPLING_STEP_CM = 1


class Point():
    x = 0
    y = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


def read_png(png_file_path):
    img = Image.open(png_file_path)
    img = img.convert(mode='L')
    img.show()
    # raw_data contain every pixel row by row
    raw_data = list(img.getdata())

    ocp_grid = [[0 for y in range(img.size[1])] for x in range(img.size[0])]
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            try:
                ocp_grid[x][y] = 0 if raw_data[y * img.size[0] + x] else 1
            except IndexError:
                print("Error while writing index=", (x * img.size[1] + y), "to [x=", x, ", y=", y, "]")

    return ocp_grid, img.size


def get_deltas(hypotenuse, alpha):
    return m.cos(m.radians(alpha)) * hypotenuse, m.sin(m.radians(alpha)) * hypotenuse


def clamp(x, y, s):
    return max(0, min(x, s[0]-1)), max(0, min(y, s[1]-1))


def point_from_cell(x, y):
    return x * CM_PER_PIXEL, y * CM_PER_PIXEL


def cell_from_point(x, y):
    return int(x / CM_PER_PIXEL), int(y / CM_PER_PIXEL)


def trace_ray(origin, alpha, ocp_grid, map_size):
    cx, cy = cell_from_point(origin.x, origin.y)
    for hypotenuse in range(0, LASER_RANGE_CM, SAMPLING_STEP_CM):
        dx, dy = get_deltas(hypotenuse, alpha)
        dx, dy = cell_from_point(dx, dy)
        cx, cy = clamp(cx + dx, cy + dy, map_size)
        if alpha == 0:
            print("cx=", cx, ", cy=", cy, "d=", ocp_grid[cx][cy], "hypotenuse=", hypotenuse)
        if ocp_grid[cx][cy] > 0:
            return hypotenuse
    return LASER_RANGE_CM
    pass


def get_laserscan(origin, ocp_grid, s):
    ranges = list()
    for alpha in range(0, 360, ANGULAR_RESOLUTION):
        ranges.append(trace_ray(origin, alpha, ocp_grid, s))
    return ranges
    pass


def main():
    ocp_grid, size = read_png(IMAGE_PATH)
    ranges = get_laserscan(Point(120, 200), ocp_grid, size)
    print(ranges)
    pass


if __name__ == "__main__":
    main()