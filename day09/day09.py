import os.path

DATA = os.path.join(os.path.dirname(__file__), 'day09.txt')


def __find_marker(data, start_idx) -> tuple:
    for i in range(start_idx, len(data)):
        c = data[i]
        if c == "(":
            start = i
            marker = ""
            while data[i + 1] != ")":
                i += 1
                marker += data[i]
            return True, marker, start, i + 2
    return False, "", -1, -1


def calculate_decompressed_length_of_data(data) -> int:
    result = 0
    for line in data.splitlines():
        idx = 0
        decompressed = line
        marker = __find_marker(decompressed, idx)
        while marker[0]:
            parts = marker[1].split("x")
            seq_len, rep, rep_start = int(parts[0]), int(parts[1]), marker[3]
            decompressed_slice = decompressed[rep_start:rep_start + seq_len]
            decompressed = (decompressed[0:marker[2]] + (decompressed_slice * rep) +
                            decompressed[rep_start + len(decompressed_slice):])
            idx += (len(decompressed_slice) * rep)
            marker = __find_marker(decompressed, idx)
        result += len(decompressed)

    return result


def __is_marker_parent(message, idx) -> bool:
    return message[idx] == "("


def __traverse_compressed_data(data, idx) -> int:
    if idx == len(data):
        return 0

    if data[idx] != "(":
        return 1 + __traverse_compressed_data(data, idx + 1)

    marker = __find_marker(data, idx)
    parts = marker[1].split("x")
    seq_len, rep, rep_start = int(parts[0]), int(parts[1]), marker[3]
    children = []

    if __is_marker_parent(data, rep_start):
        i = idx + 1
        while i != rep_start + seq_len:
            m = __find_marker(data, i)
            if not m[0] or m[2] == rep_start + seq_len:
                break
            if __is_marker_parent(data, m[3]):
                parts = m[1].split("x")
                i = m[3] + int(parts[0])
            else:
                i = m[3]
            children.append(m[2])

    if len(children) == 0:
        # leaf
        return rep * seq_len

    result = 0

    # parent
    for c in children:
        result += rep * __traverse_compressed_data(data, c)

    return result


def calculate_decompressed_length_of_data_using_improved_format(data) -> int:
    length, idx = 0, 0
    message = data
    chunks = []
    while idx < len(message):
        if message[idx] != "(":
            length += 1
            idx += 1
        else:
            marker = __find_marker(message, idx)
            if not marker[0]:
                break
            parts = marker[1].split("x")
            seq_len, rep, rep_start = int(parts[0]), int(parts[1]), marker[3]
            chunks.append((message[marker[2]:rep_start + seq_len], rep))
            idx = rep_start + seq_len

    for c in chunks:
        length += __traverse_compressed_data(c[0], 0)

    return length


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(calculate_decompressed_length_of_data(data)))
        print("Part 2: " + str(calculate_decompressed_length_of_data_using_improved_format(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
