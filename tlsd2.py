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

full_precision_str = params['user_arguments'] + " --disable-safe-unpickle --xformers --enable-insecure-extension-access --opt-sub-quad-attention --opt-channelslast"
#full_precision_str="--share --lowram --disable-safe-unpickle  --disable-console-progressbars --xformers --enable-insecure-extension-access --precision full --no-half --no-half-vae --opt-sub-quad-attention --opt-channelslast"

full_precision_str+=" --theme='dark'"

os.chdir(f'{params["sd_dir"]}')
subprocess.run(f"python launch.py {full_precision_str} --ui-settings-file {params['config_dir']} --styles-file {params['style_dir']} --lora-dir {params['lora_dir']} --ckpt-dir {params['ckpt_dir']} --ui-config-file {params['uiconfig_dir']}",shell=True)
