def square_digits(num):
    n =  [int(i) for i in str(num)]
    result = [i*i for i in list(map(int, n))]
    strings = [str(integer) for integer in result]
    a_string = "".join(strings)
    an_integer = int(a_string)
    return an_integer

square_digits(9119)