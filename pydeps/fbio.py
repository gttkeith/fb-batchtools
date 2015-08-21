import json
import ast
import sys
import cm
import facebook
import fbauth
import pkfileops

global workingids

def id_check(x):
	global workingids
	try:
                fbauth.check_auth()
		fbauth.graph.get_object(x)
	except facebook.GraphAPIError:
		print "An error occured. Please check your IDs!"
                cm.empty_file("%s/IDs.txt"%cm.resume_dir)
                resume_ids_obj=open("%s/IDs.txt"%cm.resume_dir,'a') 
		for bak in workingids:
			resume_ids_obj.write("%s\n"%bak)
		resume_ids_obj.close()
		print "Current progress has been saved. Start the program again to resume!"
		cm.keypress_exit("%r"%sys.exc_info()[0])

def get_post(post_id):
	print "in progress"
	return "sample post content"

def get_post_comments(post_id):
	try:
                field_args={'fields':'id,from.name,message','limit':'500000'}
	    	# TODO: try to remove this limit 50000 thingy...and add pagination support!
	    	comments=fbauth.graph.get_connections("%s"%post_id,connection_name='comments',**field_args)
		comments=ast.literal_eval(json.dumps(comments))
		comments_data=comments['data']
		return comments_data
	except facebook.GraphAPIError:
		id_check(x)
