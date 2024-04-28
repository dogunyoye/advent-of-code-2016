import os.path

DATA = os.path.join(os.path.dirname(__file__), 'day12.txt')


class Computer(object):

    def __init__(self, registers, program, instruction_pointer):
        self.registers = registers
        self.program = program
        self.instruction_pointer = instruction_pointer

    @staticmethod
    def __parse_instruction(instruction) -> tuple:
        parts = instruction.split(" ")
        ins_type = parts[0]
        if ins_type == "cpy" or ins_type == "jnz":
            return parts[0], parts[1], parts[2]
        elif ins_type == "inc" or ins_type == "dec":
            return parts[0], parts[1]
        raise Exception("Unknown instruction type: " + ins_type)

    def __cpy(self, source, reg):
        if source.isnumeric():
            self.registers[reg] = int(source)
        else:
            self.registers[reg] = self.registers[source]

    def __inc(self, reg):
        self.registers[reg] += 1

    def __dec(self, reg):
        self.registers[reg] -= 1

    def __jnz(self, val, jmp):
        if val.isnumeric():
            v = int(val)
        else:
            v = self.registers[val]

        if v < 0:
            self.instruction_pointer -= int(jmp)
        elif v > 0:
            self.instruction_pointer += int(jmp)
        else:
            self.instruction_pointer += 1

    def execute_program(self):
        while 0 <= self.instruction_pointer < len(self.program):
            instruction = self.program[self.instruction_pointer]
            instruction = self.__parse_instruction(instruction)
            instruction_type = instruction[0]

            if instruction_type == "cpy":
                self.__cpy(instruction[1], instruction[2])
            elif instruction_type == "inc":
                self.__inc(instruction[1])
            elif instruction_type == "dec":
                self.__dec(instruction[1])
            elif instruction_type == "jnz":
                self.__jnz(instruction[1], instruction[2])
                continue

            self.instruction_pointer += 1


def __run_program(registers, data) -> int:
    computer = Computer(registers, data.splitlines(), 0)
    computer.execute_program()
    return computer.registers["a"]


def find_value_in_register_a_after_executing_program(data) -> int:
    return __run_program({"a": 0, "b": 0, "c": 0, "d": 0}, data)


def find_value_in_register_a_after_executing_program_with_register_c_as_one(data) -> int:
    return __run_program({"a": 0, "b": 0, "c": 1, "d": 0}, data)


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(find_value_in_register_a_after_executing_program(data)))
        print("Part 2: " + str(find_value_in_register_a_after_executing_program_with_register_c_as_one(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
