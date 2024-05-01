import hashlib
import os.path

DATA = os.path.join(os.path.dirname(__file__), 'day14.txt')


def find_index_that_produces_64th_key(data) -> int:
    salt, index = data.splitlines()[0], 0
    pending, completed = [], []
    found = set()

    while True:
        candidate = hashlib.md5((salt + str(index)).encode()).hexdigest()
        to_remove = []

        for i, p in enumerate(pending):
            if p[2] == index and p[0] in found:
                completed.append(int(p[0]))  # int conversion to stop PyCharm complaining.
                to_remove.append(i)
            elif p[1] in candidate:
                if p[0] in found:
                    to_remove.append(i)
                else:
                    found.add(int(p[0]))  # int conversion to stop PyCharm complaining.

        if len(completed) == 64:
            return completed[63]

        to_remove.reverse()
        for r in to_remove:
            del pending[r]

        for i in range(0, len(candidate) - 2):
            if candidate[i] == candidate[i + 1] == candidate[i + 2]:
                pending.append((index, candidate[i] * 5, 1000 + index))
                break

        index += 1


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(find_index_that_produces_64th_key(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
