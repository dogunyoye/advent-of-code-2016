import os.path
import re

DATA = os.path.join(os.path.dirname(__file__), 'day08.txt')


def __generate_pixels_map(width, depth) -> dict:
    pixels_map = {}
    for i in range(0, depth):
        for j in range(0, width):
            pixels_map[(i, j)] = "."
    return pixels_map


def __parse_instructions(data) -> list:
    instructions = []
    for line in data.splitlines():
        if "rect" in line:
            parts = re.findall(r'rect (\d+)x(\d+)', line)[0]
            instructions.append(("rect", int(parts[0]), int(parts[1])))
        elif "rotate column" in line:
            parts = re.findall(r'rotate column x=(\d+) by (\d+)', line)[0]
            instructions.append(("rotate column", int(parts[0]), int(parts[1])))
        elif "rotate row" in line:
            parts = re.findall(r'rotate row y=(\d+) by (\d+)', line)[0]
            instructions.append(("rotate row", int(parts[0]), int(parts[1])))
    return instructions


def __print_grid(pixels_map, width, depth):
    grid = [[0 for i in range(width)] for j in range(depth)]
    for i in range(0, depth):
        for j in range(0, width):
            pos = (i, j)
            grid[i][j] = pixels_map[pos]

    for i in range(0, depth):
        line = ""
        for j in range(0, width):
            line += grid[i][j]
        print(line)
    print()


def __apply_instructions(instructions, pixels_map, grid_width, grid_depth):
    for instruction in instructions:
        action = instruction[0]
        to_shift = []
        visited = set()

        if action == "rect":
            width, depth = instruction[1], instruction[2]
            for i in range(0, depth):
                for j in range(0, width):
                    pixels_map[(i, j)] = '#'
        elif action == "rotate column":
            column, shift = instruction[1], instruction[2]
            for i in range(grid_depth - 1, -1, -1):
                if pixels_map[(i, column)] == '#':
                    to_shift.append((i, column))

            for p in to_shift:
                next_pos = ((p[0] + shift) % grid_depth, column)
                if p not in visited:
                    pixels_map[p] = "."
                pixels_map[next_pos] = "#"
                visited.add(next_pos)
        elif action == "rotate row":
            row, shift = instruction[1], instruction[2]
            for i in range(grid_width - 1, -1, -1):
                if pixels_map[(row, i)] == '#':
                    to_shift.append((row, i))

            for p in to_shift:
                next_pos = (row, (p[1] + shift) % grid_width)
                if p not in visited:
                    pixels_map[p] = "."
                pixels_map[next_pos] = '#'
                visited.add(next_pos)


def calculate_number_of_lit_pixels(data) -> int:
    width, depth = 50, 6
    pixels_map = __generate_pixels_map(width, depth)
    instructions = __parse_instructions(data)
    __apply_instructions(instructions, pixels_map, width, depth)
    return len(list(filter(lambda v: v == '#', pixels_map.values())))


def display_code_on_screen(data):
    width, depth = 50, 6
    pixels_map = __generate_pixels_map(width, depth)
    instructions = __parse_instructions(data)
    __apply_instructions(instructions, pixels_map, width, depth)
    __print_grid(pixels_map, width, depth)


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(calculate_number_of_lit_pixels(data)))
        print("Part 2: "), display_code_on_screen(data)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
