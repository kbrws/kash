# Imports
import lib.alphabet as mod_ab
import lib.scrambler as mod_scr
import lib.vig as mod_vig
from hashlib import md5 as func_md5
from random import shuffle as func_shuffle
from numpy import roll as func_roll

# Input
p3_raw = input("Message to decrypt: ")
p1_shift = int(input("Shift: "))
p3_slock = input("Shufflelock: ")
p3_pphrase = input("Passphrase: ")

# Variables / Functions
debug = False
p3_slock = func_md5(p3_slock.encode()).hexdigest()
p3_pphrase = func_md5(p3_pphrase.encode()).hexdigest()
if debug: print("SLock MD5: {}\nPPhrase MD5: {}".format(p3_slock, p3_pphrase))
altroll = lambda word, shift: word[shift:]+word[:shift]

# Phase 3
p3_stringp2 = mod_vig.decode(p3_pphrase, p3_raw)
if debug: print("Phase 3 R3: {}".format(p3_stringp2))
p3_split = p3_stringp2.split(":")
if debug: print("Phase 3 R2 SPLIT: {}".format(p3_split))
p3_shuffledec = mod_vig.decode(p3_slock, p3_split[1])
if debug: print("Phase 3 R2: {}".format(str(p3_shuffledec)))
p3_stringp1 = mod_scr.unscramble(p3_split[0], list(p3_shuffledec))
if debug: print("Phase 3 R1: {}".format(p3_stringp1))

# Phase 2
p2_ab = func_roll(mod_ab.all_s, p1_shift)
p2_sub = dict(zip(mod_ab.all_s, p2_ab))
p2_string = ''.join(p2_sub.get(c, c) for c in p3_stringp1)
if debug: print("Phase 2: <{}>".format(p2_string))

# Phase 1
p1_string = altroll(p2_string, p1_shift)
print("Result:\n{}".format(p1_string))