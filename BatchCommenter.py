from pydeps import cm
from pydeps import btoolsinit
from pydeps import fbauth
from pydeps import fbio
from pydeps import btoolsfile

btoolsinit.init()

# and here we go!
print """BATCH COMMENTER v0.1
Comment on multiple posts at the same time.
"""
fbauth.begin()

fbio.workingids=btoolsfile.import_ids_txt()
btoolsfile.import_content_txt("batch comment")

print "\nCommenting..."
for object_id in btoolsfile.targetids:
    fbio.debug_interact(fbio.post_imported_comment,object_id)
    fbio.remove_from_workingids(object_id)
    if len(fbio.workingids) > 1:
        print "%s IDs remaining."%len(fbio.workingids)
    elif len(fbio.workingids) > 0:
        print "%s ID remaining."%len(fbio.workingids)

print "Batch comments posted!"
cm.keypress_exit("")
