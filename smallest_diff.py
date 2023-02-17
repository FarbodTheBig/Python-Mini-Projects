def min_difference(numbers):
    # sort the numbers in ascending order
    sorted_numbers = sorted(numbers)
    # find the minimum difference between adjacent numbers
    min_diff = sorted_numbers[1] - sorted_numbers[0]
    for i in range(1, len(sorted_numbers) - 1):
        diff = sorted_numbers[i + 1] - sorted_numbers[i]
        if diff < min_diff:
            min_diff = diff
    return min_diff

# get input from user
user_input = input("Enter a list of numbers separated by spaces: ")
numbers = [int(num) for num in user_input.split()]

# compute and print result
result = min_difference(numbers)
print("The minimum difference between the two smallest numbers is:", result)
