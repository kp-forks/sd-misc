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

subprocess.run(f'git clone -b master --single-branch https://github.com/AUTOMATIC1111/stable-diffusion-webui {params["sd_dir"]}',shell=True)

