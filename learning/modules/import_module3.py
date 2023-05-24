import import_module1 as m1
import import_module2 as m2
import submodule.import_submodule as m3
from submodule import import_submodule as ism



line = "-" * 80
print(line, "| Module " + __name__, line, sep="\n")

def greetings():
    print("Hello from", __name__)

greetings()
m1.greetings()
m2.greetings()
m3.greetings()
ism.greetings()
