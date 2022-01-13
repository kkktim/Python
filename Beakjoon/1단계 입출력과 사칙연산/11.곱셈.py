a, b, c = map(int, input())
d, e, f = map(int, input())

s1 = (a*100 + b*10 + c) * f
s2 = (a*100 + b*10 + c) * e
s3 = (a*100 + b*10 + c) * d

print(s1)
print(s2)
print(s3)
print(s1 + s2*10 + s3*100)
