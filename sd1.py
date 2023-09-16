import os
import concurrent.futures
import time
import subprocess
import shutil
from IPython.display import clear_output

from google.colab import drive
drive.mount('/content/drive')

%cd /content/
!git clone -b master --single-branch https://github.com/AUTOMATIC1111/stable-diffusion-webui /content/colab

clear_output()

