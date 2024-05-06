import os.path

DATA = os.path.join(os.path.dirname(__file__), 'day18.txt')


def __create_floor_plan(first_row) -> dict:
    floor_plan = {}
    for i in range(0, len(first_row)):
        floor_plan[(0, i)] = first_row[i]
    return floor_plan


def print_floor_plan(floor_plan):
    for i in range(0, 10):
        line = ""
        for j in range(0, 10):
            line += floor_plan[(i, j)]
        print(line)


def trap_check(neighbours, floor_plan) -> int:
    count = 0
    left, centre, right = neighbours[0], neighbours[1], neighbours[2]

    if (left in floor_plan and floor_plan[left] == "^") and floor_plan[centre] == "^" and (
            right not in floor_plan or floor_plan[right] == "."):
        count += 1
    if floor_plan[centre] == "^" and (right in floor_plan and floor_plan[right] == "^") and (
            left not in floor_plan or floor_plan[left] == "."):
        count += 1
    if (left in floor_plan and floor_plan[left] == "^") and floor_plan[centre] == "." and (
            right not in floor_plan or floor_plan[right] == "."):
        count += 1
    if (right in floor_plan and floor_plan[right] == "^") and floor_plan[centre] == "." and (
            left not in floor_plan or floor_plan[left] == "."):
        count += 1

    return count


def __calculate(data, rows) -> int:
    floor_plan = __create_floor_plan(data.splitlines()[0])
    length = len(data.splitlines()[0])
    adjacent = [(-1, -1), (-1, 0), (-1, 1)]
    result = 0

    for i in range(1, rows):
        for j in range(0, length):
            position = (i, j)
            neighbours = []
            for a in adjacent:
                neighbours.append((position[0] + a[0], position[1] + a[1]))

            count = trap_check(neighbours, floor_plan)
            if count == 1:
                floor_plan[position] = "^"
            else:
                floor_plan[position] = "."

        for k in range(0, length):
            if floor_plan[(i-1, k)] == ".":
                result += 1
            del floor_plan[(i-1, k)]

    for v in floor_plan.values():
        if v == ".":
            result += 1

    return result


def calculate_number_of_safe_tiles(data) -> int:
    return __calculate(data, 40)


def calculate_number_of_safe_tiles_part_two(data) -> int:
    # very slow
    # "cycle detection" will likely optimise this?
    return __calculate(data, 400000)


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(calculate_number_of_safe_tiles(data)))
        print("Part 2: " + str(calculate_number_of_safe_tiles_part_two(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
