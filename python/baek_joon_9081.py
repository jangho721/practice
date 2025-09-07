import sys


# Next permutation algorithm
# Function to find the next lexicographical permutation of the given string
def next_permutatioin(string: str):
    pivot_point = -1

    # Traverse from the end to find the pivot_point
    for idx in range(len(string) - 1, 0, -1):
        if string[idx] > string[idx - 1]:
            pivot_point = idx - 1
            break

    if pivot_point == -1:
        return string

    swap_idx = -1
    min_value = None
    for idx in range(len(string) - 1, pivot_point, -1):
        if string[idx] > string[pivot_point]:
            if min_value is None or string[idx] < min_value:
                min_value = string[idx]
                swap_idx = idx

    # Swap the values at pivot_point and swap_idx
    string_list = list(string)
    string_list[pivot_point], string_list[swap_idx] = string_list[swap_idx], string_list[pivot_point]

    # Sort the suffix after pivot_point
    return ''.join(string_list[:pivot_point + 1] + sorted(string_list[pivot_point + 1:]))


# Read the number of test cases
n = int(sys.stdin.readline().strip())

# Print the next permutation for each test case
for _ in range(n):
    string = str(sys.stdin.readline().strip())
    print(next_permutatioin(string))
