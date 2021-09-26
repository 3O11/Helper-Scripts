import random
import math
from scipy.stats import norm

def get_random_permutation():
    return random.sample([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10)

def get_equal_parity_count(permutation: list):
    count = 0
    for i in range(len(permutation)):
        if (i+1) % 2 == permutation[i] % 2:
            count += 1
    return count

def calculate_expected_val():
    iterations = 50000
    total_equal_parity_count = 0
    for _ in range(iterations):
        total_equal_parity_count += get_equal_parity_count(get_random_permutation())
    
    expected_val = total_equal_parity_count / iterations
    print(total_equal_parity_count, '  ', iterations)
    print("Expected value of numbers with the same parity: {}".format(expected_val))


if(__name__ == "__main__"):
    # calculate_expected_val()
    print(norm.ppf(0.9978, loc=180, scale=7))