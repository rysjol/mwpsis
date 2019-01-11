// reading a text file
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main () {
  cout << "Content-type: text/html\n" << endl;
  string line;
  char* start_point;
  char* stop_point;
  ifstream myfile ("index.html");
  if (myfile.is_open())
  {
    while ( getline (myfile,line) )
    {
      cout << line << '\n';
    }
    myfile.close();
  }

  else cout << "Unable to open file";

  start_point = getenv("start");
  stop_point = getenv("stop");

  std::ofstream outfile ("test.txt");
  outfile << "test" << std::endl;
  outfile << "test2" << std::endl;
  outfile << start_point << std::endl;
  outfile << stop_point << std::endl;
  outfile.close();

  return 0;
}