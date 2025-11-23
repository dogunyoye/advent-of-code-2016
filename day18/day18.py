import os.path

DATA = os.path.join(os.path.dirname(__file__), 'day18.txt')

TRAPS = {
    ('^','^','.'),
    ('.','^','^'),
    ('^','.','.'),
    ('.','.','^')
}


def print_floor_plan(floor_plan):
    for i in range(0, 10):
        line = ""
        for j in range(0, 10):
            line += floor_plan[(i, j)]
        print(line)


def __calculate(data, rows) -> int:
    floor_plan = data.splitlines()[0]
    length = len(floor_plan)
    result = floor_plan.count(".")

    for _ in range(1, rows):
        next_row = []
        for j in range(0, length):
            left = "." if j - 1 < 0 else floor_plan[j - 1]
            centre = floor_plan[j]
            right = "." if j + 1 >= length else floor_plan[j + 1]

            if (left, centre, right) in TRAPS:
                next_row.append("^")
            else:
                next_row.append(".")
                result += 1

        floor_plan = ''.join(next_row)

    return result


def calculate_number_of_safe_tiles(data) -> int:
    return __calculate(data, 40)


def calculate_number_of_safe_tiles_part_two(data) -> int:
    # ~17s to complete (likely max speed for this implementation)
    # most optimised solution uses bitwise operations
    return __calculate(data, 400000)


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(calculate_number_of_safe_tiles(data)))
        print("Part 2: " + str(calculate_number_of_safe_tiles_part_two(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
