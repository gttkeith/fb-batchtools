from core import cm,btoolsinit,btoolsfile,fbauth,fbio

btoolsinit.init()

print "LIKE ALL COMMENTS v0.1\nLikes all comments on selected posts\n"

fbauth.begin()
btoolsfile.import_ids_txt()

print "\nCommenting..."
for object_id in btoolsfile.targetids:
    fbio.fb_interact(fbio.put_like,object_id)
    fbio.remove_from_workingids(object_id)
    if len(fbio.workingids) > 1:
        print "%s IDs remaining."%len(fbio.workingids)
    elif len(fbio.workingids) > 0:
        print "%s ID remaining."%len(fbio.workingids)
    
print "Comments liked!"
cm.keypress_exit("")
