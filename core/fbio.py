import sys
import json
import time
import cm
import facebook
import fbauth
import btoolsfile

global workingids

def io_exception(obj_id):
	global workingids
        fbauth.check_auth()
        print "An error occured. If it's a not an authentication error, please check your IDs and connection!"
        cm.empty_file("%s/IDs.txt"%cm.resume_dir)
        resume_ids_obj=open("%s/IDs.txt"%cm.resume_dir,'a') 
        for bak in workingids:
                resume_ids_obj.write("%s\n"%bak)
        resume_ids_obj.close()
        print "Current progress has been saved; restart the program to resume."
        cm.keypress_exit_traceback()

def remove_from_workingids(obj_id):
        global workingids
        workingids[:] = [item for item in workingids if item != obj_id]

def debug_interact(calledfunc,obj_id):
        time.sleep(2)
        ret=calledfunc(obj_id)
        print ret
        return ret

def fb_interact(calledfunc,obj_id):
        complete=False
        time.sleep(2)
        while complete == False:
                try:
                        ret=calledfunc(obj_id)
                        complete=True
                        return ret
                except:
                        print "Exception: ",sys.exc_info()[0]
                        io_exception(obj_id)

def get_post(obj_id):
        content=fbauth.graph.get_object("%s"%obj_id)
        if content.get("message") != None:
                ret=content.get("message")
        elif content.get("story") != None:
                ret=content.get("story")
        elif content.get("name") != None:
                ret=content.get("name")
        else:
                ret="(unknown content)"
        ret=ret.encode("utf-8")
        return ret
        
def get_comments(obj_id):
        field_args={'limit':'500000'}
        # TODO: try to remove this limit 50000 thingy...and add pagination support!
        comments=fbauth.graph.get_connections("%s"%obj_id,connection_name='comments',**field_args)
        comments_rawdict=json.dumps(comments)
        comments_dict=cm.boolfix_dict_eval(comments_rawdict.encode("utf-8"))
        comments_data=comments_dict["data"]
        return comments_data

def put_imported_comment(obj_id):
        fbauth.graph.put_comment(object_id=obj_id,message=btoolsfile.imported_content)
        print "Comment posted on: %s"%obj_id

def put_like(obj_id):
        fbauth.graph.put_like("%s"%obj_id)
        print "Liked: %s"%obj_id
