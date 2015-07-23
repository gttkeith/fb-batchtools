import cm

global parentscript_action

def ids_txt():
    print "Reading IDs..."
    targetids=[]
    targetids_obj=open("./UserImport/IDs.txt",'r')
    targetids_raw=targetids_obj.readlines()
    targetids_obj.close()
    # TO-DO: check if targetids are possibly invalid and if so, show a warning.
    for x_raw in targetids_raw:
        if x_raw[-1:] is "\n":
            x=x_raw[0:-1]
            targetids.append(x)
        else:
            targetids.append(x_raw)
    num_targetids=len(targetids)
    if num_targetids is 1:
        print "%d ID detected.\n"%num_targetids
    else:
        print "%d IDs detected.\n"%num_targetids
    return targetids

def content_txt():
    imported_content_obj=open("./UserImport/Content.txt",'r')
    imported_content=imported_content_obj.read()
    imported_content_obj.close()
    print "Content:"
    print imported_content
    print "\nDo you wish to %s using this content? Press ENTER to continue, or fill in your new content and press ENTER to change it."%parentscript_action
    choice=cm.raw_input_lb("> ")
    if choice is "":
        return imported_content
    else:
        tbw_obj=open("./UserImport/Content.txt",'w')
        tbw_obj.write(choice)
        tbw_obj.close()
        content_txt()
