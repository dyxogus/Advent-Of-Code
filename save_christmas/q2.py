def parse_input(file_path='../inputs/input_02.txt'):
    with open(file_path) as input_file:
        raw_input = input_file.readlines()  # brings everything into memory
        return [line.rstrip() for line in raw_input]


def q2_p1():
    original_input = parse_input()

    horizontal, depth = 0, 0
    for line in original_input:
        instruction, value = line.split(' ')
        value_int = int(value)

        if instruction == 'forward':
            horizontal += value_int
        elif instruction == 'down':
            depth += value_int
        elif instruction == 'up':
            depth -= value_int

        # print(line, (horizontal, depth))

    return horizontal * depth


def q2_p2():
    original_input = parse_input()

    horizontal, depth, aim = 0, 0, 0
    for line in original_input:
        instruction, value = line.split(' ')
        value_int = int(value)

        if instruction == 'forward':
            horizontal += value_int
            depth += (aim * value_int)
        elif instruction == 'down':
            aim += value_int
        elif instruction == 'up':
            aim -= value_int

        # print(line, (horizontal, depth))

    return horizontal * depth
