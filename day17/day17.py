import hashlib
import os.path
from collections import deque

DATA = os.path.join(os.path.dirname(__file__), 'day17.txt')


def find_shortest_path_to_the_vault(data) -> str:
    queue, visited = deque(), set()
    start, end = (0, 0), (3, 3)
    start_hash = data.splitlines()[0]
    queue.append(("", start, start_hash))

    open_door = {"b", "c", "d", "e", "f"}
    neighbours = [(-1, 0, "U"), (1, 0, "D"), (0, -1, "L"), (0, 1, "R")]

    visited.add((start, ""))

    while len(queue) != 0:
        current = queue.popleft()
        path, position, md5_hash = current[0], current[1], current[2]

        if position == end:
            return path

        new_hash = hashlib.md5(md5_hash.encode()).hexdigest()
        directions = new_hash[:4]

        for i, d in enumerate(directions):
            if d in open_door:
                next_position = (position[0] + neighbours[i][0], position[1] + neighbours[i][1])
                if 0 <= next_position[0] <= 3 and 0 <= next_position[1] <= 3:
                    next_path = path + neighbours[i][2]
                    next_hash = md5_hash + neighbours[i][2]
                    next_node = (next_path, next_position, next_hash)
                    if (next_position, next_hash) not in visited:
                        queue.append(next_node)
                        visited.add((next_position, next_hash))


def find_longest_path_to_the_vault(data) -> int:
    queue, visited = deque(), set()
    start, end = (0, 0), (3, 3)
    start_hash = data.splitlines()[0]
    queue.append(("", start, start_hash, 0))
    steps_to_vault = []

    open_door = {"b", "c", "d", "e", "f"}
    neighbours = [(-1, 0, "U"), (1, 0, "D"), (0, -1, "L"), (0, 1, "R")]

    visited.add((start, ""))

    while len(queue) != 0:
        current = queue.popleft()
        path, position, md5_hash, steps = current[0], current[1], current[2], current[3]

        if position == end:
            steps_to_vault.append(steps)
            continue

        new_hash = hashlib.md5(md5_hash.encode()).hexdigest()
        directions = new_hash[:4]

        for i, d in enumerate(directions):
            if d in open_door:
                next_position = (position[0] + neighbours[i][0], position[1] + neighbours[i][1])
                if 0 <= next_position[0] <= 3 and 0 <= next_position[1] <= 3:
                    next_path = path + neighbours[i][2]
                    next_hash = md5_hash + neighbours[i][2]
                    next_node = (next_path, next_position, next_hash, steps + 1)
                    if (next_position, next_hash) not in visited:
                        queue.append(next_node)
                        visited.add((next_position, next_hash))

    return max(steps_to_vault)


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + find_shortest_path_to_the_vault(data))
        print("Part 2: " + str(find_longest_path_to_the_vault(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
