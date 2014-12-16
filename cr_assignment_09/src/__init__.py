__author__ = 'Fernando Morillo, Joschka Rick'


import math as m


class Node(object):

    def __init__(self, x, y, costs, parent, heuristic_costs):
        self.x = x
        self.y = y
        self.costs = costs
        self.parent = parent
        self.heuristic_costs = heuristic_costs

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True

        return False

    def __repr__(self):
        return str((self.x, self.y, self.costs))

    def print_path(self):
        if not self.parent:
            return str((self.x, self.y))

        return self.parent.print_path() + " -> " + str((self.x, self.y))

    def get_distance(self, x, y):
        return m.sqrt((x - self.x)**2 + (y - self.y)**2)

    def get_total_costs(self):
        return self.costs + self.heuristic_costs


def a_star(start, goal, grid):
    open_nodes = list()
    closed_nodes = list()
    open_nodes.append(start)

    while open_nodes:
        cheapest_node = min(open_nodes, key=lambda node: node.get_total_costs())
        open_nodes.remove(cheapest_node)

        if cheapest_node == goal:
            print(len(closed_nodes))
            for node in closed_nodes:
                print(node)
            return cheapest_node

        closed_nodes.append(cheapest_node)

        expand_node(cheapest_node, grid, open_nodes, closed_nodes, goal)

    return None


def expand_node(node, grid, open_nodes, closed_list, goal):
    # Create successors
    successors = list()

    successor = get_successor(node, grid, 1, 0, goal)
    if successor:
        successors.append(successor)

    successor = get_successor(node, grid, 0, 1, goal)
    if successor:
        successors.append(successor)

    successor = get_successor(node, grid, -1, 0, goal)
    if successor:
        successors.append(successor)

    successor = get_successor(node, grid, 0, -1, goal)
    if successor:
        successors.append(successor)

    # Task 9.2
    # Diagonal
    successor = get_successor(node, grid, 1, 1, goal)
    if successor:
        successors.append(successor)

    successor = get_successor(node, grid, -1, 1, goal)
    if successor:
        successors.append(successor)

    successor = get_successor(node, grid, 1, -1, goal)
    if successor:
        successors.append(successor)

    successor = get_successor(node, grid, -1, -1, goal)
    if successor:
        successors.append(successor)

    for successor in successors:
        if successor in closed_list:
            continue

        if successor in open_nodes:
            existing_node_index = open_nodes.index(successor)
            if open_nodes[existing_node_index].costs > successor.costs:
                del open_nodes[existing_node_index]
                open_nodes.append(successor)
        else:
            open_nodes.append(successor)


def get_successor(node, grid, x_movement, y_movement, goal):
    new_x = node.x + x_movement
    new_y = node.y + y_movement

    if new_x >= len(grid) or new_y >= len(grid[0]):
        return None

    if new_x < 0 or new_y < 0:
        return None

    if grid[new_x][new_y] == 1:
        return None

    return Node(new_x, new_y, node.costs + 1, node, goal.get_distance(new_x, new_y))


grid1 = [
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 1, 1, 0],
    [0, 1, 1, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0, 0, 0, 1, 1, 0],
    [0, 1, 0, 0, 1, 1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 1, 0],
    [0, 1, 2, 1, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 3, 0, 0, 0, 0, 0]
]

start1 = None
goal1 = None
for x, row in enumerate(grid1):
    for y, column in enumerate(row):
        if grid1[x][y] == 2:
            goal1 = Node(x, y, 0, None, 0)
        if grid1[x][y] == 3:
            start1 = Node(x, y, 0, None, goal1.get_distance(x, y))

found_goal = a_star(start1, goal1, grid1)

print(found_goal.print_path())
print(found_goal.costs)