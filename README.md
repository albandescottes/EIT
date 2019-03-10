# EIT

## Partie II

Extraction d'entités nommées

Modifier le fichier ii_2_script_extraction.py dans le dossier src\ii_iii afin de changer le chemin vers le fichier dont on souhaite extraire les entités.
Ici, le fichier doit être au format xml.
La ligne à modifier est la suivante :
```shell
tree = etree.parse("formal-tst.NE.key.04oct95_sample.txt.se.xml")
```
Ensuite exécuter ce script  et rediriger la sortie vers un fichier résultat:

```shell
$ python3 ii_2_script_extraction.py > ii_2_results.txt
```

Obtention du résultat CEA List
```shell
$ analyzeText -l eng wsj_0010_sample.txt > wsj_0010_sample.txt.conll
```

Transformation pour le CEA List
```shell
# txt.conll > txt.pos.lima
$ python3 ii_iii_script_transform_conll_to_txt_pos.py wsj_0010_sample.txt.conll
# txt.pos.lima > txt.pos.univ.lima
$ python3 ii_iii_script_transform_tag_to_universel.py wsj_0010_sample.txt.pos.lima
# mise en phrase
$ python3 ii_iii_script_in_sentence.py wsj_0010_sample.txt.pos.lima
$ python3 ii_iii_script_in_sentence.py wsj_0010_sample.txt.pos.univ.lima
```
Transformation pour la référence
```shell
# pos.ref > txt.pos.ref
$ python3 ii_iii_script_transform_pos_to_txt_pos.py wsj_0010_sample.pos.ref
# txt.pos.ref > txt.pos.univ.ref
$ python3 ii_iii_script_transform_tag_to_universel.py wsj_0010_sample.txt.pos.ref
# mise en phrase
$ python3 ii_iii_script_in_sentence.py wsj_0010_sample.txt.pos.ref
$ python3 ii_iii_script_in_sentence.py wsj_0010_sample.txt.pos.univ.ref
```
Comparaison 
```shell
$ python2 evaluate.py xxx.lima xxx.ref
```
## Partie III
Obtention du résultat Stanford postagger
```shell
$ ./stanford-postagger.sh models/english-left3words-distsim.tagger wsj_0010_sample.txt > wsj_0010_sample.pos.stanford
```

Transformation pour stanford
```shell
# pos.stanford > txt.pos.stanford
$ python3 ii_iii_script_transform_in_line.py wsj_0010_sample.pos.stanford
# txt.pos.stanford > txt.pos.univ.stanford
$ python3 ii_iii_script_transform_tag_to_universel.py wsj_0010_sample.txt.pos.stanford
# mise en phrase
$ python3 ii_iii_script_in_sentence.py wsj_0010_sample.txt.pos.stanford
$ python3 ii_iii_script_in_sentence.py wsj_0010_sample.txt.pos.univ.stanford
```
Comparaison 
```shell
$ python2 evaluate.py xxx.stanford xxx.ref
```
## Partie IV
Obtention du résultat Stanford NER
```shell
$ java -mx600m -cp stanford-ner.jar:lib/* edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier classifiers/english.all.3class.distsim.crf.ser.gz -textFile  formal-tst.NE.key.04oct95_small.txt > formal-tst.NE.key.04oct95_small.ner.standford 
```

Extraction d'entités nommées

Modifier le fichier iv_2_script_extraction.py dans le dossier src\iv afin de changer le chemin vers le fichier dont on souhaite extraire les entités.
La ligne à modifier est la suivante :
```shell
f = open("formal-tst.NE.key.04oct95_small.ner.stanford", "r")
```
Ensuite exécuter ce script  et rediriger la sortie vers un fichier résultat:

```shell
$ python3 iv_2_script_extraction.py > iv_2_results.txt
```

## Partie V
Obtention du résultat CEA List
```shell
$ analyzeText -l eng formal-tst.NE.key.04oct95_small.txt > formal-tst.NE.key.04oct95_small.ner.lima
```
Transformation pour analyse
```shell
# CEA List > txt.lima.ne
$ python3 v_script_lima_to_evaluate.py formal-tst.NE.key.04oct95_small.ner.lima
# Stanford > txt.stanford.ne
$ python3 v_script_lima_to_evaluate.py formal-tst.NE.key.04oct95_small.ner.stanford
# Référence > txt.ref.ne
$ python3 v_script_lima_to_evaluate.py formal-tst.NE.key.04oct95_small.ne
```
Comparaison
```shell
python2 evaluate.py xxx.txt.lima.ne xxx.txt.ref.ne
python2 evaluate.py xxx.txt.stanford.ne xxx.txt.ref.ne
```
