import os.path

DATA = os.path.join(os.path.dirname(__file__), 'day19.txt')


def get_position(current_position, size) -> int:
    if current_position > (size // 2):
        return current_position - (size // 2) - 1

    return current_position + (size // 2) - 1


def find_position_of_elf_with_all_presents(data) -> int:
    elves = {}
    for k in range(1, int(data.splitlines()[0]) + 1):
        elves[k] = 1

    while True:
        if len(elves) == 1:
            return list(elves.keys())[0]

        remaining_keys = list(elves.keys())
        for i in range(0, len(remaining_keys), 2):
            removed = remaining_keys[(i + 1) % len(remaining_keys)]
            elves[remaining_keys[i]] += elves[removed]
            del elves[removed]


def find_position_of_elf_with_all_presents_with_revised_rotation(data) -> int:
    i = 1
    elves = int(data.splitlines()[0])
    while i * 3 < elves:
        i *= 3
    return elves - i


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(find_position_of_elf_with_all_presents(data)))
        print("Part 2: " + str(find_position_of_elf_with_all_presents_with_revised_rotation(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
