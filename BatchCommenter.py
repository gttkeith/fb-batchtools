from core import cm,btoolsinit
btoolsinit.init()

from core import btoolsfile,fbauth,fbio

print "\nBATCH COMMENTER\nComment on multiple posts at the same time\n"
fbauth.begin()

btoolsfile.import_ids_txt()
btoolsfile.import_content_txt("batch comment")

print "\nCommenting..."
for object_id in btoolsfile.targetids:
    fbio.fb_interact(fbio.put_imported_comment,object_id)
    fbio.remove_from_workingids(object_id)
    if len(fbio.workingids) > 1:
        print "%s IDs remaining."%len(fbio.workingids)
    elif len(fbio.workingids) > 0:
        print "%s ID remaining."%len(fbio.workingids)

print "Batch comments posted!"
cm.exexc(None,None)