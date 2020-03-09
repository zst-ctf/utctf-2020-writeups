#!/usr/bin/env python3
import string
import numpy as np
import sympy

'''
Hill
1322
I found these characters on top of a hill covered with algae ... bruh I can't figure it out can you help me?

wznqca{d4uqop0fk_q1nwofDbzg_eu}

by bnuno
'''

# Using 2x2 hill cipher known plaintext attack
# http://practicalcryptography.com/ciphers/hill-cipher/


ct = 'wznqca{d4uqop0fk_q1nwofDbzg_eu}'.replace('{', '').replace('}', '').replace('_', '')
pt = 'utflag'

ct = 'wznqca'
pt = 'utflag'

ct = 'canq'
pt = 'agfl'

#ct = 'gzscxnvcdjzxeovcrclsrc'
#pt = 'thegoldisburiedinorono'
print(ct)

ct_int = list(map(string.ascii_lowercase.index, ct))
print('ct_int', ct_int)
pt_int = list(map(string.ascii_lowercase.index, pt))
print('pt_int', pt_int)

ct_matrix = np.matrix(ct_int[:4]).reshape((2,2))
print('ct_matrix', ct_matrix)
pt_matrix = np.matrix(pt_int[:4]).reshape((2,2))
print('pt_matrix', pt_matrix)

inv_pt_matrix = sympy.Matrix(ct_matrix).inv_mod(26)
print('inv_pt_matrix', inv_pt_matrix)

# https://stackoverflow.com/questions/58630591/matrix-modular-inverse-in-python
k = np.dot(ct_matrix, inv_pt_matrix)
print('key', k)


cc = np.dot(pt_matrix, k)
cc = np.mod(cc, 26)
print('cc', cc)


'''
KP = C mod 26
C*invP = K
'''
# string.ascii_lowercase

# https://hackr.io/blog/numpy-matrix-multiplication
