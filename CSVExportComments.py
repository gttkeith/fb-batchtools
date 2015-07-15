import facebook
import json
import ast
from os.path import exists
from prpy import cm
from prpy import fbauth

csv_check=exists("comments.csv")

global comments
global post_id
global post_accessible
post_accessible=False

# and here we go!
print "COMMENT FETCHER v0.1\n"
graph=fbauth.authenticate()

# what's the post?
post_id=cm.raw_input_lb("What's the ID of the post you'd like to fetch?\n> ")

# verify that FB post ID isn't bogus
while post_accessible is False:
    try:
        print "Fetching comments from Facebook..."
        field_args={'fields':'id,from.name,message','limit':'50000'}
        # TODO: try to remove this limit 50000 thingy...and add pagination support!
        comments=graph.get_connections("%s"%post_id,connection_name='comments',**field_args)
        post_accessible=True
    except facebook.GraphAPIError:
        print """Post ID invalid.\nAre you sure that it's the correct ID? The post ID is a long number, just before the end of the post URL."""
        post_id=raw_input("Paste your valid post ID here:\n> ")
    
# make it into a pretty dict for processing
comments=ast.literal_eval(json.dumps(comments))
comments_data=comments['data']

print "Done.\n"

# lambs to the slaughter
print "Writing to file..."
global tbw_obj
tbw_obj=open("comments.csv",'w')
tbw_obj.truncate()
tbw_obj.write("Name,User ID,Comment,Comment ID,\n")

# write till we drop
for x in comments_data:
    x_from=x['from']
    ac_name=x_from['name']
    ac_userid=x_from['id']
    ac_message=x['message']
    # input santisation in progress!
    ac_message=ac_message.replace("\n"," ")
    ac_message=ac_message.replace('"'," ")
    ac_postid=x['id']
    tbw_obj.write("\"%s\",\"%s\",\"%s\",\"%s\"\n"%(ac_name,ac_userid,ac_message,ac_postid))
    
tbw_obj.close()
    
print "Export complete!"
