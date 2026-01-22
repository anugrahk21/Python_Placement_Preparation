# Patterns

n = int(input("Enter number of rows: "))

# Pattern 1: Right-Angled Triangle of Stars
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print("")

# Pattern 2: Right-Angled Triangle of Row-wise Incremental Numbers
for i in range(n+1):
    for j in range(i):
        print(j+1, end=" ")
    print("")

# Pattern 3: Right-Angled Triangle of Same Number in Each Row
for i in range(n+1):
    for j in range(i):
        print(i, end=" ")
    print("")

# Pattern 4: Floyd's Triangle (Incremental Numbers)
k=1
for i in range(n+1):
    for j in range(i):
        print(k, end=" ")
        k+=1
    print("")

# Pattern 5: Inverted Right-Angled Triangle of Stars
for i in range(n,0,-1):
    for j in range(i):
        print("*", end=" ")
    print("")

# Pattern 6: Inverted Right-Angled Triangle of Stars (One-liner approach)
for i in range(n,0,-1):print("* " * i)

# Pattern 7: Proper Pyramid (Equilateral Triangle) of Stars
for i in range(n):
    for j in range(n-i-1): # n-i-1 spaces because 
        print(" ", end=" ")
    for k in range(2*i+1):
        print("*", end=" ")
    print("")

# Pattern 8: Diamond Shape of Stars ( Same as patter 7 but with 2 triangle logic)
for i in range(n):
    for j in range(n-i-1,0,-1):
        print(" ", end=" ")
    for j in range(i+1):
        print("*", end=" ")
    for j in range(i):
        print("*", end=" ")
    print("")