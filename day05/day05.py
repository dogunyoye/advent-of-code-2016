import hashlib
import os.path

DATA = os.path.join(os.path.dirname(__file__), 'day05.txt')


def find_password(data) -> str:
    index = 0
    password = ""
    while True:
        candidate = hashlib.md5((data + str(index)).encode()).hexdigest()
        if candidate.startswith("00000"):
            password += candidate[5]
            if len(password) == 8:
                return password
        index += 1


def find_actual_password(data) -> str:
    index, changes = 0, 0
    password = ["_", "_", "_", "_", "_", "_", "_", "_"]

    while True:
        candidate = hashlib.md5(((data + str(index)).encode())).hexdigest()
        idx = candidate[5]
        if candidate.startswith("00000") and idx.isnumeric() and int(idx) < 8 and password[int(idx)] == "_":
            password[int(idx)] = str(candidate[6])
            changes += 1
            if changes == 8:
                return "".join(password)
        index += 1


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + find_password(data))
        print("Part 2: " + find_actual_password(data))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
