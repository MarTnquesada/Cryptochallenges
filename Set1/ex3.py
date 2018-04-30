
from operator import itemgetter
#Single-byte XOR cipher
'''Letter frequency taken from: 
https://www.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html
https://www.tandfonline.com/doi/pdf/10.1080/00437956.1950.11659381
In this last case, I have used a middle ground (Vowels = 37.8% and Consonants = 62.2%)
'''

HEX_STRING = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
VOWELS_UC = [65, 69, 73, 79, 85]
VOWELS_LC = [97, 101, 105, 111, 117]
CONSONANTS_UC = set(range(65, 91)) - set(VOWELS_UC)
CONSONANTS_LC = set(range(97, 123)) - set(VOWELS_LC)
BLANK_SPACE = 32
PUNCTUATION_MARKS = range(33,65) #from 33 to 65 - 1 (64)

VOWELS_FREQ = 0.378
CONSONANTS_FREQ = 0.622

#generator: receives byte object or bytearray and deciphers it for utf-8
def singlebyte_xor(inputbytes):
    inputbytes = bytearray(inputbytes) #wrap it around bytearray
    hist = []
    for i in range(0, 127): #XOR through all utf-8 values
        resultbytes = bytearray(len(inputbytes))
        vowels = 0
        consonants = 0
        marks = 0
        words = 1
        for j in range(len(inputbytes)):
            resultbytes[j] = inputbytes[j] ^ i
            #to avoid utf characters of 16 bytes
            if resultbytes[j] > 127:  
                break
            elif resultbytes[j] == BLANK_SPACE: 
                words += 1
            elif VOWELS_UC.__contains__(resultbytes[j]) or VOWELS_LC.__contains__(resultbytes[j]): 
                vowels += 1
            elif CONSONANTS_UC.__contains__(resultbytes[j]) or CONSONANTS_LC.__contains__(resultbytes[j]):
                consonants += 1
            else: 
                marks += 1
            if(marks > words + 2):  
                break
        else:
            let = vowels/words + consonants/words
            v_freq = vowels/let
            c_freq = consonants/let
            rank = abs(VOWELS_FREQ - v_freq) + abs(CONSONANTS_FREQ - c_freq)
            hist.append((resultbytes, i, rank)) #where i is the key and the last element is the punctuation
    ##I could use min(hist, key=lambda x:x[2]), but itemgetter is faster, at least in this case
    if len(hist) != 0: 
        return min(hist, key=itemgetter(2)) #Returns the triplet with the best histogram
    else: return None

if __name__ == '__main__':
    result =  singlebyte_xor(bytearray.fromhex(HEX_STRING))
    print(str(result[0], "utf-8"))