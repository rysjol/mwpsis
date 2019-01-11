// reading a text file
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main () {
  cout << "Content-type: text/html\n" << endl;
  cout << "1" << endl;
  string line;
  ifstream myfile ("index.html");
  if (myfile.is_open())
  {
  	cout << "2" << endl;
    while ( getline (myfile,line) )
    {
      cout << line << '\n';
    }
    myfile.close();
  }

  else cout << "Unable to open file"; 

  return 0;
}