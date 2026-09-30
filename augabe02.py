a = 1
b = 1
index =  2

while len(str(b)) < 100:
    a, b = b, a + b
    index += 1

print("Index der Fibonacci-Zahl:", index)
print("Anzahl der Stellen:", len(str(b)))
print("Die Zahl selbst:", b)