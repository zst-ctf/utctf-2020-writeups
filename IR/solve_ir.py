#!/usr/bin/env python3

'''
IR
1825
We found this snippet of code on our employee's laptop.
It looks really scary. Can you figure out what it does?

Written by hk
'''

btext = bytes.fromhex('03121A170AECF2140E05031D190E020A1F070C0117060C0A19130A161C1808071A031D1C110BF387000000000000000000000000000000000000000000000005')
btext = list(btext)

for i in reversed(range(len(btext) - 1)):
    btext[i] = btext[i] ^ btext[i+1];

for i in range(len(btext)):
    btext[i] = (btext[i] - 5) & 0xFF;

text = ''.join(map(lambda c: chr(c), btext))
print('text:', text)
print('btext:', btext)
print('len:', len(btext))
