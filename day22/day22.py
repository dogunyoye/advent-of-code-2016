import os.path
import re
from collections import deque

DATA = os.path.join(os.path.dirname(__file__), 'day22.txt')


class Node(object):

    def __init__(self, x, y, size, used, avail, used_percent):
        self.x, self.y = x, y
        self.size = size
        self.used = used
        self.avail = avail
        self.used_percent = used_percent

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return "Node(%d, %d, %dT, %dT, %dT)" % (self.x, self.y, self.size, self.used, self.avail)


def __create_nodes(data) -> list[Node]:
    lines = data.splitlines()
    nodes = []
    for i in range(2, len(lines)):
        parts = re.findall(r'/dev/grid/node-x(\d+)-y(\d+) *(\d+)T *(\d+)T *(\d+)T *(\d+)%', lines[i])[0]
        parts = list(map(int, parts))
        nodes.append(Node(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5]))
    return nodes


def __find_highest_x_at_y0(nodes) -> int:
    y0_nodes = list(filter(lambda n: n.y == 0, nodes))
    return max(list(map(lambda n: n.x, y0_nodes)))


def calculate_number_of_viable_node_pairs(data) -> int:
    nodes = __create_nodes(data)
    pairs = []
    for i in range(0, len(nodes) - 1):
        a = nodes[i]
        for j in range(i + 1, len(nodes)):
            b = nodes[j]
            if 0 < a.used <= b.avail:
                pairs.append((a, b))
            if 0 < b.used <= a.avail:
                pairs.append((b, a))
    return len(pairs)


# Puzzle visualised as a game here - https://codepen.io/anon/pen/BQEZzK/
# Requires JS library, Lodash
# on codepen.io, Settings -> Add External Scripts/Pens -> Add Lodash
def calculate_fewest_steps_to_move_goal_node(data) -> int:
    nodes = __create_nodes(data)

    goal = (0, __find_highest_x_at_y0(nodes))
    initial_empty_node = list(filter(lambda nn: nn.used == 0, nodes))[0]

    grid = {}
    for n in nodes:
        grid[(n.y, n.x)] = n

    queue, visited = deque(), set()
    queue.append(((initial_empty_node.y, initial_empty_node.x), 0))
    visited.add((initial_empty_node.y, initial_empty_node.x))

    while len(queue) != 0:
        current = queue.popleft()
        current_position, current_steps = current[0], current[1]

        y = current_position[0]
        x = current_position[1]

        # DISCLAIMER: This solution is specific to my input
        # - calculate the number of steps to place the empty
        # disk next the goal disk => current_steps
        # - every step to move the goal disk towards the destination
        # (0,0) requires 5 steps of the empty disk. We need to do this
        # max_x - 1 times => (5 * (max_x - 1))
        # - This will land us 1 step away from the destination => + 1
        if x == goal[1] - 1 and y == goal[0]:
            return current_steps + (5 * (goal[1] - 1)) + 1

        neighbors = [(y, x - 1), (y - 1, x), (y, x + 1), (y + 1, x)]
        for next_neighbour in neighbors:
            if next_neighbour in grid.keys():
                next_node = grid[next_neighbour]
                if next_node.used <= initial_empty_node.size:
                    if next_neighbour not in visited:
                        queue.append((next_neighbour, current_steps + 1))
                        visited.add(next_neighbour)

    raise Exception("No solution found")


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(calculate_number_of_viable_node_pairs(data)))
        print("Part 2: " + str(calculate_fewest_steps_to_move_goal_node(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
