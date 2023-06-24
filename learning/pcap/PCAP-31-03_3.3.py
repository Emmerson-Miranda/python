"""
PCAP-31-03 3.3 – Employ built-in string methods

    methods: .isxxx(), .join(), .split(), .sort(), sorted(), .index(), .find(), .rfind()

"""

# join
str1, str2 = 'Hello', 'world'
print('concatenating', '\'.\'.join(str2)      : ', '.'.join(str2))
print('concatenating', '\'.\'.join(str1,str2) : ', '.'.join([str1, str2]))

# split
text = 'This is a text message'
print(f"split '{text}' ", text.split())
print(f"split '{text}' ", text.split('t'))
print(f"split '{text}' ", text.split('text'))

# index
print('index', f"'{text}'.index('s')     :", text.index('s'))
print('index', f"'{text}'.index('s', 4)  :", text.index('s', 4))

# .find()
print('find', f"'{text}'.find('is')   :", text.find('is'))
# .rfind()
print('rfind', f"'{text}'.rfind('is') :", text.rfind('is'))

# isxxx()
s1 = 'a'
s2 = '4'
s3 = ' '
print(f"'{s1}'.isalnum()  :", s1.isalnum())
print(f"'{s2}'.isalnum()  :", s2.isalnum())
print(f"'{s1}'.isdigit()  :", s1.isdigit())
print(f"'{s2}'.isdigit()  :", s2.isdigit())
print(f"'{s1}'.isnumeric():", s1.isnumeric())
print(f"'{s2}'.isnumeric():", s2.isnumeric())
print(f"'{s1}'.isascii()  :", s1.isascii())
print(f"'{s2}'.isascii()  :", s2.isascii())
print(f"'{s1}'.isspace()  :", s1.isspace())
print(f"'{s3}'.isspace()  :", s3.isspace())

# sort, reverse
fruits = ['watermelon', 'apple', 'strawberry', 'banana', 'orange']
print("sort before    :", fruits)
fruits.sort()
print("sort after     :", fruits)
fruits.reverse()
print("reverse        :", fruits)

# sorted, sort
books = [
    {'year': 1955, 'name': 'Pedro paramo'},
    {'year': 1265, 'name': 'Divina comedia'},
    {'year': 1967, 'name': 'Cien años de soledad'},
    {'year': 1952, 'name': 'El viejo y el mar'},
]

print('sorted before  :', books)
sorted_books = sorted(books, key=lambda x: x['year'])
print('sorted after   :', sorted_books)
books.sort(key=lambda x: x['name'])
print('sort after     :', books)
