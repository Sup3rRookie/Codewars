'''
In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

Example
alphabet_position("The sunset sets at twelve o' clock.")
'''

def alphabet_position(text):
    char_to_num = {"a":"1", "b":"2","c":"3","d":"4","e":"5",
    "f":"6", "g":"7","h":"8","i":"9","j":"10",
    "k":"11", "l":"12", "m":"13", "n":"14",
    "o":"15", "p":"16", "q":"17","r":"18","s":"19",
    "t":"20", "u":"21", "v":"22","w":"23","x":"24","y":"25", "z":"26"}

    ## Solution 1
    text = text.replace(' ','')
    split_word = [char_to_num[char.lower()] for char in text if char.isalpha()]
    return ' '.join(split_word)

    ## Solution 2
    new_list = []
    for char in text:
        if char.isalpha():
            new_char = char.lower()
            a = char_to_num[new_char]
            new_list.append(a)

    return ' '.join(new_list)