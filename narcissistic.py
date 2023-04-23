num  = int(input('Give me a number: '))

def is_narcissistic(num):
    # convert the number to a string
    num_str = str(num)
    
    # get the length of the number
    n = len(num_str)
    
    # calculate the sum of each digit raised to the power of n
    narc_sum = sum(int(digit)**n for digit in num_str)
    
    # check if the sum is equal to the original number
    if narc_sum == num: 
        print(f'{num} is a narcissistic ')
    else: 
        print(f'{num} is not a narcissistic')



is_narcissistic(num)