def reverse(n):
    rev = 0
    is_negative = n < 0  # Check if the number is negative before modifying it
    n = abs(n)           # Convert to positive for reversal

    while n != 0:
        rem = n % 10
        rev = rev * 10 + rem
        n = n // 10

    if is_negative:
        rev = -rev  # Reapply the negative sign

    return rev

n = int(input("Enter a number: "))
print(reverse(n))
