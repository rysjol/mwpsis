# cbc daryLosu.mod% -solve -solu out.xml
# MPSiS 2018/2019
# Model UFAP, P/L

/* Number of vertexes, edges, dispositions */
param P_count, integer, >= 0;    #wierzcholki-miasta
param E_count, integer, >= 0;    #krawedzie-drogi
param D_count, integer, >= 0;    #zapotrzebowanie
param K_count, integer, >= 0;    #moduly-pojazdy

/* Sets of vertexes, edges and dispositions */
set P, default {1..P_count};
set E, default {1..E_count};
set D, default {1..D_count};
set K, default {1..K_count};    #modularnosc

/* Requirements */
param h{d in D} >= 0;
param LAM{e in E, d in D, p in P} >= 0, default 0;
param m{k in K} >= 0;    #rozmiar pojazdu
param g{k in K} >= 0;    #koszt wykorzystania danego pojazdu

/* Capacity */
#param c{e in E} >= 0, default 10;

/* KSI xD */
param KSI{e in E} >= 0;

/* KSA xD */
param KSA{e in E} >= 0;

/* Decision variables */
var x{d in D, p in P}, >= 0;
var f{e in E,k in K}, integer, >= 0;    #modularnosc

/* Objective function 'z' */
minimize z: sum{e in E, d in D, p in P} (KSI[e]*LAM[e,d,p]*x[d,p]*4.95*10/100 + KSA[e]*LAM[e,d,p]*x[d,p])  + 
sum{e in E, k in K} g[k]*f[e,k];

/* Constraints */
#s.t. c1{e in E} : c[e] >= sum{p in P, d in D} LAM[e,d,p]*x[d,p];
s.t. c2{d in D} : h[d] == sum{p in P} x[d,p];
s.t. c3{d in D} : sum{p in P} x[d,p] <= sum{e in E,k in K} m[k]*f[e,k];

/* Input data */
data;

param E_count := 18; /*liczba krawedzi*/
param D_count := 1; /*liczba zapotrzebowan*/
param K_count := 3;

/*wartosci zapotrzebowan, po 10 dla pierwszego i drugiego*/
#rozmiar pojazdu
param : m :=
 1    1
 2    10
 3    13
; 
#koszt wykorzystania danego pojazdu
param : g :=
 1    2
 2    10
 3    15
;
#ilość ładunków
param : h :=
 1      24
;
/*Macierz delta (mowi ktore linki wchodza w sklad jakich sciezek) id_link, zapotrzebowanie, id_path) */
param : LAM :=
18, 1, 1 112, 1, 1 110, 1, 1 17, 1, 1 18, 1, 1 11, 1, 2 114, 1, 2 118, 1, 3 113, 1, 3 114, 1, 3 118, 1, 4 112, 1, 4 110, 1, 4 111, 1, 4 114, 1, 4 118, 1, 5 112, 1, 5 110, 1, 5 17, 1, 5 19, 1, 5 115, 1, 5 12, 1, 6 13, 1, 6 15, 1, 6 114, 1, 6 11, 1, 7 111, 1, 7 17, 1, 7 18, 1, 7 1;param P_count := 7; /*liczba sciezek*//* Kilometry per link */
param : KSI :=
1 340
2 234
3 239
4 140
5 272
6 163
7 81
8 199
9 194
10 167
11 293
12 416
13 198
14 163
15 217
16 245
17 195
18 393
;

/* Oplata za Autobahn */
param : KSA :=
1 1000
2 0
3 0
4 0
5 1000
6 0
7 1000
8 0
9 1000
10 1000
11 0
12 0
13 0
14 0
15 0
16 0
17 0
18 1000
;

end;


