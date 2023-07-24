# Write your solution here
students = int(input("How many students on the course?"))
group_size = int(input("Desired group size?"))
# Add biggest number that is not a new group
print(f"Number of groups formed: {(students + group_size - 1) // group_size}")
