import copy
import os.path
from itertools import combinations
from collections import deque

DATA = os.path.join(os.path.dirname(__file__), 'day11.txt')

# Input
"""
The first floor contains a polonium generator, a thulium generator, a thulium-compatible microchip,
a promethium generator, a ruthenium generator, a ruthenium-compatible microchip, a cobalt generator,
and a cobalt-compatible microchip.

The second floor contains a polonium-compatible microchip and a promethium-compatible microchip.

The third floor contains nothing relevant.

The fourth floor contains nothing relevant.
"""

"""
polonium generator = POG
thulium generator = THG
thulium-compatible microchip = THM
promethium generator = PRG
ruthenium generator = RTG
cobalt generator = COG
cobalt-compatible microchip = COM
polonium-compatible microchip = POM
promethium-compatible microchip = PRM

(Part 2)
elerium generator = ELG
elerium-compatible microchip = ELM
dilithium generator = DIG
dilithium-compatible microchip = DIM
"""


def __neighbours(floor) -> list:
    if floor == 1:
        return [2]

    if floor == 4:
        return [3]

    return [floor + 1, floor - 1]


def __all_same_type(items, item_type) -> bool:
    for i in items:
        if not i.endswith(item_type):
            return False
    return True


def __floor_plan(floors) -> str:
    floor_plan = {}
    for k, v in floors.items():
        floor_plan[k] = []
        for i in v:
            if i.endswith("G"):
                floor_plan[k].append("G")
            elif i.endswith("M"):
                floor_plan[k].append("M")
        floor_plan[k].sort()
    return str(floor_plan)


def __are_floors_valid(floors, chip_to_gen) -> bool:
    for v in floors.values():
        if (len(v) == 0 or len(v) == (len(chip_to_gen) * 2)
                or __all_same_type(v, "M") or __all_same_type(v, "G")):
            continue

        floor_set = set(v)
        for f in v:
            if f.endswith("M") and chip_to_gen[f] in v:
                floor_set.remove(f)
                floor_set.remove(chip_to_gen[f])

        if len(floor_set) == 0 or __all_same_type(floor_set, "G"):
            continue
        return False
    return True


def __traverse_floors(floors, chip_to_gen) -> int:
    queue, seen = deque(), set()
    queue.append((0, 1, floors))

    while len(queue) != 0:
        current = queue.popleft()
        steps, level, current_floors = current[0], current[1], current[2]

        # with BFS, the first result we reach is guaranteed to be the minimum
        if len(current_floors[4]) == (len(chip_to_gen) * 2):
            return steps

        neighbours = __neighbours(level)
        floor_items = current_floors[level]

        for n in neighbours:
            for i in floor_items:
                copied_floors = copy.deepcopy(current_floors)
                copied_floors[n].append(i)
                copied_floors[level].remove(i)
                state = (__floor_plan(copied_floors), n)
                if __are_floors_valid(copied_floors, chip_to_gen) and state not in seen:
                    seen.add(state)
                    queue.append((steps + 1, n, copied_floors))

        if len(floor_items) > 1:
            item_combos = list(combinations(floor_items, 2))
            for n in neighbours:
                for c in item_combos:
                    copied_floors = copy.deepcopy(current_floors)
                    copied_floors[n].extend(c)
                    copied_floors[level] = [elem for elem in copied_floors[level] if elem not in c]
                    state = (__floor_plan(copied_floors), n)
                    if __are_floors_valid(copied_floors, chip_to_gen) and state not in seen:
                        seen.add(state)
                        queue.append((steps + 1, n, copied_floors))


def find_minimum_steps_required_to_bring_all_items_to_floor_four() -> int:
    # Example
    # floors = {1: ["HM", "LM"], 2: ["HG"], 3: ["LG"], 4: []}
    # chip_to_gen = {"HM": "HG", "LM": "LG"}

    # Hard-coded input
    floors = {
        1: ["POG", "THG", "THM", "PRG", "RTG", "RTM", "COG", "COM"],
        2: ["POM", "PRM"],
        3: [],
        4: []
    }

    chip_to_gen = {"POM": "POG", "THM": "THG", "PRM": "PRG", "RTM": "RTG", "COM": "COG"}
    return __traverse_floors(floors, chip_to_gen)


def find_minimum_steps_required_to_bring_all_items_to_floor_four_with_extra_items() -> int:
    # Hard-coded input
    floors = {
        1: ["POG", "THG", "THM", "PRG", "RTG", "RTM", "COG", "COM", "ELG", "ELM", "DIG", "DIM"],
        2: ["POM", "PRM"],
        3: [],
        4: []
    }

    chip_to_gen = {"POM": "POG", "THM": "THG", "PRM": "PRG", "RTM": "RTG", "COM": "COG", "ELM": "ELG", "DIM": "DIG"}
    return __traverse_floors(floors, chip_to_gen)


def main() -> int:
    print("Part 1: " + str(find_minimum_steps_required_to_bring_all_items_to_floor_four()))
    print("Part 2: " + str(find_minimum_steps_required_to_bring_all_items_to_floor_four_with_extra_items()))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
