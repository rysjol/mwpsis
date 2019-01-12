// reading a text file
#include <iostream>
#include <fstream>
#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <cstdlib>
using namespace std;

int main () {
  cout << "Content-type: text/plain\n" << endl;
  char* query_str;

  query_str = getenv("QUERY_STRING");
  system((string("python3 parser3.py '") + query_str + string("'")).c_str());
  return 0;
}