import os
import sys
from .app import *
from .inject import *
from .default import *

os.system('cls' if os.name == 'nt' else 'clear')
print(colors(''.join(open(real_path('/data/banners.txt')).readlines())))
if sys.version[0] == '2':
    log('Exception: Please use Python 3!', color='[R1]')
    sys.exit()
