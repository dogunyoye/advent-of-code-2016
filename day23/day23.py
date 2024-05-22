import os.path

DATA = os.path.join(os.path.dirname(__file__), 'day23.txt')


class Computer(object):

    def __init__(self, registers, program, instruction_pointer, part_two):
        self.registers = registers
        self.program = program
        self.instruction_pointer = instruction_pointer
        self.part_two = part_two

    @staticmethod
    def __parse_instruction(instruction) -> None | tuple:
        parts = instruction.split(" ")
        ins_type = parts[0]
        if ins_type == "cpy" or ins_type == "jnz":
            if len(parts) != 3:
                return None
            return parts[0], parts[1], parts[2]
        elif ins_type == "inc" or ins_type == "dec" or ins_type == "tgl":
            if len(parts) != 2:
                return None
            return parts[0], parts[1]
        raise Exception("Unknown instruction type: " + ins_type)

    def __cpy(self, source, reg):
        if reg.isnumeric():
            return

        if source.lstrip('-').isdigit():
            self.registers[reg] = int(source)
        else:
            self.registers[reg] = self.registers[source]

    def __inc(self, reg):
        if reg.isnumeric():
            return

        self.registers[reg] += 1

    def __dec(self, reg):
        if reg.isnumeric():
            return

        self.registers[reg] -= 1

    def __jnz(self, val, jmp):
        if val.lstrip('-').isdigit():
            v = int(val)
        else:
            v = self.registers[val]

        if jmp.lstrip('-').isdigit():
            jmp = int(jmp)
        else:
            jmp = self.registers[jmp]

        if v < 0:
            self.instruction_pointer -= int(jmp)
        elif v > 0:
            self.instruction_pointer += int(jmp)
        else:
            self.instruction_pointer += 1

    def __tgl(self, reg):
        v = self.registers[reg]
        pointer = self.instruction_pointer + v

        if pointer >= len(self.program):
            return

        instruction_string = self.program[pointer]
        instruction_type = self.__parse_instruction(instruction_string)[0]

        if instruction_type == "inc":
            self.program[pointer] = instruction_string.replace("inc", "dec")
        elif instruction_type == "dec":
            self.program[pointer] = instruction_string.replace("dec", "inc")
        elif instruction_type == "tgl":
            self.program[pointer] = instruction_string.replace("tgl", "inc")
        elif instruction_type == "jnz":
            self.program[pointer] = instruction_string.replace("jnz", "cpy")
        elif instruction_type == "cpy":
            self.program[pointer] = instruction_string.replace("cpy", "jnz")

    def execute_program(self):
        while 0 <= self.instruction_pointer < len(self.program):
            instruction = self.program[self.instruction_pointer]
            instruction = self.__parse_instruction(instruction)

            if instruction is not None:
                # !DISCLAIMER!: This is hard-coded specific to my input.
                # The general idea here is to optimise the loops in the
                # program. Many loops are incrementing/decrementing
                # register values by 1. This is slow and will take forever
                # to complete. Instead, we can shortcut this by reverse
                # engineering the program to see what condition is required
                # for each loop to terminate, and just adding/multiplying the
                # number iterations to each relevant register. Then, I can skip
                # to the instruction directly after the loop and continue the
                # program. I found 3 loops to optimise in my program. With these
                # correctly optimised, my solution returns the correct answer instantly.
                if self.part_two and self.instruction_pointer == 5:
                    self.registers["a"] += self.registers["c"] * self.registers["d"]
                    self.registers["c"] = 0
                    self.registers["d"] = 0
                    self.instruction_pointer = 10
                    continue

                if self.part_two and self.instruction_pointer == 13:
                    self.registers["c"] += self.registers["d"]
                    self.registers["d"] = 0
                    self.instruction_pointer = 16
                    continue

                if self.part_two and self.instruction_pointer == 21:
                    self.registers["a"] += abs(self.registers["d"])
                    self.registers["d"] = 0
                    self.instruction_pointer = 24
                    continue

                instruction_type = instruction[0]

                if instruction_type == "cpy":
                    self.__cpy(instruction[1], instruction[2])
                elif instruction_type == "inc":
                    self.__inc(instruction[1])
                elif instruction_type == "dec":
                    self.__dec(instruction[1])
                elif instruction_type == "tgl":
                    self.__tgl(instruction[1])
                elif instruction_type == "jnz":
                    self.__jnz(instruction[1], instruction[2])
                    continue

            self.instruction_pointer += 1


def find_value_for_safe(data) -> int:
    computer = Computer({"a": 7, "b": 0, "c": 0, "d": 0}, data.splitlines(), 0, False)
    computer.execute_program()
    return computer.registers["a"]


def find_real_value_for_safe(data) -> int:
    computer = Computer({"a": 12, "b": 0, "c": 0, "d": 0}, data.splitlines(), 0, True)
    computer.execute_program()
    return computer.registers["a"]


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(find_value_for_safe(data)))
        print("Part 2: " + str(find_real_value_for_safe(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
