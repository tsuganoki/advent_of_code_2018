

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

def log_ids():
	ids = []
	for row in open('002_inputs.txt'):
		row = row.rstrip()
		ids.append(row)
	return(ids)

def log_twos_and_threes():
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


ids = log_ids()
test_ids = ['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz']

# print(ids[:30])
str1 = 'kqnxdenujwcsthbmgvlooflarp'
str2 = 'kqzxdknpjwcsthwmgvyioflarp'

# print(has_two_or_three(str1))
# print(has_two_or_three(str2))

# twos,threes = log_twos_and_threes()
# print(twos,threes)
# print(twos * threes)


def compare_strings(str1,str2):
	same = True
	for i in range(len(str1)):
		if str1[i] != str2[i] and same:
			same = False
		elif str1[i] != str2[i]:
			return False
	if not same:
		return True

# print(compare_strings("fghij","fguij"))

def compare_all(ids):
	for i,str1 in enumerate(ids):
		for j,str2 in enumerate(ids[i:]):
			# print(i,j,str1,str2)
			if compare_strings(str1,str2):
				return (str1,str2)

str1,str2 = (compare_all(ids))
print(str1,str2)