## Simple Interest Calculator Program

# Function to calculate Simple Interest
def calculate_si(principal, rate, time):
    return (principal * rate * time) / 100


# Function to calculate total amount
def calculate_total(principal, interest):
    return principal + interest


# Main program
print("=== Simple Interest Calculator ===")

p = float(input("Enter Principal Amount: "))
r = float(input("Enter Rate of Interest (% per year): "))
t = float(input("Enter Time (in years): "))

interest = calculate_si(p, r, t)
total = calculate_total(p, interest)

print("\n--- Result ---")
print("Simple Interest:", round(interest, 2))
print("Total Amount:", round(total, 2))
