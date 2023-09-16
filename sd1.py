#@title ## 1、加载谷歌云盘并初始化环境
import os
import concurrent.futures
import time
import subprocess
import shutil
from IPython.display import clear_output



sd0="sta"+"ble-di"
sd1="ffu"+"sion"
wi="w"+"ebui"
sd=f"{sd0}{sd1}-{wi}"
sdir="drive/MyDrive/sd"
sddir='colab'

from google.colab import drive
drive.mount('/content/drive')
!apt-get -y install -qq aria2
if os.path.exists(f'/content/{sddir}'):
  shutil.rmtree(f'/content/{sddir}')
!mkdir /content/models

%cd /content/
!git clone -b master --single-branch https://github.com/AUTOMATIC1111/{sd} /content/{sddir}

def run_git_download():
  start_time = time.time()
  %cd /content/{sddir}/extensions/
  #!git clone https://github.com/Physton/sd-{wi}-prompt-all-in-one /content/{sddir}/extensions/sd-{wi}-prompt-all-in-one
  #!git clone https://github.com/Mikubill/sd-{wi}-controlnet /content/{sddir}/extensions/sd-{wi}-controlnet
  #!git clone https://github.com/dtlnor/{sd}-localization-zh_CN /content/{sddir}/extensions/{sd}-localization-zh_CN
  #!git clone https://github.com/fkunn1326/openpose-editor /content/{sddir}/extensions/openpose-editor
  !git clone https://github.com/DominikDoom/a1111-sd-{wi}-tagcomplete /content/{sddir}/extensions/a1111-sd-{wi}-tagcomplete
  !git clone https://github.com/Coyote-A/ultimate-upscale-for-automatic1111 /content/{sddir}/extensions/ultimate-upscale
  #!git clone https://github.com/toriato/{sd}-wd14-tagger /content/{sddir}/extensions/{sd}-wd14-tagger
  #!git clone https://github.com/Scholar01/sd-{wi}-mov2mov /content/{sddir}/extensions/sd-{wi}-mov2mov
  #!git clone https://github.com/nonnonstop/sd-{wi}-3d-open-pose-editor /content/{sddir}/extensions/sd-{wi}-3d-open-pose-editor
  !git clone https://github.com/hako-mikan/sd-{wi}-lora-block-weight /content/{sddir}/extensions/sd-{wi}-lora-block-weight
  !git clone https://github.com/AIrjen/OneButtonPrompt /content/{sddir}/extensions/OneButtonPrompt
  #!git clone https://github.com/KohakuBlueleaf/a1111-sd-{wi}-lycoris /content/{sddir}/extensions/a1111-sd-{wi}-lycoris
  #!git clone https://github.com/Bing-su/adetailer /content/{sddir}/extensions/adetailer
  !git clone https://github.com/adieyal/sd-dynamic-prompts /content/{sddir}/extensions/sd-dynamic-prompts
  !git clone https://github.com/zanllp/sd-{wi}-infinite-image-browsing /content/{sddir}/extensions/sd-{wi}-infinite-image-browsing
  #!git clone https://github.com/civitai/sd_civitai_extension /content/{sddir}/extensions/sd_civitai_extension
  #!git clone https://github.com/butaixianran/{sd}-Civitai-Helper /content/{sddir}/extensions/{sd}-Civitai-Helper
  !git clone https://github.com/BlafKing/sd-civitai-browser-plus /content/{sddir}/extensions/sd-civitai-browser-plus

  !curl -Lo "/content/{sddir}/models/VAE/vae-ft-mse-840000-ema-pruned.safetensors" https://huggingface.co/stabilityai/sd-vae-ft-mse-original/resolve/main/vae-ft-mse-840000-ema-pruned.safetensors
  !curl -Lo "/content/{sddir}/models/VAE/kl-f8-anime2.ckpt" https://huggingface.co/hakurei/waifu-diffusion-v1-4/resolve/4c4f05104055c029ad577c18ac176462f0d1d7c1/vae/kl-f8-anime2.ckpt
  !curl -Lo "/content/{sddir}/models/VAE/animevae.pt" https://huggingface.co/swl-models/animvae/resolve/main/animevae.pt

  if os.path.exists(f'/content/{sddir}/embeddings'):
    shutil.rmtree(f'/content/{sddir}/embeddings')
  !git clone https://huggingface.co/nolanaatama/embeddings /content/{sddir}/embeddings

  end_time = time.time()
  print("已克隆git耗时：", end_time-start_time, "秒")

def run_aria2c_download():
  start_time = time.time()

  #!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M {download_url} -d {download_dir}

  #!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11e_sd15_ip2p_fp16.safetensors -d /content/{sd}/models/ControlNet -o control_v11e_sd15_ip2p.safetensors
  #!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11f1p_sd15_depth_fp16.safetensors -d /content/{sd}/models/ControlNet -o control_v11f1p_sd15_depth.safetensors
  #!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11p_sd15_canny_fp16.safetensors -d /content/{sd}/models/ControlNet -o control_v11p_sd15_canny.safetensors
  #!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11p_sd15_inpaint_fp16.safetensors -d /content/{sd}/models/ControlNet -o control_v11p_sd15_inpaint.safetensors
  #!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11p_sd15_lineart_fp16.safetensors -d /content/{sd}/models/ControlNet -o control_v11f1p_sd15_depth.safetensors
  #!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11p_sd15_mlsd_fp16.safetensors -d /content/{sd}/models/ControlNet -o control_v11p_sd15_mlsd.safetensors
  #!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11p_sd15_normalbae_fp16.safetensors -d /content/{sd}/models/ControlNet -o control_v11p_sd15_normalbae.safetensors
  #!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11p_sd15_openpose_fp16.safetensors -d /content/{sd}/models/ControlNet -o control_v11p_sd15_openpose.safetensors
  #!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11p_sd15_scribble_fp16.safetensors -d /content/{sd}/models/ControlNet -o control_v11p_sd15_scribble.safetensors
  #!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11p_sd15_seg_fp16.safetensors -d /content/{sd}/models/ControlNet -o control_v11p_sd15_seg.safetensors
  #!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11p_sd15_softedge_fp16.safetensors -d /content/{sd}/models/ControlNet -o control_v11p_sd15_softedge.safetensors
  #!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11p_sd15s2_lineart_anime_fp16.safetensors -d /content/{sd}/models/ControlNet -o control_v11p_sd15s2_lineart_anime.safetensors
  #!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11f1e_sd15_tile_fp16.safetensors -d /content/{sd}/models/ControlNet -o control_v11f1e_sd15_tile_fp16.safetensors
  !aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lokCX/4x-Ultrasharp/resolve/main/4x-UltraSharp.pth -d /content/{sddir}/models/ESRGAN/ -o 4x-UltraSharp.pth
  !aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/datasets/daasd/CN.csv/resolve/main/CN.csv -d /content/{sddir}/extensions/a1111-sd-{wi}-tagcomplete/tags -o CN.csv
  end_time = time.time()
  print("aria2c完成下载耗时：", end_time-start_time, "秒")

def wget_download():
  start_time = time.time()
  !apt install libunwind8-dev -yqq
  os.environ["LD_PRELOAD"] = "libtcmalloc.so.4"
  os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
  !sudo apt-get install sox ffmpeg libcairo2 libcairo2-dev
  end_time = time.time()
  print("wget完成下载耗时：", end_time-start_time,"秒")






def pip_download():
  start_time = time.time()
  !pip install xformers xformers==0.0.20
  end_time = time.time()
  print("pip完成下载耗时：", end_time-start_time,"秒")

executor = concurrent.futures.ThreadPoolExecutor(max_workers=4)
task1 = executor.submit(run_git_download)
task2 = executor.submit(run_aria2c_download)
task4 = executor.submit(wget_download)
task5 = executor.submit(pip_download)
concurrent.futures.wait([task1,task2,task4,task5])

%cd /content/{sddir}

#手机平板
css_content = '''
  @media screen and (max-width: 600px) {
    .gradio-slider input[type="range"]{
      display: none;
    }
    .gradio-slider input[type="number"]{
      width: 18em;
    }
  }
  '''
with open(f'/content/{sddir}/style.css', 'a') as cssFile:
      cssFile.write(css_content)



ngrok_auth="2SQXegeslmTVLpXDxqHU1DoCBPw_43axN9HrCsnBZTZokFPaA"

full_precision_str="--share --disable-safe-unpickle --disable-console-progressbars --xformers --enable-insecure-extension-access --opt-sub-quad-attention --opt-channelslast --api"
#full_precision_str="--share --lowram --disable-safe-unpickle  --disable-console-progressbars --xformers --enable-insecure-extension-access --precision full --no-half --no-half-vae --opt-sub-quad-attention --opt-channelslast --api"

full_precision_str+=" --theme='dark'"


if ngrok_auth:
  full_precision_str+=f"  --ngrok={ngrok_auth} --ngrok-region='auto'"




!python launch.py {full_precision_str} --ui-settings-file /content/drive/MyDrive/sd/config.json --styles-file /content/drive/MyDrive/sd/styles.csv --lora-dir /content/drive/MyDrive/sd/models/Lora --ckpt-dir /content/models --ui-config-file /content/drive/MyDrive/sd/ui-config.json --no-download-sd-model --exit
clear_output()
#!apt -y update -qq
#!apt -y upgrade -qq

#
