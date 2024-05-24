import os.path
from itertools import count

DATA = os.path.join(os.path.dirname(__file__), 'day25.txt')


class Computer(object):

    def __init__(self, registers, program, instruction_pointer):
        self.registers = registers
        self.program = program
        self.instruction_pointer = instruction_pointer
        self.sequence = ""

    @staticmethod
    def __parse_instruction(instruction) -> None | tuple:
        parts = instruction.split(" ")
        ins_type = parts[0]
        if ins_type == "cpy" or ins_type == "jnz":
            if len(parts) != 3:
                return None
            return parts[0], parts[1], parts[2]
        elif ins_type == "inc" or ins_type == "dec" or ins_type == "tgl" or ins_type == "out":
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
        elif instruction_type == "out":
            self.program[pointer] = instruction_string.replace("out", "inc")
        elif instruction_type == "jnz":
            self.program[pointer] = instruction_string.replace("jnz", "cpy")
        elif instruction_type == "cpy":
            self.program[pointer] = instruction_string.replace("cpy", "jnz")

    def __out(self, x):
        if x.isnumeric():
            self.sequence += str(x)
        else:
            self.sequence += str(self.registers[x])

    def execute_program(self):
        while 0 <= self.instruction_pointer < len(self.program):
            instruction = self.program[self.instruction_pointer]
            instruction = self.__parse_instruction(instruction)

            if instruction is not None:
                instruction_type = instruction[0]

                if instruction_type == "cpy":
                    self.__cpy(instruction[1], instruction[2])
                elif instruction_type == "inc":
                    self.__inc(instruction[1])
                elif instruction_type == "dec":
                    self.__dec(instruction[1])
                elif instruction_type == "tgl":
                    self.__tgl(instruction[1])
                elif instruction_type == "out":
                    self.__out(instruction[1])
                    if len(self.sequence) == 10:
                        break
                elif instruction_type == "jnz":
                    self.__jnz(instruction[1], instruction[2])
                    continue

            self.instruction_pointer += 1


def find_lowest_positive_integer_for_register_a(data) -> int:
    program = data.splitlines()
    for i in count(1, 1):
        computer = Computer({"a": i, "b": 0, "c": 0, "d": 0}, program, 0)
        computer.execute_program()
        if computer.sequence == "0101010101":
            return i


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(find_lowest_positive_integer_for_register_a(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
