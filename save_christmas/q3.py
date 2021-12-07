def parse_input(file_path='../inputs/input_03.txt'):
    with open(file_path) as input_file:
        raw_input = input_file.readlines()  # brings everything into memory
        return [line.rstrip() for line in raw_input]


def convert_bit_array_to_decimal(bit_array):
    return int(''.join(map(str, bit_array)), base=2)


def q3_p1():
    input_ = parse_input()

    each_entry_width = len(input_[0])
    all_measurements_count = len(input_)

    sums_of_bit_indices = [sum((int(measurement[bit_index]) for measurement in input_))
                           for bit_index in range(each_entry_width)]
    half = all_measurements_count // 2

    gamma_rate_array = [sum_ > half and 1 or 0 for sum_ in sums_of_bit_indices]
    epsilon_rate_array = [sum_ < half and 1 or 0 for sum_ in sums_of_bit_indices]

    gamma_rate = convert_bit_array_to_decimal(gamma_rate_array)
    epsilon_rate = convert_bit_array_to_decimal(epsilon_rate_array)

    return gamma_rate * epsilon_rate


def q3_p2():
    return -1


if __name__ == '__main__':
    print(q3_p1())
