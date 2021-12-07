def parse_input(file_path='../inputs/input_01.txt'):
    with open(file_path) as input_file:
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
