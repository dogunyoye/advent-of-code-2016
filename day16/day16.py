import os.path

DATA = os.path.join(os.path.dirname(__file__), 'day16.txt')


def __find_checksum(required_length, data) -> str:
    a = data.splitlines()[0]

    while len(a) < required_length:
        b = a
        b = b[::-1]
        new_b = ""
        for i in range(0, len(b)):
            if b[i] == "0":
                new_b += "1"
            elif b[i] == "1":
                new_b += "0"
        a += "0" + new_b

    a = a[:required_length]

    while True:
        new_a = ""
        for i in range(0, len(a) - 1, 2):
            c0, c1 = a[i], a[i + 1]
            if c0 == c1:
                new_a += "1"
            else:
                new_a += "0"
        a = new_a
        if len(a) % 2 != 0:
            return a


def find_correct_checksum(data) -> str:
    return __find_checksum(272, data)


def find_correct_checksum_of_second_disk(data) -> str:
    return __find_checksum(35651584, data)


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + find_correct_checksum(data))
        print("Part 2: " + find_correct_checksum_of_second_disk(data))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
