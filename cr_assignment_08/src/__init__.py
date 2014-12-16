__author__ = 'Fernando Morillo, Joschka Rick'


import math as m
import matplotlib.pyplot as plt
import numpy as np


def get_distance(p1, p2):
    return m.sqrt((p1[0] - p2[0])**2 + (p1[1] - p1[1])**2)


def match_points(source, target):
    matching = list()

    for point in source:
        closest = target[0]
        for target_point in target:
            if get_distance(point, target_point) < get_distance(point, closest):
                closest = target_point

        matching.append(closest)

    return np.array(matching)


def icp(source, target):
    matches = match_points(source, target)

    target_x = matches
    source_p = source

    centroid_x = np.mean(target, axis=0)
    centroid_p = np.mean(source, axis=0)

    centered_x = target_x - np.tile(centroid_x, (target_x.shape[0], 1))
    centered_p = source_p - np.tile(centroid_p, (source_p.shape[0], 1))

    h = np.dot(centered_x.T, centered_p)

    u, s, v = np.linalg.svd(h)

    rotation = np.dot(v.T, u.T)
    print(rotation)

    translation = np.dot(-rotation, centroid_x.T) + centroid_p.T
    print(translation)

    return rotation, translation

# Target
X = np.array([(-1, 2), (0, 3), (1, 4), (2, 5), (3, 4), (4, 3), (5, 2)])

# Source
P_0 = np.array([(-0.5, 3), (0.4, 4.1), (1.3, 5.2), (2.2, 6.3), (3.1, 5.4), (4, 4.5), (4.9, 3.6)])

rot, trans = icp(P_0, X)
P_1 = np.add(np.dot(P_0, rot), trans)

print(P_1)

#r = icp(X, P)
#r = icp(P_1, X)

ax = plt.axes()

ax.scatter(X[:, 0], X[:, 1], c='b', s=50)
ax.scatter(P_0[:, 0], P_0[:, 1], c='w', s=50)
ax.scatter(P_1[:, 0], P_1[:, 1], c='r', s=50)

plt.show()