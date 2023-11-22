'''
Write a Python function to check whether a number is
in a given range
'''

def check_in_range(number, start, end):
    return start <= number <= end

# Example usage:
num_to_check = 13
start_range = 6
end_range = 13
is_in_range = check_in_range(num_to_check, start_range, end_range)
print(f"Is{num_to_check}in the range[{start_range},{end_range}]?{is_in_range}")
