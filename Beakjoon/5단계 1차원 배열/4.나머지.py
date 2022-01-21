ln = []
for i in range(10):
    num = int(input())
    ln.append(num % 42)

ln = set(ln)
print(len(ln))

