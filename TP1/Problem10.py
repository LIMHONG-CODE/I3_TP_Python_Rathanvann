def is_prime(n):
    if n < 2:
        return False
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 1
    return True


primes_below_50 = [number for number in range(2, 50) if is_prime(number)]
print("Primes below 50:", end=" ")
print(*primes_below_50)
print("Number of primes below 100:", sum(1 for n in range(2, 100) if is_prime(n)))


def goldbach(n):
    """Return the first prime pair (p, q) with p + q == n, or None."""
    if n < 4 or n % 2 != 0:
        return None
    for p in range(2, n // 2 + 1):
        if is_prime(p):
            q = n - p
            if is_prime(q):
                return p, q
    return None


for even_number in range(4, 31, 2):
    pair = goldbach(even_number)
    if pair is None:
        print(f"No Goldbach pair found for {even_number}")
    else:
        print(f"{even_number}={pair[0]}+{pair[1]}")

goldbach_holds = True
for even_number in range(4, 10001, 2):
    if goldbach(even_number) is None:
        goldbach_holds = False
        break

print(
    "Goldbach holds for every even number from 4 to 10000:",
    goldbach_holds
)