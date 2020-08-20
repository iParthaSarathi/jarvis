# jarvis
#some command will work better in linux
----------------------------------------------------
install  
sudo apt update  
sudo apt -y upgrade  
python3 -V  
sudo apt install -y python3-pip  
sudo apt install -y python3-venv  
mkdir environments  
cd environments  
python3 -m venv my_env  
ls my_env  
source my_env/bin/activate  
  
 Module
--------------------------  
import pyttsx3 => pip install pyttsx3  
import time  
import json  
import os.path  
import wikipedia => pip install wikipedia  

[create a folder for jarvis it will create  its own data for every user to remember things]
cd foldername  
python jarvis.py  
or  
download  https://github.com/iParthaSarathi/jarvis/archive/master.zip   
cd folder_name  
python jarvis.py  

jarvis a simple command line assistant talk with him ,teach him , ask qustion , he will remember your name and the things you teach next time you say your name
 still accept simple command or use your coustom command by typing 'teach'  he will remember next time you enter same name  
=================================================================================
use commands like teach to teach jarvis
like your input=hi
jarvis reply='set a reply'
------------------------------
1)tell me about [anything]  
2)who are you  
3)who i am  
4)who create you    
5)run chrome/firefox/gedit/vscode  
6)imotional like i am sad /are you sad/are you hungry  
7)exit   
