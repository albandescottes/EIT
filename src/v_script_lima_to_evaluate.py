import sys

if(len(sys.argv) != 2):
	print('Error, wrong parameter number')
else:
	out = []
	print(sys.argv[1])
	print(' > ')
	file = sys.argv[1].split('.')
	with open(sys.argv[1]) as f:
		lines = f.readlines()
		f.close()
	for line in lines:
		split = line.split('\t')
		if(len(split) != 1):
			if(split[0] != '0'):
				if(' ' in split[1]):
					newWord = split[1].replace(" ","Espace")
					if(split[5] == '_'):
						out.append(newWord + '_O')
					else:
						reresplit = split[5].split('.')
						out.append(newWord + '_' + reresplit[1])
					
				else:
					if(split[5] == '_'):
						out.append(split[1] + '_O')
					else:
						reresplit = split[5].split('.')
						out.append(split[1] + '_' + reresplit[1])
		else:
			out.append('\n')

	newFile = ''
	for i in range(len(file) - 2):
		newFile += file[i] + '.'
	newFile += 'txt.lima.ne'
	print(newFile)
	file = open(newFile, 'w')
	for word in out:
		if(word != '\n'):
			file.write(word + '\n')
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