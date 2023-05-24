"""
capitalize
center
"""

line = "-" * 80

print(line, "| 01 Capitalize", line, sep="\n")
print('1', "hello world".capitalize())
print('2', "HELLO WORLD".capitalize())
print('3', "hello World".capitalize())
print('4', "hello WOrld".capitalize())
print('5', "123 hello WOrld".capitalize())
print('6', " hello WOrld".capitalize())

print(line, "| 02 Center", line, sep="\n")
print('  >123456789<')
print('1 >', 'hello'.center(9), '<', sep='')
print('2 >', 'hello'.center(9,'*'), '<', sep='')
print('3 >', 'hello'.center(9,'0'), '<', sep='')

print(line, "| 03 Strip", line, sep="\n")
print('strip  >', "    hello world   ".strip(), '<', sep='')
print('lstrip >', "    hello world   ".lstrip(), '<', sep='')
print('rstrip >', "    hello world   ".rstrip(), '<', sep='')

print(line, "| 04 find/rfind - hello world", line, sep="\n")
print("Finding first o: ", "hello world".find("o"))
print("Finding last o : ", "hello world".find("o", 5))
print("Finding last o : ", "hello world".rfind("o")) #find from the right
print("Finding wo     : ", "hello world".find("wo"))
print("Finding ZZ     : ", "hello world".find("ZZ"))

print(line, "| 05 endswith- hello world!", line, sep="\n")
print("1 ", "hello world!".endswith("!"))
print("2 ", "hello world!".endswith("d!"))
print("3 ", "hello world!".endswith("D!"))

print(line, "| 06 startswith- hello world!", line, sep="\n")
print("1 ", "hello world!".startswith("h"))
print("2 ", "hello world!".startswith("hello"))
print("3 ", "hello world!".startswith("!"))
print("4 ", "hello world!".startswith("H"))

print(line, "| 07 lower - upper - swapcase - title", line, sep="\n")
print("lower    'this IS a tExT'", "this IS a tExT".lower())
print("upper    'this IS a tExT'", "this IS a tExT".upper())
print("swapcase 'this IS a tExT'", "this IS a tExT".swapcase())
print("title    'this IS a tExT'", "this IS a tExT".title())

print(line, "| 08 isalnum - isalpha - isdigit - islower - isupper - isspace", line, sep="\n")
print("isalnum greetings ", "greetings".isalnum())
print("isalnum 123456780 ", "123456780".isalnum())
print("isalnum gr33tings ", "gr33tings".isalnum())
print("")
print("isalpha greetings ", "greetings".isalpha())
print("isalpha 123456780 ", "123456780".isalpha())
print("isalpha gr33tings ", "gr33tings".isalpha())
print("")
print("isdigit greetings ", "greetings".isdigit())
print("isdigit 123456780 ", "123456780".isdigit())
print("isdigit gr33tings ", "gr33tings".isdigit())
print("")
print("islower    'tExT'", "tExT".islower())
print("islower    'TEXT'", "TEXT".islower())
print("islower    'text'", "text".islower())
print("islower    't@#t'", "t@#t".islower())
print("islower    '1234'", "1234".islower())
print("islower    '    '", "    ".islower())
print("")
print("isupper    'tExT'", "tExT".isupper())
print("isupper    'TEXT'", "TEXT".isupper())
print("isupper    'text'", "text".isupper())
print("isupper    't@#t'", "t@#t".isupper())
print("isupper    '1234'", "1234".isupper())
print("isupper    '    '", "    ".isupper())
print("")
print("isspace    'tExT'", "tExT".isspace())
print("isspace    'TEXT'", "TEXT".isspace())
print("isspace    'text'", "text".isspace())
print("isspace    't@#t'", "t@#t".isspace())
print("isspace    '1234'", "1234".isspace())
print("isspace    '    '", "    ".isspace())

print(line, "| 09 join - split", line, sep="\n")
texts = ['This', 'is', 'a', 'text', 'message']
print("join 'This is a text message' ", ''.join(texts))
print("join 'This is a text message' ", ' '.join(texts))
print("join 'This is a text message' ", '-'.join(texts))
print("")
text = 'This is a text message'
print("split 'This is a text message' ", text.split())
print("split 'This is a text message' ", text.split('t'))
print("split 'This is a text message' ", text.split('text'))

print(line, "| 10 replace", line, sep="\n")
print("replace 'This is a text message' ", text.replace(' ', '-'))
print("replace 'This is a text message' ", text.replace(' ', '_'))
print("replace 'This is a text message' ", text.replace('text', 'great'))
