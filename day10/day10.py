import os.path
import re

DATA = os.path.join(os.path.dirname(__file__), 'day10.txt')


def __initialise_bots(data) -> dict:
    bots = {}
    for line in data.splitlines():
        if line.startswith("value"):
            parts = re.findall(r'value (\d+) goes to bot (\d+)', line)[0]
            value, bot_id = int(parts[0]), int(parts[1])
            if bot_id not in bots.keys():
                bots[bot_id] = ([value], "", "")
            else:
                bots[bot_id][0].append(value)
                bots[bot_id][0].sort()

        if line.startswith("bot"):
            parts = re.findall(r'bot (\d+) gives low to ([a-z]+) (\d+) and high to ([a-z]+) (\d+)', line)[0]
            bot_id, low, high = int(parts[0]), str(parts[1] + " " + str(parts[2])), str(parts[3] + " " + str(parts[4]))
            if bot_id not in bots.keys():
                bots[bot_id] = ([], low, high)
            else:
                bots[bot_id] = (bots[bot_id][0], low, high)
    return bots


def find_bot_id_which_compares_61_and_17(data) -> int:
    print(__initialise_bots(data))
    return 0


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(find_bot_id_which_compares_61_and_17(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
