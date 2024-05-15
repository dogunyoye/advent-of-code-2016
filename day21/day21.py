import os.path
import re
from itertools import permutations

DATA = os.path.join(os.path.dirname(__file__), 'day21.txt')


class Scrambler(object):

    def __init__(self, password, operations):
        self.password = password
        self.operations = operations

    def __swap_position(self, position0, position1):
        x = list(self.password)
        temp = x[position0]
        x[position0] = x[position1]
        x[position1] = temp
        self.password = ''.join(x)

    def __swap_letter(self, letter0, letter1):
        idx0, idx1 = self.password.index(letter0), self.password.index(letter1)
        self.__swap_position(idx0, idx1)

    def __reverse(self, start, end):
        x = list(self.password)
        x[start:end + 1] = reversed(x[start:end + 1])
        self.password = ''.join(x)

    def __rotate_steps(self, direction, steps):
        if direction == "left":
            self.password = self.password[steps:] + self.password[0:steps]
        else:
            self.password = self.password[len(self.password) - steps:] + self.password[0: len(self.password) - steps]

    def __move(self, letter_idx, insertion_point):
        x = list(self.password)
        del x[letter_idx]
        x.insert(insertion_point, self.password[letter_idx])
        self.password = ''.join(x)

    def __rotate_position(self, letter):
        letter_idx = self.password.index(letter)
        direction = "right"
        if letter_idx >= 4:
            self.__rotate_steps(direction, 2 + letter_idx)
        else:
            self.__rotate_steps(direction, 1 + letter_idx)
        return

    def scramble(self) -> str:
        for line in self.operations:
            if line.startswith("swap position"):
                parts = re.findall(r'swap position (\d+) with position (\d+)', line)[0]
                self.__swap_position(int(parts[0]), int(parts[1]))
            elif line.startswith("swap letter"):
                parts = re.findall(r'swap letter ([a-z]) with letter ([a-z])', line)[0]
                self.__swap_letter(parts[0], parts[1])
            elif line.startswith("reverse positions"):
                parts = re.findall(r'reverse positions (\d+) through (\d+)', line)[0]
                self.__reverse(int(parts[0]), int(parts[1]))
            elif line.startswith("rotate based"):
                parts = re.findall(r'rotate based on position of letter ([a-z])', line)[0]
                self.__rotate_position(parts[0])
            elif line.startswith("move position"):
                parts = re.findall(r'move position (\d+) to position (\d+)', line)[0]
                self.__move(int(parts[0]), int(parts[1]))
            else:
                parts = re.findall(r'rotate (left|right) (\d+) step[s]*', line)[0]
                self.__rotate_steps(parts[0], int(parts[1]))
        return self.password


def scramble_password(data) -> str:
    password = "abcdefgh"
    scrambler = Scrambler(password, data.splitlines())
    return scrambler.scramble()


def unscramble_password(data) -> str:
    scrambled_password = "fbgdceah"
    operations = data.splitlines()
    for p in permutations(scrambled_password):
        candidate_password = ''.join(p)
        scrambler = Scrambler(candidate_password, operations)
        if scrambled_password == scrambler.scramble():
            return candidate_password
    raise Exception("Could not find password")


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + scramble_password(data))
        print("Part 2: " + unscramble_password(data))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
