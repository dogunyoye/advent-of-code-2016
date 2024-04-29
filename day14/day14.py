import os.path

DATA = os.path.join(os.path.dirname(__file__), 'day14.txt')


def find_index_that_produces_64th_key(data) -> int:
    salt = int(data.splitlines()[0])
    index = 0
    return 0


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(find_index_that_produces_64th_key(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
