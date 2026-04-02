## Number Analyzer Program

# Function to check even or odd
def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"


# Function to check prime
def check_prime(n):
    if n <= 1:
        return "Not Prime"
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return "Not Prime"
    return "Prime"


# Function to find factorial
def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


# Main program
num = int(input("Enter a number: "))

print("Even/Odd:", check_even_odd(num))
print("Prime/Not Prime:", check_prime(num))
print("Factorial:", factorial(num))
