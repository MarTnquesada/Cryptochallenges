import os
from operator import itemgetter
import base64
##get the Hamming distance between the following strings (its 37):

key = ["I","O","R","I","O"]
print(b'I')
print(str(b'I', "utf-8"))
I = b'I'
O = b'O'
R = b'R'
with open("breaktext.txt", "r") as f:
    file_lines = f.readlines()
    fileprep = ""
    for line in file_lines:
        fileprep = "".join((fileprep, line.rstrip('\n')))
    print(fileprep)
    filebytes = bytearray(base64.decodebytes(bytearray(fileprep, 'utf-8')))
    print(filebytes)
    n = 0
    for i in range(len(filebytes)):
        if n == 0 or n == 3:
            print(str(filebytes[i] ^ I, "utf-8"))
        elif n == 1 or n == 4:
            print(str(filebytes[i] ^ O, "utf-8"))
        elif n == 2:
            print(str(filebytes[i] ^ R, "utf-8"))
        else:
            n = -1
        n += 1

