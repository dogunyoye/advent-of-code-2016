import hashlib
import os.path

DATA = os.path.join(os.path.dirname(__file__), 'day14.txt')


def __find_index(data, hash_gen_fn) -> int:
    salt, index = data.splitlines()[0], 0

    pending: list[tuple[int, str, int]] = []
    completed: list[int] = []
    found = set()

    while True:
        candidate = hash_gen_fn(salt, index)
        to_remove = []

        for i, p in enumerate(pending):
            if p[2] == index and p[0] in found:
                completed.append(p[0])
                to_remove.append(i)
            elif p[1] in candidate:
                if p[0] in found:
                    to_remove.append(i)
                else:
                    found.add(p[0])

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


def __hash_gen_part_one(salt, index) -> str:
    return hashlib.md5((salt + str(index)).encode()).hexdigest()


def __hash_gen_part_two(salt, index) -> str:
    candidate = __hash_gen_part_one(salt, index)
    for i in range(0, 2016):
        candidate = hashlib.md5(candidate.encode()).hexdigest()
    return candidate


def find_index_that_produces_64th_key(data) -> int:
    return __find_index(data, __hash_gen_part_one)


def find_index_that_produces_64th_key_part_two(data) -> int:
    return __find_index(data, __hash_gen_part_two)


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(find_index_that_produces_64th_key(data)))
        print("Part 2: " + str(find_index_that_produces_64th_key_part_two(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
