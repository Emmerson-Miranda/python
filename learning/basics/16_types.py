# https://realpython.com/python-data-types/#type-conversion
# we can import modules in different locations using sys
from learning.modules.utilities import print_header
# import sys
# sys.path.insert(0, '../modules')
# from utilities import print_header


int_int_value = 100
int_str_value = "123"
float_float_value = 22.5
float_str_value = "34.0"
string_value = "This is a value"

print_header("01 type")
print(type(int_int_value), "value", int_int_value)
print(type(float_float_value), "value", float_float_value)
print(type(string_value), "value", string_value)

print_header("02 conversions int float str")
print("string", int_str_value, "int value", int(int_str_value))
print("string", float_str_value, "float value", float(float_str_value))
print("int", int_int_value, "string value", str(int_int_value))
print("float", float_float_value, "string value", str(float_float_value))

print_header("03 chr ascii bin ord")
character = string_value[3:4]
character_a = ascii(character)
ordinal = ord(character)
print(character, "is ascii", character.isascii())
print("character:", character_a, " - ordinal value:", ordinal)
print("ordinal:", ordinal, " - character value is:", chr(ordinal))
print("Binary value of", ordinal, "is", bin(ordinal))

print_header("04 eval")


def boolean_conversion(string):
    try:
        return eval(string)
    except Exception as myexception:
        return myexception


print("true string value:", boolean_conversion("true"))
print("True string value:", boolean_conversion("True"))
print("TRUE string value:", boolean_conversion("TRUE"))

print("false string value", boolean_conversion("false"))
print("False string value", boolean_conversion("False"))
print("FALSE string value", boolean_conversion("FALSE"))
