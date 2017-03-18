

def sum3and5multiplesLessThan(num):
    return sum([n for n in range(num)
                if 0 < (n/3)*3 == n or 0 < (n/5)*5 == n])

print (sum3and5multiplesLessThan(1000))