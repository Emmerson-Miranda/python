# START LAB DEFINITION
# Explore loops.
# Practice while with break and continue
# END LAB DEFINITION
line = "-" * 80

max = 4
exit_value = "Y"
input_value = ""

# while case sensitive
print(line, "| 01 while case sensitive", line, sep="\n")
while input_value != exit_value:
    input_value = input("pulse Y si desea salir (sensitive): ")
else:
    print("Bye!")

# while case insensitive
print(line, "| 02 while case insensitive", line, sep="\n")
input_value = ""
while input_value.upper() != exit_value:
    input_value = input("pulse Y si desea salir(insensitive) : ")


# while and break
print(line, "| 03 while and break", line, sep="\n")
input_value = ""
while input_value != exit_value:
    input_value = input("pulse Y si desea salir o A para abortar(break) :").upper()
    if(input_value == "A") :
        print("Aborting insensitive loop")
        break
    print("You introduced: ", input_value)

# while and continue
print(line, "| 04 while and continue", line, sep="\n")
input_value = ""
index = 0
while input_value != exit_value:
    index += 1
    input_value = input("pulse Y si desea salir (continue) :").upper()
    if(index % 2) :
        continue
    print("lap ", index, "introduced value:", input_value)
else:
    print("Total laps ", index)

#end

print(line)