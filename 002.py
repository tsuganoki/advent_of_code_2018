

inputs = []
id_totals = {3: 0, 4: 0}


def has_two_or_three(id_str):
	char_dict = {}
	for c in id_str:
		char_dict[c] = char_dict.get(c,0) + 1
	two = False
	three = False
	# print(char_dict)
	if 2 in char_dict.values():
		two = True
	if 3 in char_dict.values():
		three = True
	return (two,three)

def log_inputs():
	twos = 0
	threes = 0
	for row in open('002_inputs.txt'):
		row = row.rstrip()
		two,three = has_two_or_three(row)
		if two:
			twos += 1
		if three:
			threes += 1
	return (twos,threes)



str1 = 'kqnxdenujwcsthbmgvlooflarp'
str2 = 'kqzxdknpjwcsthwmgvyioflarp'

# print(has_two_or_three(str1))
# print(has_two_or_three(str2))

# twos,threes = log_inputs()
# print(twos,threes)
# print(twos * threes)


