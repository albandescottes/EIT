from prettytable import PrettyTable

f = open("formal-tst.NE.key.04oct95_small.ner.stanford", "r")
text = f.read()
sortedText = [mytext.split("/") for mytext in text.split()]

dictio = {}
dictioEtiq = {}
t = PrettyTable(['Entité nommée', 'Type', 'Nombre d\'occurence', 'Proportion dans le texte'])
totallength = 0


for word in sortedText:
	if (word[1] == "O"):
		continue;
	else:
		if word[0] not in dictio:
			dictio[word[0]] = 1
			dictioEtiq[word[0]] = word[1]
			totallength += 1
		else:
			dictio[word[0]] += 1
			totallength += 1

for word in dictio:
	t.add_row([word, dictioEtiq[word], dictio[word], ((dictio[word]/totallength)*100)])

print(t)


