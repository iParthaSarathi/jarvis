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
[create a folder for jarvis it will create  its own data for every user to remember things]
cd foldername  
python jarvis.py  
or  
use  curl -L https://github.com/iParthaSarathi/jarvis | tar zx 
cd jarvis
python jarvis.py
