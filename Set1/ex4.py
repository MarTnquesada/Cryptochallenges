import os
import ex3

FILE_PATH = "file.txt"

#Detect single character XOR from a file with hexadecimal lines
def single_character_xor(file_path):
    with open(file_path, "r") as f:
        file_lines = f.readlines()
        for line in file_lines:
            line = ''.join(line.rstrip('\n'))
            byteline = bytearray.fromhex(line)
            if byteline: #this is the same as ' while byteline != b"" '
                if ex3.singlebyte_xor(byteline) != None:
                    yield ex3.singlebyte_xor(byteline)


if __name__ == '__main__':
    for b in single_character_xor(FILE_PATH):
            print(str(b[0], "utf-8"))
        
    