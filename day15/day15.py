import os.path
import re

DATA = os.path.join(os.path.dirname(__file__), 'day15.txt')


class Disc(object):

    def __init__(self, disc_id, positions, start):
        self.disc_id = disc_id
        self.positions = positions
        self.pointer = positions.index(start)

    def rotate(self):
        self.pointer = (self.pointer + 1) % len(self.positions)

    def position(self) -> int:
        return self.positions[self.pointer]


def __create_discs(data) -> list:
    discs = []
    for line in data.splitlines():
        parts = re.findall(r'Disc #(\d+) has (\d+) positions; at time=0, it is at position (\d+)', line)[0]
        discs.append(Disc(int(parts[0]), [*range(0, int(parts[1]))], int(parts[2])))
    return discs


def __all_discs_at_position_zero(discs) -> bool:
    for d in discs:
        if d.position() != 0:
            return False
    return True


def find_time_to_press_button(data) -> int:
    discs = __create_discs(data)
    time = 0

    while not __all_discs_at_position_zero(discs):
        time += 1
        discs = __create_discs(data)
        for i, d in enumerate(discs):
            for _ in range(0, time+d.disc_id):
                d.rotate()

    return time


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(find_time_to_press_button(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
