import sys

if(len(sys.argv) != 2):
	print('Error, wrong parameter number')
else:
	# création de l'output
	split = sys.argv[1].split('.')
	newFile = ''
	for i in range(len(split) - 2):
		newFile += split[i] + '.'
	newFile += 'txt.' + split[len(split) - 2] + '.' + split[len(split) - 1]
	# lecture de l'input
	with open(sys.argv[1]) as f:
		lines = f.readlines()
		f.close()
	file = open(sys.argv[1], 'w')
	# écriture de l'output
	for line in lines:
		word = line.replace("\n", "")
		split = word.split('_')
		if(split[0] == '.'):
			file.write(word + '\n')
		else:
			file.write(word + ' ')
	file.close()