# Grading System

sub_physics = int(input("Enter Marks In Physics: "))
sub_biology = int(input("Enter Marks In Biology: "))
sub_chemistry = int(input("Enter Marks In Chemistry: "))

total = sub_physics+sub_chemistry+sub_biology
average = total/3
print (f"Total Marks Obtained : {total}")
print (f"Average : {average}")

if average>=90:
    print("Congratulation, You have received -Grade A")
elif average>=80:
    print("Congratulations, You have received -Grade B")
elif average>=70:
    print("You have received -Grade C")
else:
    print("You have received Grade D")

if sub_biology <=50:
    print("You have FAILED in Biology!")
elif sub_physics <=50:
    print("You have FAILED in Physics!")
elif sub_chemistry <=50:
    print("You have FAILED in Chemistry!")