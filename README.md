# mwpsis #

#### App starting ####
After cloning repo run in repo directory:
```bash
python3 -m http.server --cgi 8000
```
Next visit 'http://localhost:8000/cgi-bin/index.cgi' to run application.

Have fun!

#### C++ compilation ####
Go to project dir and next:
```bash
cd cgi-bin
g++ cgi.cpp -o index.cgi
g++ getids.cpp -o getids.cgi
```
