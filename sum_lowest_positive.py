number1 = int(input('Give the first number: '))
number2 = int(input('Give the second number: '))
number3 = int(input('Give the third number: '))
number4 = int(input('Give the fourth number: '))

array_of_numbers  = [number1, number2, number3, number4]

def sum_two_smallest_numbers(array_of_numbers):

    array_of_numbers.sort()

    first_number = array_of_numbers[0]
    second_number = array_of_numbers[1]

    sum_of_lowest = array_of_numbers[0] + array_of_numbers[1]

    print(f'The sum of {first_number} and {second_number} is {sum_of_lowest}')


sum_two_smallest_numbers(array_of_numbers)