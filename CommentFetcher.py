from core import cm,btoolsinit,btoolsfile,fbauth,fbio

btoolsinit.init()

print "\nCOMMENT FETCHER v0.1\nExports all comments on selected posts into a CSV file\n"
fbauth.begin()

btoolsfile.import_ids_txt()


if cm.active_dir==cm.resume_dir:
    print "Resuming export..."
    btoolsfile.active_file_obj=open("%s/fb-comments.csv"%cm.export_dir,'a')
else:
    print "Exporting to file..."
    btoolsfile.active_file_obj=open("%s/fb-comments.csv"%cm.export_dir,'w')
    btoolsfile.csv_write_line("Parent Post","Parent ID","Created","Name","User ID","Comment","Comment ID")

for post_id in btoolsfile.targetids:
    comment_count=0
    post_content=fbio.fb_interact(fbio.get_post,post_id)
    comments_data=fbio.fb_interact(fbio.get_comments,post_id)
    for single_comment in comments_data:
        fromseek=cm.dict_to_datalist(single_comment.get("from"),"name","id")
        rootseek_params=["created_time",fromseek,"message","id"]
        x_data=cm.dict_to_datalist(single_comment,*rootseek_params)
        btoolsfile.csv_write_line(post_content,post_id,*x_data)
        comment_count+=1
    fbio.remove_from_workingids(post_id)
    print "Exported: %s (%s/%s, %s comments)"%(post_id,len(btoolsfile.targetids)-len(fbio.workingids),len(btoolsfile.targetids),comment_count)

btoolsfile.active_file_obj.close()

print "Export complete!"
cm.keypress_exit("")
