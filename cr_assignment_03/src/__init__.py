__author__ = 'Fernando Morillo, Joschka Rick'


import math as m
import matplotlib.pyplot as plt


color = ['r', 'b', 'g', 'k']


def move(state, movement):
    x_prime = state[0] + movement[2] * m.cos(m.radians(state[2] + movement[0]))
    y_prime = state[1] + movement[2] * m.sin(m.radians(state[2] + movement[0]))
    t_prime = state[2] + movement[0] + movement[1]
    return x_prime, y_prime, t_prime


def apply_error(state, movement, error=(0, 0, 0)):
    error_matrix = [
        (-1, -1, -1),
        (-1, -1,  1),
        (-1,  1, -1),
        (-1,  1,  1),
        (1, -1, -1),
        (1, -1,  1),
        (1,  1, -1),
        (1,  1,  1)
    ]

    possible_states = list()
    for x in range(8):
        possible_states.append(move(state, (
            movement[0] + error_matrix[x][0] * error[0],
            movement[1] + error_matrix[x][1] * error[1],
            movement[2] + error_matrix[x][2] * error[2])))
    return possible_states


def successive_movements(state, movement, error=(0, 0, 0), iterations=3):
    all_points = list()
    all_colors = list()
    all_points.append(state)
    all_colors.append(color[iterations])

    if iterations == 0:
        return all_points, all_colors

    new_states = apply_error(state, movement, error)
    for new_state in new_states:
        new_points, new_colors = successive_movements(new_state, movement, error, iterations - 1)
        all_points += new_points
        all_colors += new_colors

    return all_points, all_colors


initial_state = (0, 0, 0)
movement1 = (-20, -30, 3)
movement2 = (20, 10, 10)
error1 = (10, 5, 0.5)

# Exercise 3.1
# print(move(initial_state, movement1))
# print(move(initial_state, movement2))

# Exercise 3.2
# ax = plt.axes()
# ax.scatter(0, 0)
# e32_results = apply_error(initial_state, movement2, error=error1)
# for i in range(len(e32_results)):
#     ax.scatter(e32_results[i][0], e32_results[i][1])
#     arrow_res = move(e32_results[i], (0.0, 0.0, 0.5))
#     ax.arrow(e32_results[i][0], e32_results[i][1],
#              arrow_res[0] - e32_results[i][0], arrow_res[1] - e32_results[i][1],
#              head_width=0.15, head_length=0.2)
# ax.set_xlim(left=0, right=13)
# ax.set_ylim(bottom=0, top=13)
# plt.show()

# Exercise 3.3
# results, colors = successive_movements(initial_state, movement2, error=error1, iterations=3)
# ax = plt.axes()
# ax.scatter(0, 0)
# for i in range(len(results)):
#     ax.scatter(results[i][0], results[i][1], c=colors[i])
#     # arrow_res = move(results[i], (0.0, 0.0, 0.5))
#     # ax.arrow(results[i][0], results[i][1],
#     #          arrow_res[0] - results[i][0], arrow_res[1] - results[i][1],
#     #          head_width=0.15, head_length=0.2)
# ax.set_xlim(left=0, right=30)
# ax.set_ylim(bottom=0, top=30)
# plt.show()

# Exercise 3.4
# results, colors = successive_movements(initial_state, movement2, error=error1, iterations=3)
# ax = plt.axes()
# ax.scatter(0, 0)
# for i in range(len(results)):
#     ax.scatter(results[i][0], results[i][1], c=colors[i])
#     arrow_res = move(results[i], (0.0, 0.0, 0.5))
#     ax.arrow(results[i][0], results[i][1],
#              arrow_res[0] - results[i][0], arrow_res[1] - results[i][1],
#              head_width=0.15, head_length=0.2)
# ax.set_xlim(left=0, right=30)
# ax.set_ylim(bottom=0, top=30)
# plt.show()