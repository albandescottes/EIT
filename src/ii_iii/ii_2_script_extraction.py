from lxml import etree
from prettytable import PrettyTable

tree = etree.parse("formal-tst.NE.key.04oct95_sample.txt.se.xml")
total_length = 0
dictio = {}
already = {}
verify = 0.0

for entity in tree.xpath("/specific_entities/specific_entity"):
	total_length += 1


t = PrettyTable(['Entité nommée', 'Type', 'Nombre d\'occurence', 'Proportion dans le texte'])

#Remplir un premier dictionnaire afin d'avoir le nombre d'occurence correspondant à chaque mot.
for entity in tree.xpath("/specific_entities/specific_entity"):
	if entity[0].text not in dictio:
		dictio[entity[0].text] = 1
		
	else:
		dictio[entity[0].text] += 1

#le deuxieme dictionnaire sert à  ne pas afficher 
for entity in tree.xpath("/specific_entities/specific_entity"):
	if entity[0].text not in already:
		already[entity[0].text] = 1
		t.add_row([entity[0].text, entity[3].text, dictio[entity[0].text], ((dictio[entity[0].text]/total_length)*100)])
		

print(t)