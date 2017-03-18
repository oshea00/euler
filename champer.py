

digits = ''

for i in xrange(1, 250000):
    digits += str(i)

print int(digits[0]) * int(digits[9]) * int(digits[99]) * \
      int(digits[999]) * int(digits[9999]) * int(digits[99999]) * int(digits[999999])
