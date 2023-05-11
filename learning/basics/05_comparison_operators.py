# START LAB DEFINITION
# Explore comparison operators. Ask for name and age for two persons and compare the values.
# Practice equals (==)
# Practice not equals (!=)
# Practice greater than (>)
# Practice greater or equals than (>=)
# Practice less than (<)
# Practice less or equals than (<=)
# END LAB DEFINITION

name_1_str = input("Introduce first person's name: ") 
name_2_str = input("Introduce second person's name: ") 

age_1_str = input("Introduce " + name_1_str + "'s age: ")
age_2 = int(input("Introduce " + name_2_str + "'s age: "))
age_1 = int (age_1_str)

print(name_1_str, "is" , age_1, "years old.")
print(name_2_str, "is" , age_2, "years old.")

if age_1 != age_2 :
    print(name_1_str, "and", name_2_str, "have DIFFERENT age.")


if age_1 > age_2 :
    print(name_1_str, "is older than", name_2_str)
elif age_1 < age_2 :
    print(name_2_str, "is older than", name_1_str)
elif age_1 == age_2 :
    print(name_1_str, "and", name_2_str, "have SAME age.")
else :
    print(name_1_str, "and", name_2_str, "have DIFFERENT age.")