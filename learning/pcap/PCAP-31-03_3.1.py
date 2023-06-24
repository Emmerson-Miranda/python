"""
PCAP-31-03 3.1 – Understand machine representation of characters

    encoding standards: ASCII, UNICODE, UTF-8, code points, escape sequences

"""

"""
Encodings
https://docs.python.org/3/howto/unicode.html
A Unicode string is a sequence of code points, which are numbers from 0 through 0x10FFFF (1,114,111 decimal).
This sequence of code points needs to be represented in memory as a set of code units, 
and code units are then mapped to 8-bit bytes. 
The rules for translating a Unicode string into a sequence of bytes are called a character encoding, or just an encoding.
UTF-8 is one of the most commonly used encodings, and Python often defaults to using it. 


Encodings and Unicode
https://docs.python.org/3/library/codecs.html#encodings-and-unicode
As with other codecs, serialising a string into a sequence of bytes is known as encoding, 
and recreating the string from the sequence of bytes is known as decoding.

Standard Encodings
https://docs.python.org/3/library/codecs.html#standard-encodings
Python comes with a number of codecs built-in, either implemented as C functions or with dictionaries as mapping tables.

"""

print('decode replace utf-8          :', b'\x80abc'.decode("utf-8", "replace"))
print('decode backslashreplace utf-8 :', b'\x80abc'.decode("utf-8", "backslashreplace"))
print('decode ignore utf-8           :', b'\x80abc'.decode("utf-8", "ignore"))
try:
    print('decode strict utf-8           :', b'\x80abc'.decode("utf-8", "strict") )
except Exception as e:
    print('decode strict utf-8           :', type(e), e)



# https://docs.python.org/3.9/library/stdtypes.html#str.encode
# https://docs.python.org/3/library/codecs.html#error-handlers

msg = 'Canta una canción del año pasado.'
msg_encoded = b'Canta una canci\xc3\xb3n del a\xc3\xb1o pasado.'

print('encode ignore utf-8     :', msg.encode("utf-8", "ignore"))
print('encode ignore ascii     :', msg.encode("ascii", "ignore"))
print('encode ignore iso8859_1 :', msg.encode("iso8859_1", "ignore"))
print('encode ignore utf-8     :', msg_encoded.decode("utf-8", "ignore"))
print('without encode          :', msg)
print('without encode          :', msg_encoded)
