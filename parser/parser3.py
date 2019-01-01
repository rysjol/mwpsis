import os
import array as arr
# import xml.etree.ElementTree as et
from xml.etree import ElementTree
from subprocess import call

os.system('dir')
import collections

file_name = 'polska_dar.xml'
full_file = os.path.abspath(os.path.join('data', file_name))
tree = ElementTree.parse(full_file)
# słownik linków od Marcina do xmla
# tranzyt = {
#     0: "Gdansk",
#     1: "Bydgoszcz",
#     2: "Kolobrzeg",
#     3: "Katowice",
#     4: "Krakow",
#     5: "Bialystok",
#     6: "Lodz",
#     7: "Poznan",
#     8: "Rzeszow",
#     9: "Szczecin",
#     10: "Warsaw",
#     11: "Wroclaw"
# }
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




source = 'Wroclaw'
target = 'Krakow'

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

f= open("results.mod","w+")

f.write("/* Input data */"+ "\r")
f.write("data;"+ "\r")
f.write(""+ "\r")
f.write("param P_count := 4; /*liczba sciezek*/"+ "\r")
f.write("param E_count := 18; /*liczba krawedzi*/"+ "\r")
f.write("param D_count := 1; /*liczba zapotrzebowan*/"+ "\r")
f.write("/*wartosci zapotrzebowan, po 10 dla pierwszego i drugiego*/"+ "\r")
f.write("param : h :="+ "\r")
f.write(" 1      1"+ "\r")
f.write(";"+ "\r")
f.write("/*Macierz delta"+ "\r") 
f.write("(mowi ktore linki"+ "\r") 
f.write("wchodza w sklad"+ "\r") 
f.write("jakich sciezek)*/"+ "\r")
f.write("param : LAM :="+ "\r")

path = []
for p in range(0, 10):
    z = []
    for x in tree.findall(
            ".//demands/demand/[@id='" + demands[0].get("id") + "']/admissiblePaths/admissiblePath/[@id='P_" + str(
                p) + "']/linkId"):
        for it in linki: 
            x.text = x.text.replace(it[0],it[1])
        print("%s, 1, %d 1" % (x.text, p+1 ))
        f.write("%s, 1, %d 1" % (x.text, p+1 ) + "\r")
        z.append(x.text)
    f.write("\r")
f.write(";"+ "\r")
f.write("/* Kilometry per link */"+ "\r")
f.write("param : KSI :="+ "\r")
f.write("1 156"+ "\r")
f.write("2 272"+ "\r")
f.write("3 156"+ "\r")
f.write("4 186"+ "\r")
f.write("5 272"+ "\r")
f.write("6 237"+ "\r")
f.write("7 208"+ "\r")
f.write("8 181"+ "\r")
f.write("9 208"+ "\r")
f.write("10 250"+ "\r")
f.write("11 324"+ "\r")
f.write("12 324"+ "\r")
f.write("13 250"+ "\r")
f.write("14 165"+ "\r")
f.write("15 305"+ "\r")
f.write("16 142"+ "\r")
f.write("17 195"+ "\r")
f.write("18 294"+ "\r")
f.write(";"+ "\r")
f.write(""+ "\r")
f.write("/* Oplata za Autobahn */"+ "\r")
f.write("param : KSA :="+ "\r")
f.write("1 1000"+ "\r")
f.write("2 1000"+ "\r")
f.write("3 0"+ "\r")
f.write("4 0"+ "\r")
f.write("5 0"+ "\r")
f.write("6 1000"+ "\r")
f.write("7 0"+ "\r")
f.write("8 0"+ "\r")
f.write("9 0"+ "\r")
f.write("10 1000"+ "\r")
f.write("11 1"+ "\r")
f.write("12 0"+ "\r")
f.write("13 1"+ "\r")
f.write("14 0"+ "\r")
f.write("15 1"+ "\r")
f.write("16 0"+ "\r")
f.write("17 0"+ "\r")
f.write("18 1000"+ "\r")
f.write(";"+ "\r")
f.write(""+ "\r")
f.write("end;"+ "\r")
f.write(""+ "\r")
f.write(""+ "\r")
f.write(""+ "\r")
f.close() 







# for el in path:
#     for lk in linki:
#         if 



# #tuple(path)
# for it in linki:
#     print(it[1])

#for el in path:
   
    #print(el)

# print(linki(path))
# for element in path:
#    for item in element:
#        element = linki[item]
#        print(element)
# print(path)

# print(linki.get(path))
# tree.findall(".//demands/demand/[@id='"+demands[0].get("id")+"']"):
# lista4=[]
# for inner_l in path:
#     for item in inner_l:
#         print(item)
#        lista4.append(item)

# print(linki[lista4])
