a = float(input())
b = float(input())
c = float(input())

if a == b == c:
    print("equilatero")
elif a == b or a == c or b == c:
    print("isosceles")
else:
    print("escaleno")
