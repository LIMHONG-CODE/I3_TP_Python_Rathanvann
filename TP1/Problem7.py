def digit_sum(n):
    n = abs(n)
    total = 0
    while n > 0 :
        total += n % 10
        n //= 10
    return total 

def reverse_number(n):
    """Reverse a non-negative integer without converting to str."""
    n = abs(n)
    reversed_value = 0
    while n > 0:
        reversed_value = reversed_value * 10 + n % 10
        n //= 10
    return reversed_value

def is_palindrome(n):
    if n < 0 :
        return False
    return n == reverse_number(n)

for number in (2026, 12321, 9875):
    print(
        f"{number}: is digit sum = {digit_sum(number)}, "
        f"Revers = {reverse_number(number)}, "
        f"Palindrome = {is_palindrome(number)}"
    )

palindrome_count = sum(1 for num in range(10, 1000) if is_palindrome(num))
print(f"Palindrome form 10 to 999 is : {palindrome_count}")