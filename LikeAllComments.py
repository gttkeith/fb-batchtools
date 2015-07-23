import json
import ast
import facebook
from pydeps import cm
from pydeps import fbauth

global comments
global post_id
global post_accessible
post_accessible=False

# and here we go!
print "LIKE ALL COMMENTS v0.1\nLikes all comments on a selected post\n"
graph=fbauth.authenticate()

# what's the post?
post_id=cm.raw_input_lb("What's the ID of the post you'd like to like all comments for?\n> ")

# verify that FB post ID isn't bogus
while post_accessible is False:
    try:
        print "Fetching comments from Facebook..."
        field_args={'fields':'id,from.name,message','limit':'50000'}
        # REMINDER: try to remove this limit 50000 thingy...and add pagination support!
        comments=graph.get_connections("%s"%post_id,connection_name='comments',**field_args)
        post_accessible=True
    except facebook.GraphAPIError:
        print """Post ID invalid.\nAre you sure that it's the correct ID? The post ID is a long number, just before the end of the post URL."""
        post_id=raw_input("Paste your valid post ID here:\n> ")
    
# make it into a pretty dict for processing
comments=ast.literal_eval(json.dumps(comments))
comments_data=comments['data']

print "Done.\n\nLiking all comments..."

# like till we drop
for x in comments_data:
    x_id=x['id']
    graph.put_like("%s"%x_id)
    
print "All comments liked!"
