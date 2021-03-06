import sys

if(len(sys.argv) != 2):
	print('Error, wrong parameter number')
else:
	# création du fichier output
	split = sys.argv[1].split('.')
	newFile = ''
	for i in range(len(split) - 2):
		newFile += split[i] + '.'
	newFile += 'txt.pos.lima'

	out = []
	# lecture de l'input
	with open(sys.argv[1]) as f:
		lines = f.readlines()
		f.close()
	# parcours de l'input
	for line in lines:
		split = line.split('\t')
		if(len(split) != 1):
			if(split[0] != '0'):
				if(split[3] == 'PONCTU'):
					out.append(split[1] + '_' + split[1])
				else:
					word = split[1].replace(" ","Espace")
					out.append(word + '_' + split[4])	
		else:
			out.append('\n')
	# ecriture dans l'output
	file = open(newFile, 'w')
	for word in out:
		if(word != '\n'):
			file.write(word + '\n')
	file.close()