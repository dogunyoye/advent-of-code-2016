import os.path
from collections import deque
from itertools import permutations

DATA = os.path.join(os.path.dirname(__file__), 'day24.txt')


def __create_map(data) -> tuple:
    layout = {}
    locations = set()
    start = (-1, -1)
    for i, line in enumerate(data.splitlines()):
        for j in range(0, len(line)):
            if line[j] != "#":
                layout[(i, j)] = line[j]
                if line[j] == "0":
                    start = (i, j)
                if line[j].isnumeric() and line[j] != "0":
                    locations.add((i, j))
    return layout, locations, start


def __fewest_steps(data, part_two) -> int:
    layout, locations, start = __create_map(data)
    all_steps = []

    for p in permutations(locations):
        route = list(p)
        route.insert(0, start)
        if part_two:
            route.append(start)
        steps = 0

        for i in range(0, len(route) - 1):
            start_node, end_node = route[i], route[i + 1]
            queue, visited = deque(), set()

            queue.append((start_node, 0))
            visited.add(start_node)

            while len(queue) != 0:

                current = queue.popleft()
                current_position, current_steps = current[0], current[1]
                if current_position == end_node:
                    steps += current_steps
                    break

                i, j = current_position
                neighbors = [(i, j - 1), (i - 1, j), (i, j + 1), (i + 1, j)]

                for n in neighbors:
                    if n in layout and n not in visited:
                        queue.append((n, current_steps + 1))
                        visited.add(n)

        all_steps.append(steps)

    return min(all_steps)


def calculate_fewest_steps_to_reach_all_locations(data) -> int:
    return __fewest_steps(data, False)


def calculate_fewest_steps_for_roundtrip(data) -> int:
    return __fewest_steps(data, True)


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(calculate_fewest_steps_to_reach_all_locations(data)))
        print("Part 2: " + str(calculate_fewest_steps_for_roundtrip(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
