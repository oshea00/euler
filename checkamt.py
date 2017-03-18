numbers = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
           'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen',
           'eighteen', 'nineteen']
tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
places = ['', 'hundred', 'thousand']


letters = []
for i in range(1, 1001):
    name=''
    if 0 < i < 20:
        name = numbers[i]
    if 19 < i < 100:
        name = tens[int(str(i)[0])] + numbers[int(str(i)[1])]
    if 99 < i < 1000:
        name = numbers[int(str(i)[0])]+'hundred'
        if 0 < int(str(i)[1:]) < 20:
            name += 'and' + numbers[int(str(i)[1:])]
        if 19 < int(str(i)[1:]) < 100:
            name += 'and' + tens[int(str(i)[1:2])] +  numbers[int(str(i)[2:])]
    if i == 1000:
        name = 'onethousand'
    letters.append(name)

all = ''.join(letters)
print(len(all))
