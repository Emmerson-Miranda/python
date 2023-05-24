import import_module1

line = "-" * 80
print(line, "| Module " + __name__, line, sep="\n")

def greetings():
    print("Hello from", __name__)
