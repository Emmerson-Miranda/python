# https://docs.python.org/3/reference/datamodel.html#object.__call__
# https://www.w3schools.com/python/ref_keyword_pass.asp
# https://www.geeksforgeeks.org/__call__-in-python/
from enum import Enum


line = "-" * 80

print(line, "| 01 Simple Decorator", line, sep="\n")


class MeasureWithoutArgs:
    def __init__(self, fn):
        self.fn = fn

    def __call__(self):
        print("Before:", self.fn.__name__)
        self.fn()
        print("After:", self.fn.__name__)


@MeasureWithoutArgs
def process_document():
    print("hello world ")


process_document()


print(line, "| 02 Decorator with arguments (true)", line, sep="\n")


class MeasureWithArgs:
    def __init__(self, active):
        self.active = active

    def __call__(self, fn):
        def __fn():
            if self.active:
                print("Before:", fn.__name__)
            fn()
            if self.active:
                print("After:", fn.__name__)

        return __fn


@MeasureWithArgs(active=True)
def process_document_arguments():
    print("hello world active argument")


process_document_arguments()

print(line, "| 03 Decorator with arguments (false)", line, sep="\n")


@MeasureWithArgs(active=False)
def process_document_arguments2():
    print("hello world with inactive argument")


process_document_arguments2()


print(line, "| 04 Strategy - callable without arguments", line, sep="\n")


class OutputFormat(Enum):
    JSON = 0
    XML = 1
    TEXT_PLAIN = 3


class PrintMessage:
    def __init__(self, convert_type, message):
        self.convert_type = convert_type
        self.message = message

    def __call__(self):
        if self.convert_type == OutputFormat.JSON:
            return '{"message":"' + self.message + '"}'
        elif self.convert_type == OutputFormat.XML:
            return '<message>' + self.message + '</message>'
        elif self.convert_type == OutputFormat.TEXT_PLAIN:
            return self.message


msg = PrintMessage(OutputFormat.TEXT_PLAIN, "Hello World")
print("Plain text:", msg())
msg = PrintMessage(OutputFormat.JSON, "Hello World")
print("JSON      :", msg())
msg = PrintMessage(OutputFormat.XML, "Hello World")
print("XML       :", msg())


print(line, "| 05 Strategy - callable with arguments", line, sep="\n")

class PrintMessageV2:
    def __init__(self, message):
        self.message = message

    def __call__(self, convert_type):
        if convert_type == OutputFormat.JSON:
            return '{"message":"' + self.message + '"}'
        elif convert_type == OutputFormat.XML:
            return '<message>' + self.message + '</message>'
        elif convert_type == OutputFormat.TEXT_PLAIN:
            return self.message


msg = PrintMessageV2("Hello World")
print("XML        :", msg(OutputFormat.XML))
print("JSON       :", msg(OutputFormat.JSON))
print("TEXT PLAIN :", msg(OutputFormat.TEXT_PLAIN))
