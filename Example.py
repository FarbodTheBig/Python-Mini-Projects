def get_concatenation(nums):
    result = 0
    while len(nums) > 0:
        if len(nums) > 1:
            result += int(str(nums[0]) + str(nums[-1]))
            nums.pop(0)
            nums.pop(-1)
        else:
            result += nums[0]
            nums.pop(0)
    return result

# prompt the user for input
nums = input("Enter a list of integers: ").split()
nums = [int(num) for num in nums]

# call the function and print the result
concatenation = get_concatenation(nums)
print("The concatenation value of the list is:", concatenation)
