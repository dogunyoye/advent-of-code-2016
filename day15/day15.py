import os.path
import re

DATA = os.path.join(os.path.dirname(__file__), 'day15.txt')


class Disc(object):

    def __init__(self, disc_id, positions, start):
        self.disc_id = disc_id
        self.positions = positions
        self.start = start

    def steps_to_position0(self) -> int:
        idx = (self.start + self.disc_id) % self.positions
        return 0 if idx == 0 else self.positions - idx

    def size(self):
        return self.positions


def __create_discs(data) -> list:
    discs = []
    for line in data.splitlines():
        parts = re.findall(r'Disc #(\d+) has (\d+) positions; at time=0, it is at position (\d+)', line)[0]
        parts = list(map(int, parts))
        discs.append(Disc(parts[0], parts[1], parts[2]))
    return discs


# Modular arithmetic
# https://en.wikipedia.org/wiki/Modular_arithmetic#Congruence
#
# We have to find a time (t) such that the position on each wheel
# is 0. To do this, we need to know how many 'steps' away the starting position
# on each wheel is away from 0 (n) with respect the size of the disk (s).
# The equation is: t ≡ n mod s, which is the same as: t mod s = n mod s
#
# This can also be solved with the Chinese Remainder Theorem
# https://en.wikipedia.org/wiki/Chinese_remainder_theorem#Statement
# https://www.geeksforgeeks.org/introduction-to-chinese-remainder-theorem/
def __find_time(discs: list[Disc]) -> int:
    time = 0
    while True:
        all_discs_at_zero = True
        for d in discs:
            steps_to_zero = d.steps_to_position0()
            if time % d.size() != steps_to_zero % d.size():
                all_discs_at_zero = False
                break
        if all_discs_at_zero:
            return time
        time += 1


def find_time_to_press_button(data) -> int:
    return __find_time(__create_discs(data))


def find_time_to_press_button_part_two(data) -> int:
    discs = __create_discs(data)
    discs.append(Disc(len(discs) + 1, 11, 0))
    return __find_time(discs)


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(find_time_to_press_button(data)))
        print("Part 2: " + str(find_time_to_press_button_part_two(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
