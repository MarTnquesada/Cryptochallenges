import base64

#Convert hex to base64
HEX_STRING = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

#receives byte objects/bytearrays and returns bytes in base64
def hex_to_base64(inputbytes):
    b64_bytes = bytearray(base64.b64encode(inputbytes))
    return b64_bytes

if __name__ == '__main__':
    inputbytes = bytearray.fromhex(HEX_STRING)
    print(inputbytes)
    print(str(hex_to_base64(inputbytes), "utf-8"))