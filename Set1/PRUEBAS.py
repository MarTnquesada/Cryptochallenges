import os
from operator import itemgetter
##get the Hamming distance between the following strings (its 37):

lista = [("fsd", "fsdfd", 1), ("fasdfsd", "fsdffsdd", 2), ("fasdfsdfdfd", "fsdaaffsdd", 3)]

print(min(lista, key=lambda x:x[2]))


