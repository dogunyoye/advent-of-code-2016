import os.path

DATA = os.path.join(os.path.dirname(__file__), 'day04.txt')


def calculate_sum_of_sector_ids_for_real_rooms(data) -> int:
    result = 0
    for line in data.splitlines():
        open_square_bracket = line.index('[')
        closed_square_bracket = line.index(']')
        last_dash = line.rfind('-')

        encrypted_name = line[0:last_dash]
        sector_id = eval(line[last_dash + 1:open_square_bracket])
        checksum = line[open_square_bracket + 1:closed_square_bracket]

        count_map = {}
        for i in range(0, len(encrypted_name)):
            if encrypted_name[i] != "-":
                count_map[encrypted_name[i]] = encrypted_name.count(encrypted_name[i])

        sorted_checksum = ""
        sorted_list = sorted(count_map.items(), key=lambda tup: (-tup[1], tup[0]))

        for e in sorted_list:
            sorted_checksum += e[0]

        if sorted_checksum[0:len(checksum)] == checksum:
            result += sector_id

    return result


def find_sector_id_for_north_pole_objects_room(data) -> int:
    for line in data.splitlines():
        open_square_bracket = line.index('[')
        last_dash = line.rfind('-')

        encrypted_name = line[0:last_dash]
        sector_id = eval(line[last_dash + 1:open_square_bracket])

        decrypted = ""
        for i in range(0, len(encrypted_name)):
            c = line[i]
            if c == "-":
                decrypted += " "
            else:
                decrypted += chr(((ord(c) - 97 + sector_id) % 26) + 97)
        if decrypted == "northpole object storage":
            return sector_id

    raise Exception("Could not find sector id!")


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(calculate_sum_of_sector_ids_for_real_rooms(data)))
        print("Part 2: " + str(find_sector_id_for_north_pole_objects_room(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
