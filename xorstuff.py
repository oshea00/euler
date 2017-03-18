import zlib

def xorencrypt(txt, k):
    ptxt = bytearray(txt)
    pk = bytearray(k)
    enctxt = bytearray()
    j = 0
    for i in range(len(ptxt)):
        keycharord = pk[j % len(pk)]
        ptxtord = ptxt[i]
        enctxt.append(keycharord ^ ptxtord)
        j += 1
    return enctxt

plaintext = "now is now the time for now all good men to come to the aid of now"
key = "1234"
plaintext2 = "now some now text with a now lots of now in it"

enc = xorencrypt(plaintext, key)
enc2 = xorencrypt(enc, "now ") # look for guessed text in enc by using it as a key

pt = xorencrypt(enc, key)
pt2 = xorencrypt(enc2, key)

sr = xorencrypt(enc, enc2)
print enc
print enc2
print pt
print pt2
print sr

f = file('comp2.bin', 'rb')
data = f.read()
#data.insert(0,0x78)
#data.insert(0,0x9c)
#encd = str(data)

#compressed = zlib.compress(f.read())
#fo = file('zcomp.bin', 'wb')
#fo.write(compressed)

uncompressed = zlib.decompress(data, -15)
for b in uncompressed:
    print(b),

fo = file('rec.mp', 'wb')
fo.write(uncompressed)
