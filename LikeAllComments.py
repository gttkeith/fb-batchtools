from core import cm,btoolsinit
btoolsinit.init()

from core import btoolsfile,fbauth,fbio

print "LIKE ALL COMMENTS v0.1\nLikes all comments on selected posts\n"

fbauth.begin()
btoolsfile.import_ids_txt()

print "\nLiking comments..."
for object_id in btoolsfile.targetids:
    comments_count=0
    comment_s = ""
    comments_data=fbio.fb_interact(fbio.get_comments,object_id)
    for comment in comments_data:
        comment_id=comment.get("id")
        fbio.fb_interact(fbio.put_like,comment_id)
        comments_count+=1
    fbio.remove_from_workingids(object_id)
    if comments_count != 1:
        comment_s = "s"
    if len(fbio.workingids) > 1:
        print "%s comment%s liked; %s IDs remaining."%(comments_count,comment_s,len(fbio.workingids))
    elif len(fbio.workingids) == 1:
        print "%s comment%s liked; 1 ID remaining."%(comments_count,comment_s)
    else:
        print "%s comment%s liked."%(comments_count,comment_s)
        
print "All comments liked!"
cm.keypress_exit("")
