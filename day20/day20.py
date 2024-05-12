import os.path

DATA = os.path.join(os.path.dirname(__file__), 'day20.txt')


def __create_ranges(data) -> list:
    ranges = []
    for line in data.splitlines():
        parts = line.split("-")
        ranges.append((int(parts[0]), int(parts[1])))
    return ranges


def __combine_ranges(data) -> list:
    ranges = __create_ranges(data)
    ranges = sorted(ranges, key=lambda r: r[0])

    while True:
        has_union = False
        intersection, to_remove = [], []

        for i in range(0, len(ranges) - 1):
            for j in range(i + 1, len(ranges)):
                first, second = ranges[i], ranges[j]
                first_min, first_max = first[0], first[1]
                second_min, second_max = second[0], second[1]

                if first_min <= second_min <= first_max <= second_max:  # right overlap
                    intersection.append((first_min, second_max))
                elif second_min <= first_min <= second_max <= first_max and first_max >= second_min:  # left overlap
                    intersection.append((second_min, first_max))
                elif first_min <= second_min <= first_max and first_min <= second_max <= first_max:  # within
                    has_union = True
                    to_remove.append(j)
                    break

                if len(intersection) == 1:
                    has_union = True
                    to_remove.append(i)
                    to_remove.append(j)
                    break

            if has_union:
                break

        for r in to_remove[::-1]:
            del ranges[r]

        if len(intersection) == 1:
            ranges.append(intersection[0])

        ranges = sorted(ranges, key=lambda x: x[0])
        if not has_union:
            break

    return ranges


def find_lowest_unblocked_ip_value(data) -> int:
    ranges = __combine_ranges(data)

    for i in range(0, len(ranges) - 1):
        r0, r1 = ranges[i], ranges[i + 1]
        if r0[1] + 1 != r1[0]:
            return r0[1] + 1

    raise Exception("No solution found!")


def calculate_number_of_ips_allowed_by_blacklist(data) -> int:
    ranges = __combine_ranges(data)
    result = 0

    for i in range(0, len(ranges) - 1):
        r0, r1 = ranges[i], ranges[i + 1]
        if r0[1] + 1 != r1[0]:
            result += r1[0] - r0[1] - 1

    return result


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(find_lowest_unblocked_ip_value(data)))
        print("Part 2: " + str(calculate_number_of_ips_allowed_by_blacklist(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
