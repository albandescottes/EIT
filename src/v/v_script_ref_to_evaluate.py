import sys
import re

if(len(sys.argv) != 2):
	print('Error, wrong parameter number')
else:
	print(sys.argv[1])
	print(' > ')
	# création de l'output
	split = sys.argv[1].split('.')
	newFile = ''
	for i in range(len(split) - 1):
		newFile += split[i] + '.'
	newFile += 'txt.ref.ne'
	# lecture de l'input
	with open(sys.argv[1]) as f:
		lines = f.readlines()
		f.close()
	print(newFile)
	file = open(newFile, 'w')
	# ecriture de l'output
	for line in lines:
		line = re.sub(r"<TIMEX.*?>", "", line)
		line = re.sub(r"<\/TIMEX>", "", line)
		regex = r"(<ENAMEX.*?<\/ENAMEX>)"
		split = re.split(regex, line)
		for element in split:
			if( "</ENAMEX>" in element):
				regex = r"<ENAMEX TYPE=\"(.*?)\".*?>(.*?)<\/ENAMEX>"
				after = re.split(regex, element)
				file.write(after[2].replace(" ","Espace") + '_' + after[1] + '\n')
			else:
				resplit = element.split()
				for word in resplit:
					if("," in word):
						if(word == ','):
							file.write(",_O\n")
						else:
							file.write(word.replace(",","") + '_O\n')
							file.write(",_O\n")
					elif("." in word):
						if(word == '.'):
							file.write("._O\n")
						else:
							if(split.index(element) == (len(split) - 1)):
								file.write(word.replace(".","") + '_O\n')
								file.write("._O\n")
							else:
								file.write(word + '_O\n')
					else:
						file.write(word + '_O\n')
	file.close()
	#lecture du fichier temporaire
	with open(newFile) as f:
		lines = f.readlines()
		f.close()
	file = open(newFile, 'w')
	#ecriture du fichier final
	for line in lines:
		word = line.replace("\n", "")
		split = word.split('_')
		if(split[0] == '.'):
			file.write(word + '\n')
		else:
			file.write(word + ' ')
	file.close()