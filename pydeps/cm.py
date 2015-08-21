import os
import sys
from os.path import expanduser

global usr_home
usr_home = expanduser("~")
global active_dir
global work_dir
work_dir = "%s/Documents/fb-batchtools"%usr_home
global cfg_dir
cfg_dir = "%s/cfg"%work_dir
global resume_dir
resume_dir = "%s/resume"%work_dir
global export_dir
export_dir = "%s/export"%work_dir

def raw_input_lb(txt):
    out=raw_input(txt)
    print " "
    return out

def keypress_exit(error):
    if error != "":
        print "Error: ",error
    raw_input("\n** PRESS ANY KEY TO EXIT **")
    exit(0)

def ensure_dir(x):
    if not os.path.exists(x):
        os.makedirs(x)

def ensure_file(x):
    if not os.path.exists(x):
        touch=open(x,'w')
        touch.close

def empty_file(filen):
    tbe_obj=open(filen,'w')
    tbe_obj.close()
