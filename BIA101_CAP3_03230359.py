# https://github.com/Tlaywang/Tlaywang
# Thinley wangmo
# BI A
# 03230359

# REFERENCES
# https://docs.python.org/3/reference/index.html
# https://stackoverflow.com/questions/64749889/how-to-extract-the-first-and-last-value-from-a-txt-file-in-python
# https://www.geeksforgeeks.org/python-extract-digits-from-given-string/
# SOLUTION
# Your Solution Score: <483707>



f = open('359.txt', 'r')

def read_input(f):
    with open(f, 'r') as file:
        lines = file.readlines()
    return lines

# Calculate the sum of two-digit numbers formed from the first and last digits in each line
def calculate_sum(lines):
    total_sum = 0  # Initialize the total sum

    # Iterate over each line
    for line in lines:
        line = line.strip()
        first_digit = None
        last_digit = None

        for i in range(len(line)):
            if line[i].isdigit():
                if first_digit is None:
                    first_digit = line[i]
                last_digit = line[i]

        # If both digits are found, combine them and add to the total sum
        if first_digit and last_digit:
            two_digit_number = int(first_digit + last_digit)
            total_sum += two_digit_number

    return total_sum


def print_solution(file_path, answer):
    print(f"The total sum from the given input file {file_path} is {answer}")

# Main execution
file_name = "359.txt"  # Replace with the actual file name if different
lines = read_input(file_name)
answer = calculate_sum(lines)
print_solution(file_name, answer)