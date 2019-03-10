import sys

def createDic():
	with open('POSTags_PTB_Universal_Linux.txt') as f:
		universel = f.readlines()
		f.close()

	dic = {
		"TAG" : "TAG"
	}
	for tag in universel:
		split = tag.split()
		dic[split[0]] = split[1]
	return dic

def createNewFile(file, dic):
	print(file)
	split = file.split('.')
	newFile = ''
	for i in range(len(split) - 1):
		newFile += split[i] + '.'
	newFile += 'univ.' + split[len(split) - 1]

	with open(file) as f:
		lines = f.readlines()
		f.close()
	file = open(newFile, 'w')

	for line in lines:
		split = line.replace("\n","").split('_')
		if(len(split) != 1):
			if(dic.get(split[1]) != None):
				file.write(split[0] + '_' + dic[split[1]] + '\n')
			else:
				file.write(split[0] + '_' + split[1] + '\n')
	file.close()
	print('success : ' + newFile + ' created')


if(len(sys.argv) != 2):
	print('Error, wrong parameter number')
else:
	dic = createDic()
	createNewFile(sys.argv[1], dic)