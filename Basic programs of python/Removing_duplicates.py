def duplicates(numbers):
    unique_numbers = []
    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)
    return unique_numbers

# Testing the function to remove the duplicates in the list

nums = [1, 2, 3, 2, 1, 4, 5, 3, 7]

unique_nums = duplicates(nums)
print(unique_nums)
