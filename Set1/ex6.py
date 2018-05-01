
import base64
from operator import itemgetter
#Break repeating-key XOR

FILE_PATH = "breaktext.txt"
VOWELS_UC = [65, 69, 73, 79, 85]
VOWELS_LC = [97, 101, 105, 111, 117]
CONSONANTS_UC = set(range(65, 91)) - set(VOWELS_UC)
CONSONANTS_LC = set(range(97, 123)) - set(VOWELS_LC)
VOWELS_FREQ = 0.378
CONSONANTS_FREQ = 0.622

#Hamming distance between two bytearrays or byte objects
def hmg_distance(bstr1, bstr2):
    if len(bstr1) != len(bstr2) :raise ValueError("Error: sequences of different length")
    result = 0
    for b1, b2 in zip(bstr1, bstr2):
        result += sum(bit1 != bit2 for bit1, bit2 in zip(bin(b1)[2:].rjust(8, '0'), bin(b2)[2:].rjust(8, '0')))
    return result

'''The method from ex3 is fine, but for key validation it is necessary a simple version
that only focuses on the characters being valid, rather than word frequency and structure'''
def simp_singlebyte_xor(inputbytes): 
    inputbytes = bytearray(inputbytes) #wrap it around bytearray
    hist = []
    for i in range(0, 127): #XOR through all utf-8 values
        resultbytes = bytearray(len(inputbytes))
        vowels = 0
        consonants = 0
        marks = 0
        for j in range(len(inputbytes)):
            resultbytes[j] = inputbytes[j] ^ i
            #to avoid utf characters of 16 bytes
            if resultbytes[j] > 127:  
                break
            elif VOWELS_UC.__contains__(resultbytes[j]) or VOWELS_LC.__contains__(resultbytes[j]): 
                vowels += 1
            elif CONSONANTS_UC.__contains__(resultbytes[j]) or CONSONANTS_LC.__contains__(resultbytes[j]):
                consonants += 1
            else: 
                marks += 1
        else:
            let = vowels + consonants + marks
            v_freq = vowels/let
            c_freq = consonants/let
            rank = abs(VOWELS_FREQ - v_freq) + abs(CONSONANTS_FREQ - c_freq)
            hist.append((resultbytes, i, rank)) #where i is the key and the last element is the punctuation
    ##I could use min(hist, key=lambda x:x[2]), but itemgetter is faster, at least in this case
    if len(hist) != 0: 
        return min(hist, key=itemgetter(2)) #Returns the triplet with the best histogram
    else: return None

def break_it(file_path):
    ##First, it is necessary to find the KEYSIZE
    with open(file_path, "r") as f:
        file_lines = f.readlines()
        fileprep = ""
        for line in file_lines:
            fileprep = "".join((fileprep, line.rstrip('\n')))
        print(fileprep)
        filebytes = bytearray(base64.decodebytes(bytearray(fileprep, 'utf-8')))
        print(filebytes)
        selectedks = []
        for i in range(2, 45):
            hmg_norm = hmg_distance(filebytes[:i], filebytes[i:i+i]) / i
            if len(selectedks) < 3:
                selectedks.append((i, hmg_norm))
                print((i, hmg_norm))
            elif hmg_norm < max(selectedks, key=itemgetter(1))[1]:
                selectedks.remove(max(selectedks, key=itemgetter(1)))
                print((i, hmg_norm))
                selectedks.append((i, hmg_norm)) 
        #now that we probably have solved the KEYSIZE
        print(selectedks)
        for (keysize, hmg_norm) in selectedks: #KEYSIZE is in byte number
            key = []
            for bnum in range(keysize):
                block = filebytes[bnum:len(filebytes):keysize]
                if simp_singlebyte_xor(block) != None:
                    #print(simp_singlebyte_xor(block)[0])
                    key.append(simp_singlebyte_xor(block)[1]) #suppose that from here we get a key
            if len(key) != 0: yield key
            
        

if __name__ == '__main__':
    for key in break_it(FILE_PATH):
        print(key)
        for char in key:
            print(chr(char))





