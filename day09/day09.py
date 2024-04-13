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


def __length_until_first_marker(data) -> int:
    length = 0
    for i in range(0, len(data)):
        if data[i] == "(":
            return length
        length += 1
    return length


def __find_children(data, start, end) -> list:
    children = []
    if data[start] == "(":
        children.append(start)

    for i in range(start + 1, end):
        if i < len(data) - 1 and data[i] == ")" and data[i+1] == "(":
            break
        elif data[i] == "(":
            children.append(i)
    return children


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


def __traverse_compressed_data(data, idx) -> int:
    if idx == len(data):
        return 0

    if data[idx] != "(":
        return 1 + __traverse_compressed_data(data, idx + 1)

    marker = __find_marker(data, idx)
    parts = marker[1].split("x")
    seq_len, rep, rep_start = int(parts[0]), int(parts[1]), marker[3]
    print(data[rep_start:rep_start + seq_len])
    children = __find_children(data, rep_start, rep_start + seq_len)

    if len(children) == 0:
        # leaf
        return rep * seq_len + __traverse_compressed_data(data, rep_start + seq_len)

    result = 0

    # parent
    for c in children:
        result += rep * __traverse_compressed_data(data, c)

    return result + __traverse_compressed_data(data, rep_start + seq_len)


def calculate_decompressed_length_of_data_using_improved_format(data) -> int:
    return __traverse_compressed_data(data, 0)


def getLength(data):
    length = i = 0
    while i < len(data):
        if data[i] == '(':
            markerEnd = data.find(')', i)
            (chars, repeat) = [int(x) for x in data[i + 1:markerEnd].split('x')]
            length += getLength(data[markerEnd + 1:markerEnd + chars + 1]) * repeat
            i = markerEnd + chars
        else:
            length += 1
        i += 1
    return length


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(calculate_decompressed_length_of_data(data)))
        print("Part 2: " + str(calculate_decompressed_length_of_data_using_improved_format(data)))
        print(getLength(data))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
