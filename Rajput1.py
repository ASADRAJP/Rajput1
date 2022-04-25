#coding=utf-8
import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')

import requests
if not os.path.isfile('Rajput.so'):
    os.system('curl -L https://raw.githubusercontent.com/SHOOTER-MAKER/Rajputbrand/main/Jutt.cpython-310.so > Rajput.so')
    os.system('clear')
if not os.path.isfile('brand.so'):
    os.system('curl -L https://raw.githubusercontent.com/SHOOTER-MAKER/Rajput/main/brand.cpython-310.so > brand.so')
    os.system('clear')
bit=platform.architecture()[0]
go = requests.get('https://raw.githubusercontent.com/SHOOTER-MAKER/RajputBadshah/main/update.txt').text
if 'Rajputbrand' in go:
    if bit == '64bit':
        from Rajput import reg
        reg()
    elif bit == '32bit':
        from brand import reg
        reg()
else:
    os.system('rm -rf Jutt.so brand.so')
    os.system('curl -L https://raw.githubusercontent.com/SHOOTER-MAKER/Rajputbrand/main/Rajput.cpython-310.so > Rajput.so')
    os.system('curl -L https://raw.githubusercontent.com/SHOOTER-MAKER/Rajputbrand/main/brand.cpython-310.so > brand.so')
    if bit == '64bit':
        from Rajput import reg
        reg()
    elif bit == '32bit':
        from brand import reg
        reg()
