#include <iostream>
#include <fstream>
#include <cstdlib>
#include <string>
#include <vector>
#include <sstream>

 
using namespace std;

vector <string> splitString(string lineToSplit)
{
 string buf; // Have a buffer string
 stringstream ss(lineToSplit ); // Insert the string into a stream
 
 vector<string> tokens; // Create vector to hold our words
 
 while (ss >> buf)
 tokens.push_back(buf);
 
 /// ForDebuging
 /*for (int i=0; i < tokens.size(); i++) {
 cout << i << " " << tokens[i] << endl;
 }*/
 return tokens;
}
 
int main()
{
    string linia;
    fstream plik;

    int e=4;
    int d=5;

    //trasa Bialystok-Wroclaw
    string trasa[e][d][4];

 
    plik.open("plik.txt", ios::in);

    if(plik.good() == true)
    {
        while(!plik.eof())
        {
            getline(plik, linia);
            vector <string> tokens = splitString(linia);    
            for (int i=0; i < tokens.size(); i++) {
            //cout << i << " " << trasa[e][d][4] << endl;
            trasa[0][0][0] = tokens[i];
            cout << trasa[0][0][0] << endl;

 }
        }
        plik.close();

       
    }

    /*int e=4;
    int d=5;

    int trasa[e][d][4]*/


 
    system("PAUSE");
    return(0);
}