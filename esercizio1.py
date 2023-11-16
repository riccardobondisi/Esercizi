# 1) Given a number x (no matter if integer or float) and a positive integer n compute and get printed
# out the value of the expression x n(without using the Python operator “**” or the power(x,n)

def power(x, n):
    result = 1
    for i in range(n):
        result *= x
    return result

print(power(3,4))
