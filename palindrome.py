import euler


def biggestPal():
    i = 100  # Smallest 3 digit number
    j = 100  # Largest 3 digit number
    maxp = 0

    # all products of 3 digit numbers
    while i < 1000:
        while j < 1000:
            n = i * j
            if euler.ispalindrome(n):
                maxp = max(maxp, n)
            j += 1
        i += 1
        j = 0
    return maxp

print(biggestPal())
