# Printing the input-name only by one with the help of re(Regular expressions).

import re

fn = input("Enter your first name: ").capitalize().strip()
if re.fullmatch(r"\w+", fn):
    pass
else:
    print("Invalid input! Your first name should only contain alphabetic characters.")

ln = input("Enter your last name: ").capitalize().strip()
if re.fullmatch(r"\w+", ln):
    pass
else:
    print("Invalid input! Your last name should only contain alphabetic characters.")
print(f"Hello, {fn} {ln}. You just delved into python.")
