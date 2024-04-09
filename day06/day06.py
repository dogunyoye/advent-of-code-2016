import os.path

DATA = os.path.join(os.path.dirname(__file__), 'day06.txt')


def __build_count_map_list(lines, i) -> list:
    count_map = {}
    for line in lines:
        c = line[i]
        if c in count_map.keys():
            count_map[c] += 1
        else:
            count_map[c] = 0

    count_map = sorted(count_map.items(), key=lambda x: x[1])
    return count_map


def find_error_corrected_message(data) -> str:
    lines = data.splitlines()
    message = ""
    for i in range(0, len(lines[0])):
        count_map = __build_count_map_list(lines, i)
        message += count_map[-1][0]
    return message


def find_original_message(data) -> str:
    lines = data.splitlines()
    message = ""
    for i in range(0, len(lines[0])):
        count_map = __build_count_map_list(lines, i)
        message += count_map[0][0]
    return message


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + find_error_corrected_message(data))
        print("Part 2: " + find_original_message(data))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
