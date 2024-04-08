import os.path

DATA = os.path.join(os.path.dirname(__file__), 'day03.txt')


def __is_valid_triangle(dimensions) -> bool:
    return ((dimensions[0] + dimensions[1] > dimensions[2]) and
            (dimensions[0] + dimensions[2] > dimensions[1]) and
            (dimensions[1] + dimensions[2] > dimensions[0]))


def find_number_of_possible_triangles(data) -> int:
    count = 0
    for line in data.splitlines():
        dimensions = [eval(p) for p in line.split()]
        if __is_valid_triangle(dimensions):
            count += 1
    return count


def find_number_of_possible_triangles_reading_data_by_columns(data) -> int:
    rows = []
    count = 0
    for line in data.splitlines():
        rows.append([eval(p) for p in line.split()])

    for i in range(0, 3):
        for j in range(0, len(rows) - 2, 3):
            dimensions = rows[j][i], rows[j + 1][i], rows[j + 2][i]
            if __is_valid_triangle(dimensions):
                count += 1
    return count


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(find_number_of_possible_triangles(data)))
        print("Part 2: " + str(find_number_of_possible_triangles_reading_data_by_columns(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
