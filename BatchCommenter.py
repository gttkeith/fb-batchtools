import facebook
from pydeps import cm
from pydeps import fbauth
from pydeps import pkimport

pkimport.parentscript_action = "send your batch comments"

# and here we go!
print """BATCH COMMENTER v0.1
Comment on multiple posts at the same time
Place your content into Content.txt and list of target IDs into IDs.txt!
"""
graph=fbauth.authenticate()

# import IDs and content
targetids=pkimport.ids_txt()
imported_content=pkimport.content_txt()

print "\nCommenting..."
for x in targetids:
    graph.put_comment(object_id=x,message=imported_content)

print "Done.\n\n"
    
print "Batch comments posted!"
