"""
KASH made by kbrrws

Explanation:

	3 Phases

	Shift:
	Move all characters left or right by n

	Substitution:
	Replace all characters with corrosponding characters but shifted opposite way of Phase 1
	Ex: Shifted Right 5, Subbed Left 5

	Final:
	Scramble the output.
	Encrypt the scramble key with VIGC.
	Add scrambled text and scramble key and protect with passphrase using VIGC.

https://github.com/kbrrws
"""

# Imports
import lib.alphabet as mod_ab
import lib.scrambler as mod_scr
import lib.vig as mod_vig
from hashlib import md5 as func_md5
from random import shuffle as func_shuffle
from numpy import roll as func_roll

# Config
csum = False
debug = False

# Inputs
p0_rawmsg = input("Message to encrypt: ")
p0_msg = list(p0_rawmsg)
p4_hash = func_md5(str.encode(p0_rawmsg))
p4_csum = p4_hash.hexdigest()
p1_shift = int(input("Shift: "))
p3_slock = input("Shufflelock: ")
p3_pphrase = input("Passphrase: ")

p3_slock = func_md5(p3_slock.encode()).hexdigest()
p3_pphrase = func_md5(p3_pphrase.encode()).hexdigest()
if debug: print("SLock MD5: {}\nPPhrase MD5: {}".format(p3_slock, p3_pphrase))

# Phase 1
p1_string = func_roll(p0_msg, p1_shift)
if debug: print("Phase 1: {}".format("".join(p1_string)))

# Phase 2
p2_ab = func_roll(mod_ab.all_s, p1_shift * -1)
p2_sub = dict(zip(mod_ab.all_s, p2_ab))
p2_string = ''.join(p2_sub.get(c, c) for c in p1_string)
if debug: print("Phase 2: {}".format(p2_string))

# Phase 3
p3_key = list(range(0, len(list(p2_string))))
func_shuffle(p3_key)
p3_strkey = "".join(str(num) for num in p3_key)
p3_stringp1 = mod_scr.scramble(p2_string, p3_key)
if debug: print("Phase 3 R1: {}:{}".format(p3_stringp1, p3_strkey))
p3_shuffleenc = mod_vig.encode(p3_slock, p3_strkey)
if debug: print("Phase 3 R2: {}:{}".format(p3_stringp1, str(p3_shuffleenc)))
p3_stringkey = "{}:{}".format(p3_stringp1, p3_shuffleenc.decode())
p3_stringp2 = mod_vig.encode(p3_pphrase, p3_stringkey)
if debug: print("Phase 3 R3: {}".format(str(p3_stringp2)))
print(p3_stringp2.decode())

# Checksum (Optional)
if csum: print(("-" * 32) + "\nChecksum:\n{}".format(p4_csum))