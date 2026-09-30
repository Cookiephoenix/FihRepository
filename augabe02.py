a = 1
b = 1
index =  2

# Solange die Anzahl der Stellen von b kleiner als 100 ist, rechnen wir weiter
while len(str(b)) < 100:
    a, b = b, a + b
    index += 1

print("Index der Fibonacci-Zahl:", index)
