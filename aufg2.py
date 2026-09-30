grenze = 1_000_000_000_000
n = 0
summe = 0

while summe <= grenze:
	n += 1
	summe += n

print(f"n = {n}")
print(f"Letzte 2 Ziffern der Summe: {summe % 100:02d}")
