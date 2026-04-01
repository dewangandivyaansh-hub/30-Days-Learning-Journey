# Marks Analyzer Program

# Step 1: Take input
marks = []

n = int(input("Enter number of subjects: "))

for i in range(n):
    m = float(input(f"\n Enter marks for subject {i+1}: "))
    marks.append(m)

# Step 2: Calculate total and average
total = sum(marks)
average = total / n

# Step 3: Find highest and lowest
highest = max(marks)
lowest = min(marks)

# Step 4: Grade calculation
if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "Fail"

# Step 5: Output results
print("\n--- Result --- \n")
print("Total Marks:", total)
print("Average Marks:", average)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Grade:", grade)
