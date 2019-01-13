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
minimize z: sum{e in E, d in D, p in P} (KSI[e]*LAM[e,d,p]*x[d,p] + KSA[e]*LAM[e,d,p]*x[d,p])  + 
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

/*Macierz delta (mowi ktore linki wchodza w sklad jakich sciezek) id_link, zapotrzebowanie, id_path) */
param : LAM :=12, 1, 1 118, 1, 1 12, 1, 1 16, 1, 1 110, 1, 2 111, 1, 2 11, 1, 2 12, 1, 2 16, 1, 2 112, 1, 3 113, 1, 3 11, 1, 3 12, 1, 3 16, 1, 3 112, 1, 4 118, 1, 4 11, 1, 4 15, 1, 4 13, 1, 4 16, 1, 4 112, 1, 5 118, 1, 5 12, 1, 5 13, 1, 5 14, 1, 5 116, 1, 5 110, 1, 6 17, 1, 6 18, 1, 6 114, 1, 6 11, 1, 6 12, 1, 6 16, 1, 6 110, 1, 7 111, 1, 7 15, 1, 7 13, 1, 7 16, 1, 7 1;param P_count := 7; /*liczba sciezek*/param h := 1 1 ;/* Kilometry per link */
param : KSI :=
1 156
2 272
3 156
4 186
5 272
6 237
7 208
8 181
9 208
10 250
11 324
12 324
13 250
14 165
15 305
16 142
17 195
18 294
;

/* Oplata za Autobahn */
param : KSA :=
1 1000
2 1000
3 0
4 0
5 0
6 1000
7 0
8 0
9 0
10 1000
11 1
12 0
13 1
14 0
15 1
16 0
17 0
18 1000
;

end;

