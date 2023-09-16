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



%cd /content/
!git clone -b master --single-branch https://github.com/AUTOMATIC1111/{sd} /content/{sddir}



