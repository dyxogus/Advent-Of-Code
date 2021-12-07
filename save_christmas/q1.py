def q1_sample():
    return [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


def parse_input():
    with open('../inputs/input_01.txt') as input_file:
        raw_input = input_file.readlines()  # brings everything into memory
        return [int(line.rstrip()) for line in raw_input]


def count_increased(list_):
    differences = [one_after - before for before, one_after in zip(list_, list_[1:])]
    return len(list(filter(lambda difference: difference > 0, differences)))


def q1_p1():
    original_input = parse_input()
    return count_increased(original_input)


def q1_p2():
    original_input = parse_input()
    window_size = 3
    sliding_window = [sum(original_input[i:i + window_size])
                      for i in range(len(original_input) - (window_size - 1))]
    return count_increased(sliding_window)
