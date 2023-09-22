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

subprocess.run("apt install libunwind8-dev -yqq",shell=True) 
os.environ["LD_PRELOAD"]="libtcmalloc.so.4"
os.environ["TF_CPP_MIN_LOG_LEVEL"]="3"
subprocess.run("apt install sox ffmpeg libcairo2 libcairo2-dev",shell=True)
subprocess.run("pip install -q xformers==0.0.20 triton==2.0.0 -U",shell=True) 
