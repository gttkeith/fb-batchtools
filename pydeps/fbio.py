import sys
import json
import ast
import time
import cm
import facebook
import fbauth
import btoolsfile

global workingids

def id_check(obj_id):
	global workingids
	try:
                fbauth.check_auth(fbauth.access_token)
		fbauth.graph.get_object("%s"%obj_id)
	except:
		print "An error occured. If it's a Facebook Graph error, please check your IDs and connection!"
                cm.empty_file("%s/IDs.txt"%cm.resume_dir)
                resume_ids_obj=open("%s/IDs.txt"%cm.resume_dir,'a') 
		for bak in workingids:
			resume_ids_obj.write("%s\n"%bak)
		resume_ids_obj.close()
		print "Current progress has been saved; restart the program to resume."
		cm.keypress_exit("%r"%sys.exc_info()[0])

def remove_from_workingids(obj_id):
        global workingids
        workingids[:] = [item for item in workingids if item != obj_id]

def debug_interact(calledfunc,obj_id):
        time.sleep(0.5)
        ret=calledfunc(obj_id)
        print ret
        return ret

def fb_interact(calledfunc,obj_id):
        complete=False
        time.sleep(0.5)
        while complete == False:
                try:
                        ret=calledfunc(obj_id)
                        complete=True
                        return ret
                except:
                        print "Exception: ",sys.exc_info()[0]
                        id_check(obj_id)

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
        field_args={'fields':'id,from,message','limit':'500000'}
        # TODO: try to remove this limit 50000 thingy...and add pagination support!
        comments=fbauth.graph.get_connections("%s"%obj_id,connection_name='comments',**field_args)
        comments=ast.literal_eval(json.dumps(comments))
        comments_data=comments['data']
        return comments_data

def post_imported_comment(obj_id):
        fbauth.graph.put_comment(object_id=obj_id,message=btoolsfile.imported_content)
        print "Comment posted on: %s"%obj_id
