import os
from os.path import expanduser

global usr_home
usr_home = expanduser("~")

def raw_input_lb(txt):
    out=raw_input(txt)
    print " "
    return out

def ensure_dir(x):
    if not os.path.exists(x):
        os.makedirs(x)

def ensure_file(x):
    if not os.path.exists(x):
        touch=open(x,'w')
        touch.close

def init():
    ensure_dir("%s/Documents/fb-powerkit"%usr_home)
    ensure_dir("%s/Documents/fb-powerkit/cfg"%usr_home)
    ensure_file("%s/Documents/fb-powerkit/cfg/access_token"%usr_home)
    
    ensure_file("%s/Documents/fb-powerkit/Content.txt"%usr_home)
    ensure_file("%s/Documents/fb-powerkit/IDs.txt"%usr_home)
