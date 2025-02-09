# First Program

print("Happy New Year....")

try:
    name = input("Please Enter Your Name : ")
    age = int(input("Please Enter Your Age : "))
    print(f"Hello {name} and have a nice year ahead!.")
except ValueError:
    print("PLEASE ENTER VALID NAME AND AGE!")