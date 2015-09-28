import os,sys,site,importlib,pip,cm

def init():
    # Check for dependencies
    depens = ("facebook",)
    for pak in depens:
        try:
            importlib.import_module(pak)
        except ImportError:
            print "\"%s\" not found. Installing..."%pak
            pip.main(['install',pak])
            print "Installed."
        finally:
            reload(site)
            globals()[pak] = importlib.import_module(pak)

    # Ensure FS dirs are present
    cm.ensure_dir("%s"%cm.work_dir)
    cm.ensure_dir("%s"%cm.cfg_dir)
    cm.ensure_dir("%s"%cm.export_dir)
    cm.ensure_dir("%s"%cm.resume_dir)

    cm.ensure_file("%s/Content.txt"%cm.work_dir)
    cm.ensure_file("%s/IDs.txt"%cm.work_dir)

    cm.ensure_file("%s/access_token"%cm.cfg_dir)

    cm.ensure_file("%s/IDs.txt"%cm.resume_dir)

    # Check for resume files
    resumecheck_obj=open("%s/IDs.txt"%cm.resume_dir,'r')
    resumecheck=resumecheck_obj.read()
    resumecheck_obj.close()
    if resumecheck == '':
        cm.active_dir = cm.work_dir
    else:
        print "Data from last session was found. Resume session?\nType Y to continue, or anything else to discard and start a new session."
        choice=str(cm.raw_input_lb("> ")).lower().find("y")
        if choice != -1:
            print "Resuming..."
            cm.active_dir = cm.resume_dir
        else:
            print "Resume canceled."
            cm.active_dir = cm.work_dir
            cm.empty_file("%s/IDs.txt"%cm.resume_dir)
