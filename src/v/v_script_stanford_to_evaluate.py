import sys

if(len(sys.argv) != 2):
	print('Error, wrong parameter number')
else:
	print(sys.argv[1])
	print(' > ')
	split = sys.argv[1].split('.')
	newFile = ''
	for i in range(len(split) - 2):
		newFile += split[i] + '.'
	newFile += 'txt.stanford.ne'

	with open(sys.argv[1]) as f:
		lines = f.readlines()
		f.close()
	print(newFile)
	file = open(newFile, 'w')

	for line in lines:
		split = line.split()
		for w in split:
			resplit = w.split('/')
			file.write(resplit[0] + '_' + resplit[1] + '\n')
	file.close()

	with open(newFile) as f:
		lines = f.readlines()
		f.close()
	file = open(newFile, 'w')

	for line in lines:
		word = line.replace("\n", "")
		split = word.split('_')
		if(split[0] == '.'):
			file.write(word + '\n')
		else:
			file.write(word + ' ')
	file.close()