# Calculate the area of rectangle using a def python function.

def area_of_rectangle(length, width):
    area = length*width
    return area

try:
    length = float(input("Enter Length: "))
    width = float(input("Enter Width: "))

    area = area_of_rectangle(length, width)
    print(f"Area of the rectangle is {area}")

except ValueError:
    print("PLEASE ENTER THE VALUES CORRECTLY")
