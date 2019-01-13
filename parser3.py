import os
import sys
import array as arr
import re
import json
# import xml.etree.ElementTree as et
from xml.etree import ElementTree
from subprocess import call
from urllib.parse import parse_qs
import subprocess

import collections

file_name = 'polska_dar.xml'
full_file = os.path.abspath(os.path.join('data', file_name))
tree = ElementTree.parse(full_file)
#słownik linków od Marcina do xmla
tranzyt = {
   0: "Gdansk",
   1: "Bydgoszcz",
   2: "Kolobrzeg",
   3: "Katowice",
   4: "Krakow",
   5: "Bialystok",
   6: "Lodz",
   7: "Poznan",
   8: "Rzeszow",
   9: "Szczecin",
   10: "Warsaw",
   11: "Wroclaw"
}

#print(str(sys.argv))
#print()
# Słownik z xmla do modelu


linki = [
['Link_0_10','1','[[18.653259,54.348590],[21.0100477, 52.2497413]]'],
['Link_0_2','2','[[18.653259,54.348590],[15.574454, 54.1762177]]'],
['Link_1_2','3','[[18.000434,53.121994],[15.574454, 54.1762177]]'],
['Link_1_7','4','[[18.000434,53.121994],[16.9314281, 52.4082542]]'],
['Link_1_10','5','[[18.000434,53.121994],[21.0100477, 52.2497413]]'],
['Link_2_9','6','[[15.574454, 54.1762177],[14.5576182, 53.4243505]]'],
['Link_3_4','7','[[19.0195338, 50.2590427],[19.9351372, 50.0615991]]'],
['Link_3_6','8','[[19.0195338, 50.2590427],[19.452173, 51.7811939]]'],
['Link_3_11','9','[[19.0195338, 50.2590427],[17.0301722, 51.1106992]]'],
['Link_4_8','10','[[19.9351372, 50.0615991],[22.0033492, 50.037221]]'],
['Link_4_10','11','[[19.9351372, 50.0615991],[21.0100477, 52.2497413]]'],
['Link_5_8','12','[[23.1585387, 53.1322542],[22.0033492, 50.037221]]'],
['Link_5_10','13','[[23.1585387, 53.1322542],[21.0100477, 52.2497413]]'],
['Link_6_10','14','[[19.452173, 51.7811939],[21.0100477, 52.2497413]]'],
['Link_6_11','15','[[19.452173, 51.7811939],[17.0301722, 51.1106992]]'],
['Link_7_9','16','[[16.9314281, 52.4082542],[14.5576182, 53.4243505]]'],
['Link_7_11','17','[[16.9314281, 52.4082542],[17.0301722, 51.1106992]]'],
['Link_0_5','18','[[18.653259,54.348590],[23.1585387, 53.1322542]]']
]







query_string = sys.argv[1]
# target = sys.argv[2]
data = parse_qs(query_string)
source = tranzyt[int(data['start'][0])]
target = tranzyt[int(data['stop'][0])]
load = int(data['load'][0])

lista = []
lista2 = []

for w in tree.findall(".//demand/[city='" + source + "']"):
   # print(w.attrib)
   lista.append(w.attrib)
for v in tree.findall(".//demand/[city='" + target + "']"):
   # print(v.attrib)
   lista2.append(v.attrib)

#Otrzymywanie demandu
def intersection(lista, lista2):
   lista3 = [value for value in lista if value in lista2]
   return lista3

demands = intersection(lista, lista2)

with open("model.mod") as f:
   with open("results.mod", "w") as f1:
       for line in f:
           f1.write(line)

path = []
p_count = 0
with open("results.mod", "a") as f:
   for p in range(0, 10):
       z=[]
       for x in tree.findall(
           ".//demands/demand/[@id='" + demands[0].get("id") + "']/admissiblePaths/admissiblePath/[@id='P_" + str(
               p) + "']/linkId"):
           for it in linki:
               x.text = x.text.replace(it[0],it[1])
           f.write("%s, 1, %d 1" % (x.text, p+1 ) + "\r")
           last_p_count=p_count
           p_count=p+1
           z.append(x.text)
       f.write("\r\r")
   f.write(";\rparam P_count := "+str(p_count)+"\r; /*liczba sciezek*/\r")
   f.write("param h :=\r 1 "+str(load)+" \r;\r")
with open("dane.dat") as f2:
   with open("results.mod", "a") as f3:
       for line in f2:
           f3.write(line)


with open("paths.mod", "w") as f:
   for p in range(0, 10):
       z=[]
       for x in tree.findall(
           ".//demands/demand/[@id='" + demands[0].get("id") + "']/admissiblePaths/admissiblePath/[@id='P_" + str(
               p) + "']/linkId"):
           for it in linki:
               x.text = x.text.replace(it[0],it[1])
           f.write(x.text+ ";")
           z.append(x.text)
       f.write("\r")

#os.system('cbc results.mod% -solve -solu out.csv')
subprocess.run(['cbc', 'results.mod%', '-solve', '-solu', 'out.csv'], stdout = open('ttt.txt', 'w'))

with open("out.csv", "r") as f:
	file = f.read()
	small_car=str(0)
	midi_car=str(0)
	big_car=str(0)
	pathID = re.findall("x\[1\,(.)", file)
	value = str(re.findall("value (\w+)", file)[0])
	if re.findall("f\[.*\,1]\s*(\w+)\s*", file):
		small_car = str(re.findall("f\[.*\,1]\s*(\w+)\s*", file)[0])
	if re.findall("f\[.*\,2]\s*(\w+)\s*", file):
		midi_car = str(re.findall("f\[.*\,2]\s*(\w+)\s*", file)[0])
	if re.findall("f\[.*\,3]\s*(\w+)\s*", file):
		big_car = str(re.findall("f\[.*\,3]\s*(\w+)\s*", file)[0])
	print("Aby przewieźć "+str(load)+" palet z "+source+" do "+target+" potrzebujesz "+small_car+" małych, "+midi_car+" średnich i "+big_car+" dużych pojazdów. Będzie kosztować to "+value+" złotych.")
with open ("paths.mod", "r") as f:
	line = f.readlines()
	path = line[int(pathID[0])-1]
path = path[:-2].split(';')
with open("js/links.geojson","w") as f:
	f.write('{\r"type": "MultiLineString",\r"coordinates": [')
	for link in path:
		f.write(str(linki[int(link)-1][2])+",")
	f.seek(f.tell() - 1, os.SEEK_SET)
	f.write(']\r}')

