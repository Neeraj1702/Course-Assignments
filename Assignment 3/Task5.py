# calculate factorial using a func

#using loop
n=int(input("Enter the number: "))
def factorial(n):
    res=1
    for i in range(2, n + 1):
        res=res*i
    return res
print(f"Factorial of {n} is: {factorial(n)}")

# using recursion
m=int(input("Enter the number: "))
def fact_recursive(m):
    if m < 2:
        return 1
    else:
        return m * fact_recursive(m - 1)
print(f"Factorial of {m} is: {fact_recursive(m)}")