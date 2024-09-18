I1=int(12)      # Assign an integer to a variable.
S1="Hello"      # Assign a string to a variable.
F1=float(12.34) # Assign a float to a variable.

# Use the print() function to print out the variable you assigned.
print("integer: "+ str(I1)+ ", string: "+S1+", float: "+str(F1))

# Operators
Calc = I1 + F1     # =, +
Result = 4 * 5 / 12 # *, /
Remainder = 12 % 5    # %

print()
print("logical operators & conditional statement")
if 10>5 and 3<15 and S1!="mello":   # if, and, not
    print("and statement is true, or statement not tested")
elif 2==Remainder or 4>5:           # elif, or
    print("and statement is false, or statement is true")
else:                               # else
    print("and statement is false, or statement is false")
    
print()
print("While loop is starting")       
Counter=int(0)
while Counter<=I1:
    print("counter is "+ str(Counter))
    Counter+=1
    
print()
print("For loop is starting")   
for x in range(6):
  print(x)

print()
print("List in for loop")
Colors = ['red', 'blue', 'green', 'magenta', 'black']
for Color in Colors:
    print(Color)
    
print()
print("Tuple in for loop")
Numbers = (1, 5, 7, 9, 4)
for x in Numbers:
    print(x)

# Define a function that returns a string variable.
def ColorYouLike():
    print("Guessing the color you like!")
    ColorsToChoose = ['red', 'blue', 'green', 'magenta', 'black']
    YourChoice=input("Choose a number between 0-4 : ")
    intYourChoice=int(YourChoice)
    if intYourChoice>4:
        intYourChoice=4
    elif intYourChoice<0:
        intYourChoice=0
    return ColorsToChoose[intYourChoice]

# Call the function you defined above and print the result to the shell.
print()
print("The color you like is "+ColorYouLike())

