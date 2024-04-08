import os.path
from enum import Enum

DATA = os.path.join(os.path.dirname(__file__), 'day01.txt')


class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


def __manhattan_distance(start, end) -> int:
    return abs(start[0] - end[0]) + abs(start[1] - end[1])


def calculate_distance_easter_bunny_hq(data) -> int:
    direction = Direction.NORTH
    start, current_pos = (0, 0), (0, 0)

    for instruction in data.split(", "):
        ins_direction = instruction[0]
        ins_steps = eval(instruction[1:])

        value: int = direction.value
        if ins_direction == "R":
            direction = Direction((int(value + 1)) % 4)
        else:
            direction = Direction((int(value - 1)) % 4)

        if direction == Direction.NORTH:
            current_pos = (current_pos[0] - ins_steps, current_pos[1])
        elif direction == Direction.EAST:
            current_pos = (current_pos[0], current_pos[1] + ins_steps)
        elif direction == Direction.SOUTH:
            current_pos = (current_pos[0] + ins_steps, current_pos[1])
        else:
            current_pos = (current_pos[0], current_pos[1] - ins_steps)
    return __manhattan_distance(start, current_pos)


def add_visited_locations(direction, steps, current_pos, visited) -> tuple:
    for _ in range(steps):
        if direction == Direction.NORTH:
            current_pos = (current_pos[0] - 1, current_pos[1])
        elif direction == Direction.EAST:
            current_pos = (current_pos[0], current_pos[1] + 1)
        elif direction == Direction.SOUTH:
            current_pos = (current_pos[0] + 1, current_pos[1])
        else:
            current_pos = (current_pos[0], current_pos[1] - 1)

        if current_pos in visited:
            return current_pos, True
        visited.add(current_pos)

    return current_pos, False


def calculate_distance_from_the_first_location_visited_twice(data) -> int:
    direction = Direction.NORTH
    start, current_pos = (0, 0), (0, 0)
    visited = set()

    for instruction in data.split(", "):
        ins_direction = instruction[0]
        ins_steps = eval(instruction[1:])

        value: int = direction.value
        direction = Direction((int(value + 1)) % 4) if ins_direction == "R" else Direction((int(value - 1)) % 4)

        current_pos, found = add_visited_locations(direction, ins_steps, current_pos, visited)
        if found:
            return __manhattan_distance(start, current_pos)

    raise Exception("Could not find location visited twice!")


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(calculate_distance_easter_bunny_hq(data)))
        print("Part 2: " + str(calculate_distance_from_the_first_location_visited_twice(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
