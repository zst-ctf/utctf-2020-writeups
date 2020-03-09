#!/usr/bin/env python3
import string
import socket
import telnetlib
import statistics

'''
Random ECB
1922
nc crypto.utctf.live 9003

by dmanc

$ nc crypto.utctf.live 9003
Input a string to encrypt (input 'q' to quit):

Here is your encrypted string, have a nice day :)
48c4dddab92943c70724451780d8fddc2a7d2771570cb0d414c2b9b2285439b7

'''

# Connect to server
s = socket.socket()
s.connect(('ecb.utctf.live', 9003))
t = telnetlib.Telnet()
t.sock = s

def encrypt(s):
	t.write(s.encode() + b'\n')
	t.read_until(b'Here is your encrypted string, have a nice day :)\n')
	encrypted = t.read_until(b'\n').decode().strip()
	return encrypted

known_pt = 'utfl'
known_pt = 'utflag{3cb_w'
pad = ''

appeared_before = set()

block_to_attack = 1 # zero-indexed

# while not yet end of flag
while '}' not in known_pt:
	print("\nStart")
	# get padded only
	len_pad = block_to_attack*16 + 15 - len(known_pt)
	pad = 'A' * len_pad
	payload = pad
	while True:
		target_enc = encrypt(payload)
		print("Target:", target_enc)

		# this means that it has occurred before
		# hence, one extra padding which was covered previously
		# so we know that the random bit has occurred.
		if target_enc not in appeared_before:
			appeared_before.add(target_enc)
			break
	while True:
		success = False

		# remove newline from the characters to test or it will cause issues in sending payload
		for ch in (string.printable.replace('\n', '')):
			payload = pad + known_pt + ch
			enc = encrypt(payload)

			# we can choose which targetted block to attack
			encoded_block = enc[block_to_attack*32:block_to_attack*32+32]
			target_block = target_enc[block_to_attack*32:block_to_attack*32+32]
			attacked_block_is_equal = (encoded_block == target_block)
			
			#if attacked_block_is_equal and ch == '\x01':
			#	print("\rFailed (Rand bit):", ch, known_pt, end='')
			#	break

			# if appeared before, means that one extra padding was randomly added
			if attacked_block_is_equal and encoded_block not in appeared_before:
				print("\nSuccess:", ch, known_pt)
				success = True
				known_pt += ch
				appeared_before.add(target_block)
				break
			else:
				print("\rFailed:", ch, known_pt, end='')

		if success:
			break

# Flag
# Success: } utflag{3cb_w17h_r4nd0m_pr3f1x
