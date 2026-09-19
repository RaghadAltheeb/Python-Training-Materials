"""
#1
if __name__ == '__main__':
    n = int(input("Enter the number of test cases: "))
    for i in range(n):
        i+=1
        print(i,end="")
#2
if __name__ == '__main__':
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print(a+b)
    print(a-b)
    print(a*b)
#3
if __name__ == '__main__':
    n = int(input("Enter the number: "))
    for i in range(n):
        print(i**2)



#4
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print(a//b)
print(a%b)
print(divmod(a,b))
#5
if __name__ == '__main__':
    s = input("Enter a string: ")
    alphanumeric = False
    alphabetical = False
    digit = False
    lowercase = False
    uppercase = False
    for i in s:
        if i.isalnum():
            alphanumeric = True
        if i.isalpha():
            alphabetical = True
        if i.isdigit():
            digit = True
        if i.islower():
            lowercase = True
        if i.isupper():
            uppercase = True
    print(alphanumeric)
    print(alphabetical)
    print(digit)
    print(lowercase)
    print(uppercase)
#6
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
m=int(input("Enter the mod number: "))
print(pow(a,b))
print(pow(a,b,m))
"""
