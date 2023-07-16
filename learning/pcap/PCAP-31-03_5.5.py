"""
PCAP-31-03 5.5 – Perform Input/Output operations

    the open() function
    the errno variable and its values
    functions: close(), .read(), .write(), .readline(), readlines()
    using bytearray as input/output buffer

"""
import os
import hashlib

# reading all content as single text
print(f'\n{"-" * 80}\nreading all content as single text\n{"-" * 80}')
with open('if.txt', 'rt') as file: # safer than f=open() and f.close()
    print(file.read())

# reading content in separate lines
print(f'\n{"-" * 80}\nread readlines\n{"-" * 80}')
with open('if.txt', 'rt') as file:
    lines = file.readlines()
    print(lines)

# reading content line by line
print(f'\n{"-" * 80}\nreading line by line\n{"-" * 80}')
with open('if.txt', 'rt') as file:
    line = file.readline()
    while line:
        print(line, end="")
        line = file.readline()

# read and write binary file in a single read and write
print(f'\n{"-" * 80}\nreading and writting binary file\n{"-" * 80}')
with open('avatar-copy.jpg', 'wb') as target:
    with open('avatar.jpg', 'rb') as file:
        target.write(file.read())


print(f'\n{"-" * 80}\nreading binary file by chunks \n{"-" * 80}')
buffer_size = 20
with open('avatar.jpg', 'rb') as file:
    chunk = file.read(buffer_size)
    if chunk:
        chunk_counter = 1
        file_hash = hashlib.sha256()
        with open('avatar-copy-2.jpg', 'wb') as target:
            while chunk:
                target.write(chunk)
                file_hash.update(chunk)
                chunk = file.read(buffer_size)
                chunk_counter += 1
        print(f'{chunk_counter} chunks of {buffer_size} bytes. Hash {file_hash.hexdigest()}')


print(f'\n{"-" * 80}\nWrite a binary file from a text\n{"-" * 80}')
quote = 'Accept the things to which fate binds you, and love the people with whom fate brings you together, ' \
        'but do so with all your heart.'
quote += '\n\nWe have two ears and one mouth so that we can listen twice as much as we speak.'
file = open("document.txt", "wb")
sentence = bytearray(quote.encode("ascii"))
file.write(sentence)
file.close()


print(f'\n{"-" * 80}\nReadinto - full\n{"-" * 80}')
buffer = bytearray(os.path.getsize('document.txt'))
with open('document.txt', 'rb') as file:
    read_bytes = file.readinto(buffer)
    print('size:', read_bytes, 'content:', buffer)


print(f'\n{"-" * 80}\nReadinto - by chunks\n{"-" * 80}')
buffer_size = 50
buffer = bytearray(50)
total_bytes = os.path.getsize('document.txt')
with open('document.txt', 'rb') as file:
    while True:
        if (file.tell() + buffer_size) > total_bytes:
            buffer = bytearray(total_bytes - file.tell())
        read_bytes = file.readinto(buffer)
        if not read_bytes:
            break
        print('position:', file.tell(), 'bytes read:', read_bytes, 'content:', buffer)
