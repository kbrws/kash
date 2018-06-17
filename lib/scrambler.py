def scramble(s, p):
	chars = list(s)
	scrambled = ['']*len(chars)
	for char, i in zip(chars, p):
		#scrambled[i] = char
		scrambled.append(char)
	return ''.join(scrambled)

def unscramble(s, p):
	reverse_p = sorted(range(len(p)), key=p.__getitem__)
	return scramble(s, reverse_p)