'''
You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.

#Examples:

    Kata.getMiddle("test") should return "es"

    Kata.getMiddle("testing") should return "t"

    Kata.getMiddle("middle") should return "dd"

    Kata.getMiddle("A") should return "A"
'''
str = "testing";

def get_middle(str):
    # Finding string length
    length = len(str);
    middle = (length // 2) - 1 ;
    # Finding middle index of string
    if length % 2 == 0:
        res = str[middle] + str[int(middle+1)]
        print(res)
        return res
    else:
        res = str[int(middle+1)]
        print(res)
        return res

get_middle(str)
