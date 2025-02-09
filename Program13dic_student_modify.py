# Example Dictionary

student = {
    "name": "Alex Johnson",
    "roll_no": 2023,
    "subjects": ["Math", "Physics", "Biology"],
    "marks": {
        "Math": 85,
        "Physics": 78,
        "Biology": 92
    }
}

# Add a new key "grade" with a value "A"
student["grade"] = "A"

# Update the marks for "Physics" to 88
student["marks"]["Physics"] = 88

# Add a new subject "Chemistry" with marks 90
student["marks"]["Chemistry"] = 90
student["subjects"].append("Chemistry")

# Check if the key "sports" exists; if not, add it
if "sports" not in student:
    student["sports"] = ["Basketball", "Football"]

# Calculate the total marks obtained
print("\n")
total_marks = sum(student["marks"].values())
print(f"Total Marks Obtained: {total_marks}")

# Calculate the average marks obtained
average_marks = total_marks / len(student["marks"])
print(f"Average Marks Obtained: {average_marks}")

# Display the modified directory
print("\nUpdated Student Directory:")
for key, value in student.items():
    print(f"{key}: {value}")