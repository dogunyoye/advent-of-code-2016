import os.path

DATA = os.path.join(os.path.dirname(__file__), 'day19.txt')


def __initialise_elves(elves_size) -> dict:
    elves = {}
    for i in range(0, elves_size):
        elves[i] = 1
    return elves


def find_position_of_elf_with_all_presents(data) -> int:
    elves_size = int(data.splitlines()[0])
    elves, remaining = __initialise_elves(elves_size), []
    for k in elves.keys():
        remaining.append(k)
    current_elf = 0

    while True:
        elf = remaining[current_elf]
        next_elf = remaining[(remaining.index(elf) + 1) % len(remaining)]
        if elves[elf] > 0:
            elves[elf] += elves[next_elf]
            del elves[next_elf]
            remaining.remove(next_elf)

        if len(remaining) == 1:
            return remaining[0] + 1
        current_elf = (remaining.index(elf) + 1) % len(remaining)


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(find_position_of_elf_with_all_presents(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
