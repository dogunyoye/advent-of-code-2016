import os.path
import re

DATA = os.path.join(os.path.dirname(__file__), 'day22.txt')


class Node(object):

    def __init__(self, i, j, size, used, avail, used_percent):
        self.i = i
        self.j = j
        self.size = size
        self.used = used
        self.avail = avail
        self.used_percent = used_percent

    def __eq__(self, other):
        return self.i == other.i and self.j == other.j

    def __hash__(self):
        return hash((self.i, self.j))

    def __repr__(self):
        return ("Node(%d, %d, %dT, %dT, %dT, %d%%)" %
                (self.i, self.j, self.size, self.used, self.avail, self.used_percent))


def __create_nodes(data) -> list[Node]:
    lines = data.splitlines()
    nodes = []
    for i in range(2, len(lines)):
        parts = re.findall(r'/dev/grid/node-x(\d+)-y(\d+) *(\d+)T *(\d+)T *(\d+)T *(\d+)%', lines[i])[0]
        parts = list(map(int, parts))
        nodes.append(Node(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5]))
    return nodes


def calculate_number_of_viable_node_pairs(data) -> int:
    nodes = __create_nodes(data)
    return 0


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(calculate_number_of_viable_node_pairs(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
