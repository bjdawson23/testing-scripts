# Online Python - IDE, Editor, Compiler, Interpreter

pie = 3.14159
radius = 5
circumference = 2*pie*radius
area = pie*(radius**2)
remain = 26 % 2
print (pie)
print (radius)
print (circumference)
print (area)
print (remain)

if 1024 % 4 == 0:
    print("1024 is a multiple of 4")
else:
    print("1024 is not a multiple of 4")


if 10 % 2 == 0:
    print("2 is a multiple of 10")
else:
    print("2 is not a multiple of 10")

print("Number\tSquare\tCube")  # Header row
for num in range(6):  # Iterate from 0 to 5
    print(f"\t{num}\t\t\t{num**2}\t\t\t{num**3}")  # Print values with tab spacing

