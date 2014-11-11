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


def read_png(png_file_path):
    img = Image.open(png_file_path)
    raw_data = img.tostring()

    data = [[0 for y in range(img.size[1])] for x in range(img.size[0])]
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            try:
                data[x][y] = raw_data[x * img.size[0] + y]
            except IndexError:
                print("Error while writing index=", (x * img.size[0] + y), "to [x=", x, ", y=", y, "]")

    return data, img.size


def get_deltas(h, a):
    return m.cos(a) * h, m.sin(a) * h


def clamp(x, y, s):
    return max(0, min(x, s[0]-1)), max(0, min(y, s[1]-1))


def trace_ray(o, a, d, s):
    cx, cy = int(o[0] / PX_PER_CM), int(o[1] / PX_PER_CM)
    dx, dy = 0, 0
    for h in range(0, LASER_RANGE_CM, SAMPLING_STEP_CM):
        dx, dy = get_deltas(h, a)
        dx, dy = int(dx / PX_PER_CM), int(dy / PX_PER_CM)
        cx, cy = clamp(cx + dx, cy + dy, s)
        if a == 0:
            print("cx=", cx, ", cy=", cy)
        if d[cx][cy] > 0:
            return h
    return LASER_RANGE_CM
    pass


def get_laserscan(o, d, s):
    ranges = list()
    for a in range(0, 360, ANGULAR_RESOLUTION):
        ranges.append(trace_ray(o, a, d, s))
    return ranges
    pass


def main():
    data, size = read_png(IMAGE_PATH)
    ranges = get_laserscan((1, 1), data, size)
    print(ranges)
    pass


if __name__ == "__main__":
    main()