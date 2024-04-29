import os.path
from collections import deque

DATA = os.path.join(os.path.dirname(__file__), 'day13.txt')


def __get_value(position, favourite_number) -> str:
    # (x, y) -> j = x, i = y
    i, j = position[0], position[1]

    # x*x + 3*x + 2*x*y + y + y*y
    val = (j * j) + (3 * j) + (2 * j * i) + i + (i * i)
    val += favourite_number
    binary = format(val, 'b')
    number_of_ones = binary.count('1')

    if number_of_ones % 2 == 0:
        return '.'
    return '#'


def __bfs(favourite_number, start, end) -> int:
    queue, visited = deque(), set()
    queue.append((0, start))

    while len(queue) != 0:
        current = queue.popleft()
        steps, position = current[0], current[1]
        if position == end:
            return steps

        i, j = position[0], position[1]
        neighbors = [(i, j - 1), (i - 1, j), (i, j + 1), (i + 1, j)]
        neighbors = \
            (list(filter(lambda p: p[0] >= 0 and p[1] >= 0 and __get_value(p, favourite_number) == '.', neighbors)))

        for n in neighbors:
            if n not in visited:
                queue.append((steps + 1, n))
                visited.add(n)


def find_fewest_steps_to_destination(data) -> int:
    return __bfs(int(data.splitlines()[0]), (1, 1), (39, 31))


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(find_fewest_steps_to_destination(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
