def recurison(n):
    if n == 1:
        return 1
    else:
        return n * recurison(n-1)

print(recurison(int(input"Enter a number")))