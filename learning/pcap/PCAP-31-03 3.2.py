"""
PCAP-31-03 3.2 – Operate on strings

    functions: ord(), chr()
    indexing, slicing, immutability
    iterating through strings, concatenating, multiplying, comparing (against strings and numbers)
    operators: in, not in

"""


# functions: ord(), chr()
character = 'A'
ordinal = ord(character)
print('Character:', character, ' - ord:', ordinal, ' - chr:', chr(ordinal))

# slicing
"""
https://www.w3schools.com/python/python_strings.asp
Strings
Are arrays of bytes representing unicode characters. 
Python does not have a character data type, a single character is simply a string with a length of 1.
Square brackets can be used to access elements of the string.

Indexing
https://realpython.com/lessons/string-indexing/
https://codehs.com/textbook/intropython_textbook/5.1
Indexing allows you to access individual characters in a string directly by using a numeric value. String indexing is zero-based
Negative Indexing - start the slice from the end of the string

Slicing
https://codehs.com/textbook/intropython_textbook/5.2
You can return a range of characters by using the slice syntax.
Specify the start index and the end index, separated by a colon, to return a part of the string.

Immutability
https://codehs.com/textbook/intropython_textbook/5.3
immutability which means they cannot be mutated or changed. You can assign strings to variables, 
and reassign new strings to the same variable, but individual characters within a string cannot be reassigned.

Comparing
https://www.digitalocean.com/community/tutorials/python-string-comparison
Python string comparison compares the characters in both strings one by one. 
When different characters are found, then their Unicode code point values are compared. 
The character with the lower Unicode value is considered to be smaller.

"""
text = '0123456789'

print('text       original string  :', text)
print('text[0::]  original string  :', text[0::])
print('text[::]   original string  :', text[::])
print('text[::-1] revert string    :', text[::-1])
print('text[1]    first character  :', text[1])    # String Indexing
print('text[4]    fourth character :', text[4])    # String Indexing
print('text[-4]   fourth character :', text[-4])   # String Negative Indexing
print('text[2:5]  2,3,4 character  :', text[2:5])
print('text[4:]   from 4 character :', text[4:])    # Slice To the End
print('text[4::]  from 4 character :', text[4::])
print('text[:4]   from 4 character :', text[:4])    # Slice From the Start (4 non included)
print('text[::4]  from 4 character :', text[::4])
print('text[-6:-2] 4567 character  :', text[-6:-2])  # Negative Indexing

# iterating
abc = 'abcdef'
print('Iterating over a string')
for c in abc:
    print(c, end=' ')
print('')

print('Iterating over a string using enumerate')
for i, c in enumerate(abc):
    print(i, c, end=' ')
print('')

# operators: in, not in
print("'cde' in abc     :", 'cde' in abc)
print("'abcdef' in abc  :", 'abcdef' in abc)
print("'abcdefg' in abc :", 'abcdefg' in abc)
print("'ced' in abc     :", 'ced' in abc)
print("'ced' not in abc :", 'ced' not in abc)

# concatenating
str1 = 'Hello'
str2 = 'world'
str3 = str1 + str2
str4 = "{}-{}".format(str1, str2)
str5 = f"{str1}_{str2}"

print('concatenating', '"{}-{}".format(str1, str2) : ', str4)
print('concatenating', 'f"{str1}_{str2}"    : ', str5)
print('concatenating', 'str1 + str2         : ', str3)
print('concatenating', '\'.\'.join(str2)      : ', '.'.join(str2))
print('concatenating', '\'.\'.join(str1,str2) : ', '.'.join([str1, str2]))


# multiplying
txt = 'A' * 10
txt2 = 'Abc' * 5
txt3 = 3 * ('hello', 'world')
txt4 = 3 * ['hello', 'world']
print('multiplying', "'A' * 10              :", txt)
print('multiplying', "'Abc' * 5             :", txt2)
print('multiplying', "3 * ('hello', 'world'):", txt3)
print('multiplying', "3 * ['hello', 'world']:", txt4)


# comparing
fruit1 = 'Apple'

print('comparing ', f"{fruit1} == 'Apple' :", fruit1 == 'Apple')
print('comparing ', f"{fruit1} != 'Apple' :", fruit1 != 'Apple')
print('comparing ', f"{fruit1} < 'Apple'  :", fruit1 < 'Apple')
print('comparing ', f"{fruit1} > 'Apple'  :", fruit1 > 'Apple')
print('comparing ', f"{fruit1} <= 'Apple' :", fruit1 <= 'Apple')
print('comparing ', f"{fruit1} >= 'Apple' :", fruit1 >= 'Apple')

print('comparing ', f"{fruit1} == 'Ananas' :", fruit1 == 'Ananas')
print('comparing ', f"{fruit1} != 'Ananas' :", fruit1 != 'Ananas')
print('comparing ', f"{fruit1} < 'Ananas'  :", fruit1 < 'Ananas')
print('comparing ', f"{fruit1} > 'Ananas'  :", fruit1 > 'Ananas')
print('comparing ', f"{fruit1} <= 'Ananas' :", fruit1 <= 'Ananas')
print('comparing ', f"{fruit1} >= 'Ananas' :", fruit1 >= 'Ananas')

print('comparing ', f"{fruit1} == 'Banana' :", fruit1 == 'Banana')
print('comparing ', f"{fruit1} != 'Banana' :", fruit1 != 'Banana')
print('comparing ', f"{fruit1} < 'Banana'  :", fruit1 < 'Banana')
print('comparing ', f"{fruit1} > 'Banana'  :", fruit1 > 'Banana')
print('comparing ', f"{fruit1} <= 'Banana' :", fruit1 <= 'Banana')
print('comparing ', f"{fruit1} >= 'Banana' :", fruit1 >= 'Banana')
