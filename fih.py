def is_prime(number):
	if number < 2:
		return False
	for divisor in range(2, int(number ** 0.5) + 1):
		if number % divisor == 0:
			return False
	return True


prime_count = 0
candidate = 1

while prime_count < 1000:
	candidate += 1
	if is_prime(candidate):
		prime_count += 1

print(candidate)
