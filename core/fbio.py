import sys,time,json,cm,facebook,fbauth,btoolsfile

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
        cm.exexc(str(sys.exc_info()[0]),None)

def remove_from_workingids(obj_id):
        global workingids
        workingids[:] = [item for item in workingids if item != obj_id]           

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

def parse_fb_dict_input(raw_data):
        data_rawdict=json.dumps(raw_data)
        data_dict=cm.boolfix_dict_eval(data_rawdict.encode("utf-8"))
        parsed_data=data_dict.get("data")
        return parsed_data

def get_content(obj_id):
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
        # TODO: try to remove this limit 500000 thingy...and add pagination support!
        comments=fbauth.graph.get_connections("%s"%obj_id,connection_name='comments',**field_args)
        return parse_fb_dict_input(comments)

def get_insights(obj_id):
        field_args={'limit':'500000'}
        # TODO as above again
        data=fbauth.graph.get_connections("%s"%obj_id,connection_name='insights',**field_args)
        return parse_fb_dict_input(data)

def put_imported_comment(obj_id):
        fbauth.graph.put_comment(object_id=obj_id,message=btoolsfile.imported_content)
        print "Comment posted on: %s"%obj_id

def put_like(obj_id):
        fbauth.graph.put_like("%s"%obj_id)
        print "Liked: %s"%obj_id
