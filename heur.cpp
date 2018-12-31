#include <fstream> 
#include <stdio.h> 
#include <iostream>

using namespace std;
int partition(int tablica[], int p, int r){
	int x=tablica[p];
	int i = p, j=r, w;
	while(true){
		while(tablica[j]>x)
			j--;
		while(tablica[i]<x)
			i++;
		if(i<j)
		{
			w=tablica[i];
			tablica[i]=tablica[j];
			tablica[j]=w;
			i++;
			j--;
		}
		else
			return j;
	}
}

void quicksort(int tablica[], int p, int r){
	int q;
	if (p<r)
	{
		q=partition(tablica,p,r);
		quicksort(tablica,p,q);
		quicksort(tablica,q+1,r);

	}
}
int main (){
	int e=4;
	int d=5;

	//trasa Bialystok-Wroclaw
    int trasa[e][d][4] = {
    	{{18,1,1,1},{2,1,1,1},{3,1,1,1},{4,1,1,1},{17,1,1,1}},
    	{{12,1,2,1},{10,1,2,1},{7,1,2,1},{9,1,2,1},{0,0,2,0}},
    	{{18,1,3,1},{1,1,3,1},{11,1,3,1},{7,1,3,1},{9,1,3,1}},
    	{{18,1,4,1},{2,1,4,1},{6,1,4,1},{16,1,4,1},{17,1,4,1}}
	};

	int KSI[18] =  {
		156,
		272,
		156,
		186,
		272,
		237,
		208,
		181,
		208,
		250,
		324,
		324,
		250,
		165,
		305,
		142,
		195,
		294
	};
	int KSA[18] = {
 1000,
 1000,
 0,
 0,
 0,
 1000,
 0,
 0,
 0,
 1000,
 1,
 0,
 1,
 0,
 1,
 0,
 0,
 1000
};
	int dlugosc=0;
	int suma[e];
	int x;

	/*for (int i=0; i<e; i++){
		for(int j=0; j<d; j++){
		dlugosc += KSI[x-1]*trasa[i][j][0];	
		}
	}*/

		for (int i=0; i<e; i++){
			suma[i] = 0;
			for(int j=0; j<d; j++){
				x=trasa[i][j][0];
				dlugosc = KSI[x-1]*trasa[i][j][1]+KSA[x-1]*trasa[i][j][1];
				suma[i]+=dlugosc;
				//cout << dlugosc << endl;
				//cout << x << endl;
			//cout<< trasa[0][i][0];
		}
		cout << suma[i] << endl;	
	}
quicksort(suma,0,e-1);
cout << endl;
//for (int i=0; i<e; i++){
cout << suma[0] << endl;
//}


    
    return 0;
};


