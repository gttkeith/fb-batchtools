from core import cm,btoolsinit,btoolsfile,fbauth,fbio

btoolsinit.init()

print "\nCOMMENT FETCHER v0.1\nExports all comments on selected posts into a CSV file\n"
fbauth.begin()

fbio.workingids=btoolsfile.import_ids_txt()

if cm.active_dir==cm.resume_dir:
    print "Appending to file..."
    btoolsfile.active_file_obj=open("%s/fb-comments.csv"%cm.export_dir,'a')
else:
    print "Writing to file..."
    btoolsfile.active_file_obj=open("%s/fb-comments.csv"%cm.export_dir,'w')
    btoolsfile.csv_write_line("Post","Post ID","Created (GMT)","Name","User ID","Comment","Comment ID")

for post_id in btoolsfile.targetids:
    comment_count=0
    post_content=fbio.fb_interact(fbio.get_post,post_id)
    comments_data=fbio.fb_interact(fbio.get_comments,post_id)
    for x in comments_data:
        ac_createdtime=x['created_time'].encode("utf-8")
        try:
            x_from=x['from']
            ac_name=x_from['name'].encode("utf-8")
            ac_userid=x_from['id'].encode("utf-8")
        except:
            ac_name="(unknown)"
            ac_userid="(unknown)"
        ac_message=x['message'].encode("utf-8")
        ac_postid=x['id'].encode("utf-8")
        btoolsfile.csv_write_line(post_content,post_id,ac_createdtime,ac_name,ac_userid,ac_message,ac_postid)
        comment_count+=1
    fbio.remove_from_workingids(post_id)
    print "Exported: %s (%s/%s, %s comments)"%(post_id,len(btoolsfile.targetids)-len(fbio.workingids),len(btoolsfile.targetids),comment_count)

btoolsfile.active_file_obj.close()

print "Export complete!"
cm.keypress_exit("")
