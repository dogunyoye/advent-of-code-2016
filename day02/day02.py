import os.path

DATA = os.path.join(os.path.dirname(__file__), 'day02.txt')


def __get_code(keypad, current_pos, data) -> str:
    code = ""
    for line in data.splitlines():
        for i in range(0, len(line)):
            direction = line[i]

            if direction == "U":
                next_pos = (current_pos[0] - 1, current_pos[1])
            elif direction == "R":
                next_pos = (current_pos[0], current_pos[1] + 1)
            elif direction == "D":
                next_pos = (current_pos[0] + 1, current_pos[1])
            else:
                next_pos = (current_pos[0], current_pos[1] - 1)

            if next_pos in keypad.keys():
                current_pos = next_pos

        code += str(keypad[current_pos])
    return code


def find_bathroom_code(data) -> str:
    current_pos = (1, 1)
    keypad = {
        (0, 0): 1, (0, 1): 2, (0, 2): 3,
        (1, 0): 4, (1, 1): 5, (1, 2): 6,
        (2, 0): 7, (2, 1): 8, (2, 2): 9
    }

    return __get_code(keypad, current_pos, data)


def find_correct_bathroom_code(data) -> str:
    current_pos = (3, 0)
    keypad = {
        (0, 2): "1",
        (1, 1): "2", (1, 2): "3", (1, 3): "4",
        (2, 0): "5", (2, 1): "6", (2, 2): "7", (2, 3): "8", (2, 4): "9",
        (3, 1): "A", (3, 2): "B", (3, 3): "C",
        (4, 2): "D"
    }

    return __get_code(keypad, current_pos, data)


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + find_bathroom_code(data))
        print("Part 2: " + find_correct_bathroom_code(data))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
