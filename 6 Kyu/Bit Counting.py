'''
Write a function that takes an integer as input, and returns the number of bits
that are equal to one in the binary representation of that number.
You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010,
so the function should return 5 in this case
'''

def binary_array_to_number(arr):
    # Solution 1
    listToStr = f'{arr:08b}'
    counter = 0
    for i in listToStr:
        if i == str(1):
            counter += 1
    return counter

    # Solution 2
    total = 0
    while n > 0:
        total += n % 2
        n >>= 1
    return total
binary_array_to_number(15)