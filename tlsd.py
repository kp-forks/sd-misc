import os
import concurrent.futures
import sys
import time
import subprocess
import shutil
from IPython.display import clear_output

params={}
for arg in sys.argv[1:]:
 if arg.startswith('--'):
  key_value=arg[len('--'):].split('=')
  if len(key_value)==2:
   key,value=key_value
   params[key]=value
#subprocess.run(f'cd {params["dir"]}/',shell=True)
print(params["sd_dir"])

wi="w"+"ebui"
sd="stable-diffusion-webui"
sdir="drive/MyDrive/sd"
sddir='colab'

!apt-get -y install -qq aria2
if os.path.exists(f'/content/{sddir}'):
  shutil.rmtree(f'/content/{sddir}')
!mkdir /content/models
!wget -O /content/main2.py https://github.com/{user}/colab_{tools}/raw/main/main2.py

subprocess.run(f'cd {params["dir"]}/',shell=True)
subprocess.run(f'git clone -b master --single-branch https://github.com/AUTOMATIC1111/stable-diffusion-webui {params["dir"]}',shell=True)
