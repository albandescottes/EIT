import sys

if(len(sys.argv) != 2):
	print('Error, wrong parameter number')
else:
	split = sys.argv[1].split('.')
	newFile = ''
	for i in range(len(split) - 2):
		newFile += split[i] + '.'
	newFile += 'txt.' + split[len(split) - 2] + '.' + split[len(split) - 1]

	with open(sys.argv[1]) as f:
		lines = f.readlines()
		f.close()
	file = open(sys.argv[1], 'w')

	for line in lines:
		word = line.replace("\n", "")
		split = word.split('_')
		if(split[0] == '.'):
			file.write(word + '\n')
		else:
			file.write(word + ' ')
	file.close()