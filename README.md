# UTCTF 2020 Writeups

This is a collection of my writeups for challenges in [UTCTF 2020](https://hsctf.com/)

---

## IR

#### Challenge

	We found this snippet of code on our employee's laptop.
	It looks really scary. Can you figure out what it does?

#### Solution

We are given a file with LLVM IR code. 

From these references, we can see how the language works.

- https://llvm.org/docs/LangRef.html
- https://idea.popcount.org/2013-07-24-ir-is-better-than-assembly/

And from here, we can slowly reverse each like into psuedo-C code.

> [ir_psuedocode.c](./IR/ir_psuedocode.c)

And from this, I can see what the code does:

- Input an char array to the function as a parameter
- In the 1st for-loop, the number 5 is added to each character
- In the 2nd for-loop, each character is XORed with the next character (ie. index `i` is XORed with index `i+1` and stored back into index `i`)
- The output is then checked against the global array `@check`

Do it in reverse to get the flag

> [solve_ir.py](./IR/solve_ir.py)

#### Flag

	utflag{machine_agnostic_ir_is_wonderful}

---

## One_True_Problem

#### Challenge

	One True Problem

	Two of my friends were arguing about which CTF category is the best,
	but they encrypted it because they didn't want anyone to see.
	Lucky for us, they reused the same key; can you recover it?

	Here are the ciphertexts:
	    213c234c2322282057730b32492e720b35732b2124553d354c22352224237f1826283d7b0651
	    3b3b463829225b3632630b542623767f39674431343b353435412223243b7f162028397a103e

#### Solution

Known plaintext attack on XOR cipher. By guessing "which CTF category is the best", I first did a decryption of 'cryptography'.

See comments in [my Python script](./One_True_Problem/One_True_Problem-Cryptography.py)

#### Flag

	utflag{tw0_tim3_p4ds}

---

## .PNG2

#### Challenge

	In an effort to get rid of all of the bloat in the .png format, I'm proud to announce .PNG2!
	The first pixel is #7F7F7F, can you get the rest of the image?

#### Solution

Read the file using a hex reader (xxd or hexdump).

	PNG2 $ xxd pic.png2 | head -3
	00000000: 504e 4732 7769 6474 683d 05cf 6865 6967  PNG2width=..heig
	00000010: 6874 3d02 887f 7f7f 7f7f 7f7f 7f7f 7f7f  ht=.............
	00000020: 7f7f 7f7f 7f7f 7f7f 7f7f 7f7f 7f7f 7f7f  ................

From here, we can see that the width=0x05cf and height=0x0288 are defined. This is followed by RGB bytes of the pixels.

Using a script, create a new image of the width and height and then fill in group of 3 bytes as the RGB pixel.

This will produce a readable PNG file.

> [./PNG2/solve_png2.py](./PNG2/solve_png2.py)

---

## Random_ECB

#### Challenge

	$ nc crypto.utctf.live 9003

	Input a string to encrypt (input 'q' to quit):

	Here is your encrypted string, have a nice day :)
	48c4dddab92943c70724451780d8fddc2a7d2771570cb0d414c2b9b2285439b7

#### Solution

The challenge is a server which we can input a string to do AES-ECB.

The source for the encryption is as follows:

	def encryption_oracle(plaintext):
	    b = getrandbits(1)
	    plaintext = pad((b'A' * b) + plaintext + flag, 16)
	    return aes_ecb_encrypt(plaintext, KEY).hex()

Here, we see that the plaintext is appended with the flag. Hence, this is an AES-ECB Chosen 
Plaintext Attack.

- https://zachgrace.com/posts/attacking-ecb/
- https://crypto.stackexchange.com/questions/42891/chosen-plaintext-attack-on-aes-in-ecb-mode

However, there is a random character 'A' that is prepended to the plaintext.

We can defeat this by checking if the output is repeated.

1. Let's say we do a padding of 'A' * 15. We store the output.
2. Next, when we do a padding of 'A' * 14, if a random bit occurs, it will be equal to the previous output (repeated), so we know that the random character occurred.

#### Flag

	utflag{3cb_w17h_r4nd0m_pr3f1x}


