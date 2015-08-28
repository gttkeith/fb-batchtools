from core import cm,btoolsinit,btoolsfile,fbauth,fbio

btoolsinit.init()

print "LIKE ALL COMMENTS v0.1\nLikes all comments on selected posts\n"

fbauth.begin()
btoolsfile.import_ids_txt()

print "\nCommenting..."
for object_id in btoolsfile.targetids:
    comments_count=0
    comments_data=fbio.fb_interact(fbio.get_comments,object_id)
    for comment in comments_data:
        comment_id=comment.get("id")
        fbio.fb_interact(fbio.put_like,comment_id)
        comments_count+=1
    fbio.remove_from_workingids(object_id)
    if len(fbio.workingids) > 1:
        print "%s comment(s) liked; %s IDs remaining."%(comments_count,len(fbio.workingids))
    elif len(fbio.workingids) > 0:
        print "%s comment(s) liked; %s ID remaining."%(comments_count,len(fbio.workingids))
    
print "Comments liked!"
cm.keypress_exit("")
