import os
import sys
import subprocess


params={}
for arg in sys.argv[1:]:
 if arg.startswith('--'):
  key_value=arg[len('--'):].split('=')
  if len(key_value)==2:
   key,value=key_value
   params[key]=value

if(params['ckpt_url']):
      subprocess.run(f'aria2c --console-log-level=error -c -x 16 -s 16 -k 1M -d {params["ckpt_dir"]} {params["ckpt_url"]}',shell=True)

full_precision_str="--share --lowram --no-half-vae --disable-safe-unpickle --disable-console-progressbars --xformers --enable-insecure-extension-access --opt-sub-quad-attention --opt-channelslast --api"
#full_precision_str="--share --lowram --disable-safe-unpickle  --disable-console-progressbars --xformers --enable-insecure-extension-access --precision full --no-half --no-half-vae --opt-sub-quad-attention --opt-channelslast --api"

full_precision_str+=" --theme='dark'"

os.chdir(f'{params["sd_dir"]}')
subprocess.run(f"python launch.py {full_precision_str} --ui-settings-file {params['uiconfig_dir']} --styles-file {params['style_dir']} --lora-dir {params['lora_dir']} --ckpt-dir {params['ckpt_dir']} --ui-config-file {params['config_dir']}",shell=True)
