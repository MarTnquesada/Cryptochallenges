
#Fixed XOR
HEX_STRING = "1c0111001f010100061a024b53535009181c"
HEX_KEYSTRING = "686974207468652062756c6c277320657965"

#receives bytes objects/bytearrays and XOR them returning a bytearray
def xor_buffers(input_bytes, input_keybytes): 
    resultbytes = bytearray(input_bytes)
    keybytes = bytearray(input_keybytes)
    for i, b in enumerate(keybytes):
        resultbytes[i] ^= b

    return resultbytes

if __name__ == '__main__':
    inputbytes = bytearray.fromhex(HEX_STRING)
    keybytes = bytearray.fromhex(HEX_KEYSTRING)
    resultbytes = xor_buffers(inputbytes, keybytes)
    print(resultbytes)
    string_result = "".join("%02x" % b for b in resultbytes) #decode to hex
    print(string_result)

