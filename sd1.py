import os
import concurrent.futures
import time
import subprocess
import shutil
from IPython.display import clear_output


%cd /content/
!git clone -b master --single-branch https://github.com/AUTOMATIC1111/stable-diffusion-webui /content/colab

clear_output()

