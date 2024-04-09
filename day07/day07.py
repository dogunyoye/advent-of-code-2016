import os.path

DATA = os.path.join(os.path.dirname(__file__), 'day07.txt')


def __find_brackets_indices(line) -> list:
    indices, pair = [], []
    for i in range(0, len(line)):
        if line[i] == "[":
            pair.append(i)
        elif line[i] == "]":
            pair.append(i)
            indices.append(pair)
            pair = []
    return indices


def __is_within_brackets(indices, idx) -> bool:
    for pair in indices:
        if pair[0] <= idx <= pair[1]:
            return True
    return False


def calculate_number_of_ips_supporting_tls(data) -> int:
    result = 0
    for line in data.splitlines():
        indices = __find_brackets_indices(line)
        has_palindrome = False
        for i in range(0, len(line) - 3):
            seq = line[i:i + 4]
            if (seq == seq[::-1]) and (line[i] != line[i + 1]):
                if __is_within_brackets(indices, i):
                    has_palindrome = False
                    break
                has_palindrome = True
        if has_palindrome:
            result += 1
    return result


def calculate_number_of_ips_supporting_ssl(data) -> int:
    result = 0

    for line in data.splitlines():
        outside_brackets, inside_brackets = [], []
        indices = __find_brackets_indices(line)
        for i in range(0, len(line) - 2):
            seq = line[i:i + 3]
            if (seq == seq[::-1]) and (line[i] != line[i + 1]):
                if __is_within_brackets(indices, i):
                    inside_brackets.append(seq)
                else:
                    outside_brackets.append(seq)

        found = False
        for s1 in outside_brackets:
            for s2 in inside_brackets:
                if str(s1[1] + s1[0] + s1[1]) == s2:
                    result += 1
                    found = True
                    break
            if found:
                break

    return result


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(calculate_number_of_ips_supporting_tls(data)))
        print("Part 2: " + str(calculate_number_of_ips_supporting_ssl(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
