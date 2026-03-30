# Diamond Pattern Program

n = 3

# upper

for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

# lower

for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))
