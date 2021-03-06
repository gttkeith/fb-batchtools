import os
import sys
import traceback
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


def raw_input_lb(txt):
    out=raw_input(txt)
    print " "
    return out

def boolfix_dict_eval(target_rawstr):
    if target_rawstr[0] is "{" and target_rawstr[-1] is "}":
        try:
            target_rawstr=target_rawstr.replace(": true",": True").replace(":true",":True")
            target_rawstr=target_rawstr.replace(": false",": False").replace(":false",":False")
            output=eval(target_rawstr)
            return output
        except:
            exexc("unexpected retrieved string input",None)

def dict_to_datalist(target_dict,*args):
    ret_list = []
    for item in args:
        if type(item) is list:
            ret_list.extend(item)
        else:
            try:
                data_item=target_dict[item]
                ret_list.append(data_item)
            except:
                ret_list.append("(unknown \'%s\')"%item)
    return ret_list

def exexc(cause,subsequent):
    if cause != None:
        print "\nException: %s."%cause.lower()
    if subsequent != None:
        print "\n** PRESS RETURN TO %s **"%subsequent.upper()
    else:
        print "\n** PRESS RETURN TO EXIT **"
    input = raw_input()
    if input == "traceback" and cause != "":
        print traceback.format_exc()
        raw_input("\n** END TRACEBACK **")
    if subsequent == None:
        exit(0)
