def square_digits(num):
    # Solution 1
    n =  [int(i) for i in str(num)]
    result = [i*i for i in list(map(int, n))]
    strings = [str(integer) for integer in result]
    a_string = "".join(strings)
    an_integer = int(a_string)
    return an_integer

    # # Solution 2
    # ret = ""
    # for x in str(num):
    #     ret += str(int(x)**2)
    # return int(ret)
square_digits(9119)