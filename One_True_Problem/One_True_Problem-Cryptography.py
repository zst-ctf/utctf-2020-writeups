#!/usr/bin/env python3
'''
One True Problem

Two of my friends were arguing about which CTF category is the best,
but they encrypted it because they didn't want anyone to see.
Lucky for us, they reused the same key; can you recover it?

Here are the ciphertexts:
    213c234c2322282057730b32492e720b35732b2124553d354c22352224237f1826283d7b0651
    3b3b463829225b3632630b542623767f39674431343b353435412223243b7f162028397a103e

by balex
'''

from Crypto import Random
from Crypto.Cipher import AES
import sys
import time
import binascii
import base64

ak = bytes.fromhex('213c234c2322282057730b32492e720b35732b2124553d354c22352224237f1826283d7b0651')
bk = bytes.fromhex('3b3b463829225b3632630b542623767f39674431343b353435412223243b7f162028397a103e')

def xor_zip_bytes(bytearray1, bytearray2):
    final = b''
    for a, b in zip(bytearray1, bytearray2):
        final += bytes([a ^ b])
    return final

def and_zip_bytes(bytearray1, bytearray2):
    final = b''
    for a, b in zip(bytearray1, bytearray2):
        final += bytes([a & b])
    return final

def bruteforce_key():
    for i in range(0, len(ak)):
        # 1) I guess cryptograpy is used as one of the texts. I use it here with an offset to guess te key.
        known_pt = b'Cryptography'.rjust(i, b'\x00')

        # 2) I see that 'binary exploitation' is part of the text.
        # i = 37 | text = b'\x1a\x07et\n\x00s\x16e\x10\x00fo\r\x04t\x0c\x14o\x10\x10n\x08\x01y exploitatio'
        
        # 3) Play back and forth and I find the preceeding words
        # i = 37 | text = b'\x1a\x07et\n\x00s\x16e\x10\x00fo\r\x04t\x0c\x14 BINARY EXPLOITATIO'
        known_pt = b'ORY IS CRYPTOGRAPHY'.rjust(i, b'\x00')

        # 4) Now I guess that the word is 'category'
        # i = 37 | text = b'\x1a\x07et\n\x00s\x16e\x10\x00 ONE IS BINARY EXPLOITATIO'
        known_pt = b'F CATEGORY IS CRYPTOGRAPHY'.rjust(i, b'\x00')

        # 5) From the description, they talk about the best ctf category
        # i = 12 | text = b'\x1a\x07et\n\x00ST CTF'
        known_pt = b' BEST '.rjust(i, b'\x00')
        # i = 12 | text = b'\x1a\x07etBEST CTF'
        known_pt = b'HE BEST '.rjust(i, b'\x00')

        # 6) Combine what we have together
        # i = 37 | text = b'NO THE BE\x10\x00 ONE IS BINARY EXPLOITATIO'
        known_pt_start = b'THE BEST '
        known_pt_end = b'F CATEGORY IS CRYPTOGRAPHY'.rjust(i - len(known_pt_start), b'\x00')
        known_pt = known_pt_start + known_pt_end

        # 7) Finally we get the text from more guessing
        known_pt = b'THE BEST CTF CATEGORY IS CRYPTOGRAPHY'.rjust(i, b'\x00')
        # i = 37 | text = b'NO THE BEST ONE IS BINARY EXPLOITATIO'
        # guess_key = b'utflag{tw0_tim3_p4ds}utflag{tw0_tim3_'

        guess_key = xor_zip_bytes(known_pt, ak)
        decrypt_b = xor_zip_bytes(guess_key, bk)

        print('i =', i, '| text =', decrypt_b)      
    print('guess_key =', guess_key)      
    return None

if __name__ == '__main__':
    bruteforce_key()
