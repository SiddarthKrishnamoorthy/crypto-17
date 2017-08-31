import struct


def bytes_from_file(filename):
    with open(filename, "rb") as f:
        while True:
            byte = f.read(1)
            if not byte:
                break
            yield(ord(byte))


n = 0
c = 0
tot = 74448
listofbytes = []
shit = ['0'] * tot
for b in bytes_from_file('export.png'):
    listofbytes.append(b)
print len(listofbytes)
outFile = open("out", "wb")
while (c < tot):
    byte = (listofbytes[c] - n) % 256
    shit[c] = byte
    c += 2
    n -= 2
c = 1
n = 0
while (c < tot):
    byte = (n - listofbytes[c]) % 256
    if (byte < 0):
        byte += 256
    shit[c] = byte
    c += 2
    n += 2
for a in shit:
    outFile.write(chr(a))
print("done")
outFile.close()
