from os.path import exists
import cm
import fbio

global active_file_obj

def import_ids_txt():
    global targetids
    targetids=[]
    targetids_obj=open("%s/IDs.txt"%cm.active_dir,'r')
    targetids_raw=targetids_obj.readlines()
    targetids_obj.close()
    # TO-DO: check if targetids are possibly invalid and if so, show a warning.
    for x_raw in targetids_raw:
        if x_raw[-1:] is """
""":
            x=x_raw[0:-1]
            targetids.append(x)
        else:
            targetids.append(x_raw)
    rem_dect=""
    if cm.active_dir == cm.resume_dir:
        print "Resuming from previous session..."
        rem_dect=" remaining"
        cm.empty_file("%s/IDs.txt"%cm.active_dir)
    num_targetids=len(targetids)
    if num_targetids is 1:
        print "%d%s ID detected.\n"%(num_targetids,rem_dect)
    else:
        print "%d%s IDs detected.\n"%(num_targetids,rem_dect)
    fbio.workingids=targetids[:]

def import_content_txt(action):
    global imported_content
    imported_content_obj=open("%s/Content.txt"%cm.work_dir,'r')
    imported_content=imported_content_obj.read()
    imported_content_obj.close()
    print "Content:"
    print imported_content
    print "\nDo you wish to %s using this content? Press ENTER to continue, or fill in your new content and press ENTER to change it."%action
    choice=cm.raw_input_lb("> ")
    if choice is "":
        return imported_content
    else:
        tbw_obj=open("%s/Content.txt"%cm.work_dir,'w')
        tbw_obj.write(choice)
        tbw_obj.close()
        import_content_txt(action)

def csv_write_line(*args):
    newline=True
    to_be_written=""
    for item in args:
        item_sanitised=item.replace('"',"\'\'").replace("\n"," // ")
        if newline == True:
            to_be_written+=str("\"")
            newline=False
        else:
            to_be_written+=str(",\"")
        to_be_written+=str(item_sanitised)
	to_be_written+=str("\"")
    active_file_obj.write(to_be_written)
    active_file_obj.write("\n")
