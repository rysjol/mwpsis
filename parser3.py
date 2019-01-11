import os
import sys
import array as arr
# import xml.etree.ElementTree as et
from xml.etree import ElementTree
from subprocess import call

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
['Link_0_10','1'],
['Link_0_2','2'],
['Link_1_2','3'],
['Link_1_7','4'],
['Link_1_10','5'],
['Link_2_9','6'],
['Link_3_4','7'],
['Link_3_6','8'],
['Link_3_11','9'],
['Link_4_8','10'],
['Link_4_10','11'],
['Link_5_8','12'],
['Link_5_10','13'],
['Link_6_10','14'],
['Link_6_11','15'],
['Link_7_9','16'],
['Link_7_11','17'],
['Link_0_5','18']
]






source = sys.argv[1]
target = sys.argv[2]

lista = []
lista2 = []

# for w in tree.findall(".//demand/[city='" + source + "']"):
#    # print(w.attrib)
#    lista.append(w.attrib)
# for v in tree.findall(".//demand/[city='" + target + "']"):
#    # print(v.attrib)
#    lista2.append(v.attrib)

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
with open("results.mod", "a") as f:
   for p in range(0, 10):
       z=[]
       for x in tree.findall(
           ".//demands/demand/[@id='" + demands[0].get("id") + "']/admissiblePaths/admissiblePath/[@id='P_" + str(
               p) + "']/linkId"):
           for it in linki:
               x.text = x.text.replace(it[0],it[1])
       #print("%s, 1, %d 1" % (x.text, p+1 ))
           f.write("%s, 1, %d 1" % (x.text, p+1 ) + "\r")
           p_count=p+1
           z.append(x.text)
       f.write("\r\r")
   f.write(";\rparam P_count := "+str(p_count)+"\r; /*liczba sciezek*/\r")

with open("dane.dat") as f2:
   with open("results.mod", "a") as f3:
       for line in f2:
           f3.write(line)

f.close()


os.system('cbc results.mod% -solve -solu out.csv')


