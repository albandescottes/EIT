import sys

if(len(sys.argv) != 2):
	print('Error, wrong parameter number')
else:
	# création de l'output
	split = sys.argv[1].split('.')
	newFile = ''
	for i in range(len(split) - 2):
		newFile += split[i] + '.'
	newFile += 'txt.pos.ref'
	# lecture de l'input
	with open(sys.argv[1]) as f:
		lines = f.readlines()
		f.close()
	# écriture de l'output
	file = open(newFile, 'w')
	for line in lines:
		split = line.split('\t')
		if(len(split) != 1):
			file.write(split[0] + '_' + split[1])
	file.close()