def facto(n):
    if n==1:
        return 1
    return n*facto(n-1)
A=int(input("Enter your value :"))
print(facto(A))