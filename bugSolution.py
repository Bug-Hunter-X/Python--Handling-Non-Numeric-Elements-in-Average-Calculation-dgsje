def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0 #Handle list with no numbers
    total = sum(numeric_numbers)
    average = total / len(numeric_numbers)
    return average

my_list = []
result = calculate_average(my_list)
print(f"The average is: {result}")

my_list = [1, 2, 3, 4, 5]
result = calculate_average(my_list)
print(f"The average is: {result}")

my_list = [1, 2, 'a', 4, 5]
result = calculate_average(my_list)
print(f"The average is: {result}")
