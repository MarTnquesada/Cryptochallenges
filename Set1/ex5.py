
#Implement repeating-key XOR
KEY = "ICE"
INPUT_STRING = "Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"

#Receives key as string utf-8 along with inputbytes and applies repeated xor key
def repeating_key_xor(key, inputbytes):
    keybytes = bytearray(key, "utf-8")
    inputbytes = bytearray(inputbytes)
    j = 0
    for i in range(len(inputbytes)):
        if j == len(keybytes):
            j = 0
        inputbytes[i] = inputbytes[i] ^ keybytes[j]
        j += 1

    return inputbytes
  

if __name__ == '__main__':
    inputbytes = bytearray(INPUT_STRING, "utf-8")
    resultbytes = repeating_key_xor(KEY, inputbytes)
    string_result = "".join("%02x" % b for b in resultbytes) #decode to hex
    print(string_result)