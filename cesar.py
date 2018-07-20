#!/usr/bin/env python
#Programa para criptografar e descriptografar arquivo txt,essa e a criptografia de cesar

import sys
from string import lowercase as lc

file = open(sys.argv[1],'r').read().lower()
key = int(sys.argv[2])
mode = sys.argv[3]

result = ''

for lt in file:
    if lt in lc:
	idx = lc.find(lt)
	if mode == 'enc':
           idx = (idx + key) % 26
	elif mode == 'dec':
	   idx = (idx - key) % 26
	result += lc[idx]
    else:
	result += lt
print result,

