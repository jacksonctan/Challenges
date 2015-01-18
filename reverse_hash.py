import sys

letters = "acdegilmnoprstuw"

def reverse_hash(hash_val, s_len):

	s = ""

	while(s_len > 0):
		idx = hash_val % 37
		s = letters[idx] + s
		hash_val = (hash_val - idx) / 37
		s_len = s_len - 1

	return s


def hash(s):
	h = 7
	for i in range(len(s)):
		h = (h * 37 + letters.index(s[i]))

	return h


def main(argv):
	s = str(argv[0])
	s_len = len(s)
	hash_val = hash(s)

	print "\n\tHash value is " + str(hash_val)
	print "\tString length is " + str(s_len)

	reverse_hash_output = reverse_hash(hash_val, s_len)

	print "\tOutput for reverse_hash() is " + reverse_hash_output
	if reverse_hash_output == s:
		print "\tCongratufrigginlations, the input string to hash() matches the output string of reverse_hash()\n"
	else:
		print "\tYou f****d up\n"

if __name__  == "__main__":
	main(sys.argv[1:])



