import sys

def get_all_lines(filename):
    with open(filename) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines

def count_occurrences(lines):
    counts = dict()
    for line in lines:
        if (not line in counts):
            counts[line] = 1
        else:
            counts[line] += 1
    return counts

def print_out(counts):
    for val in counts.items():
        if (val[1] > 1):
            print(val)


def main():
    # put filepath as parameter of get_all_lines()
    print_out(count_occurrences(get_all_lines()))

if __name__ == "__main__":
    main()