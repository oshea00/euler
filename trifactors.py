from euler import trianglenums, divisors

for t in trianglenums():
    divs = divisors(t)
    if len(divs) > 500:
        print('{} has {} divisors'.format(t, len(divs)))
        print(divs)
        break






