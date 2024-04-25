import os.path
import re
from math import prod

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
    bots, outputs = __initialise_bots(data), {}
    target = (17, 61)

    while True:
        for k, v in bots.items():
            values = v[0]
            if len(values) == 2:
                values.sort()
                if (values[0], values[1]) == target:
                    return k

                for i, dest in enumerate([v[1], v[2]]):
                    bot_or_output_id = int(dest.split(" ")[1])
                    if dest.startswith("bot"):
                        bots[bot_or_output_id][0].append(values[i])
                    else:
                        if bot_or_output_id not in outputs.keys():
                            outputs[bot_or_output_id] = [values[i]]
                        else:
                            outputs[bot_or_output_id].append(values[i])

                values.clear()


def find_product_of_outputs_with_one_chip(data) -> int:
    bots, outputs = __initialise_bots(data), {0: [], 1: [], 2: []}

    while True:
        for k, v in bots.items():
            values = v[0]
            if len(values) == 2:
                values.sort()

                for i, dest in enumerate([v[1], v[2]]):
                    bot_or_output_id = int(dest.split(" ")[1])
                    if dest.startswith("bot"):
                        bots[bot_or_output_id][0].append(values[i])
                    else:
                        if bot_or_output_id not in outputs.keys():
                            outputs[bot_or_output_id] = [values[i]]
                        else:
                            outputs[bot_or_output_id].append(values[i])

                if len(outputs[0]) == 1 and len(outputs[1]) == 1 and len(outputs[2]) == 1:
                    return prod([outputs[0][0], outputs[1][0], outputs[2][0]])

                values.clear()


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(find_bot_id_which_compares_61_and_17(data)))
        print("Part 2: " + str(find_product_of_outputs_with_one_chip(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
