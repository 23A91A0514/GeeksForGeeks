def firstDigit(n):
    while n >= 10:
        n //= 10
    return n
