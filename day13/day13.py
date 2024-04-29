import os.path
from collections import deque

DATA = os.path.join(os.path.dirname(__file__), 'day13.txt')


def __identify_terrain(position, favourite_number) -> str:
    # (x, y) -> j = x, i = y
    i, j = position[0], position[1]

    # x*x + 3*x + 2*x*y + y + y*y
    terrain_value = (j * j) + (3 * j) + (2 * j * i) + i + (i * i)
    terrain_value += favourite_number
    binary = format(terrain_value, 'b')
    number_of_ones = binary.count('1')

    if number_of_ones % 2 == 0:
        return '.'
    return '#'


def __is_position_open(p, favourite_number) -> bool:
    return p[0] >= 0 and p[1] >= 0 and __identify_terrain(p, favourite_number) == '.'


def __bfs(favourite_number, start, end, part_two) -> int:
    queue, visited = deque(), set()
    queue.append((0, start))
    number = favourite_number

    while len(queue) != 0:
        current = queue.popleft()
        steps, position = current[0], current[1]

        if not part_two and position == end:
            return steps
        if part_two and steps == 50:
            return len(visited)

        i, j = position[0], position[1]
        neighbors = [(i, j - 1), (i - 1, j), (i, j + 1), (i + 1, j)]
        neighbors = (list(filter(lambda p: __is_position_open(p, number), neighbors)))

        for n in neighbors:
            if n not in visited:
                queue.append((steps + 1, n))
                visited.add(n)


def find_fewest_steps_to_destination(data) -> int:
    return __bfs(int(data.splitlines()[0]), (1, 1), (39, 31), False)


def find_number_of_unique_positions_in_50_steps(data) -> int:
    return __bfs(int(data.splitlines()[0]), (1, 1), None, True)


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(find_fewest_steps_to_destination(data)))
        print("Part 2: " + str(find_number_of_unique_positions_in_50_steps(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
