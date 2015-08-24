import cm
import os
import sys

def init():
    cm.ensure_dir("%s"%cm.work_dir)
    cm.ensure_dir("%s"%cm.cfg_dir)
    cm.ensure_dir("%s"%cm.export_dir)
    cm.ensure_dir("%s"%cm.resume_dir)

    cm.ensure_file("%s/Content.txt"%cm.work_dir)
    cm.ensure_file("%s/IDs.txt"%cm.work_dir)

    cm.ensure_file("%s/access_token"%cm.cfg_dir)

    cm.ensure_file("%s/IDs.txt"%cm.resume_dir)

    resumecheck_obj=open("%s/IDs.txt"%cm.resume_dir,'r')
    resumecheck=resumecheck_obj.read()
    resumecheck_obj.close()
    if resumecheck == '':
        cm.active_dir = cm.work_dir
    else:
        print "Data from last session was found. Resume session?\nType Y to continue, or anything else to discard and start a new session."
        choice=cm.raw_input_lb("> ")
        if choice is "Y":
            cm.active_dir = cm.resume_dir
        else:
            cm.active_dir = cm.work_dir
            tbe_obj=open("%s/IDs.txt"%cm.resume_dir,'w')
            tbe_obj.close()
