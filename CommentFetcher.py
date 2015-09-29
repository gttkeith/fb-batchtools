from core import cm,btoolsinit
btoolsinit.init()

from core import btoolsfile,fbauth,fbio

print "\nCOMMENT FETCHER\nExports all comments on selected posts into a CSV file\n"
fbauth.begin()

btoolsfile.import_ids_txt()
btoolsfile.smart_edit("%s/fb-comments.csv"%cm.export_dir)
btoolsfile.csv_write_line("Parent Post","Parent ID","Created","Name","User ID","Comment","Comment ID")

for post_id in btoolsfile.targetids:
    comment_count=0
    comment_s="s"
    post_content=fbio.fb_interact(fbio.get_content,post_id)
    comments_data=fbio.fb_interact(fbio.get_comments,post_id)
    for single_comment in comments_data:
        fromseek=cm.dict_to_datalist(single_comment.get("from"),"name","id")
        rootseek_params=["created_time",fromseek,"message","id"]
        x_data=cm.dict_to_datalist(single_comment,*rootseek_params)
        btoolsfile.csv_write_line(post_content,post_id,*x_data)
        comment_count+=1
    fbio.remove_from_workingids(post_id)
    if comment_count is 0:
        btoolsfile.csv_write_line(post_content,post_id,'','','',"(no comments)")
    elif comment_count is 1:
        comment_s=""
    print "Exported: %s (%s/%s, %s comment%s)"%(post_id,len(btoolsfile.targetids)-len(fbio.workingids),len(btoolsfile.targetids),comment_count,comment_s)

btoolsfile.active_file_obj.close()

print "Export complete!"
cm.exexc(None,None)
