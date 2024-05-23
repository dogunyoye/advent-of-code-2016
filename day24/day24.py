import os.path

DATA = os.path.join(os.path.dirname(__file__), 'day24.txt')


def __create_map(data) -> tuple:
    layout = {}
    locations = set()
    for i, line in enumerate(data.splitlines()):
        for j in range(0, len(line)):
            if line[j] != "#":
                layout[(i, j)] = line[j]
                if line[j].isnumeric() and line[j] != "0":
                    locations.add((i, j))
    return layout, locations


def calculate_fewest_steps_to_reach_all_locations(data) -> int:
    layout, locations = __create_map(data)
    print(layout)
    print(locations)
    return 0


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(calculate_fewest_steps_to_reach_all_locations(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
