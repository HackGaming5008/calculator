# this code is written by chanveersingh follow on github for more

wl ="Welcome to calculator, calculate the value you want."
opp = ("1.Addition\n"
       "2.Subraction\n"
       "3.Division\n"
       "4.Multiplication\n"
       "5.Float division\n"
       "6.EXIT")

y = "Your result is:"
print(wl)
print(opp)

option = int(input("Enter your option from above:"))
number1 = float(input("Enter your first number:"))
number2 = float(input("Enter your second number:"))

# if else will give result with opratores of python

if option == 1:
    print(y,number1 + number2)
elif option == 2:
    print(y,number1 - number2)
elif option == 3:
    print(y,number2 / number1)
elif option == 4:
    print(y,number1*number2)
elif option == 5:
    print(y,number1//number2)
elif option == 6:
    print("Bye bye have a nice day.")
else:
    print("Your value is invailed.")

