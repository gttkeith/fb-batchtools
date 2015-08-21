import json
import ast
import facebook
from pydeps import cm
from pydeps import btoolsinit
from pydeps import fbauth
from pydeps import fbio
from pydeps import btoolsfile

btoolsinit.init()

# and here we go!
print "\nCOMMENT FETCHER v0.1\nExports all comments on selected posts into a CSV file\n"
fbauth.begin()

fbio.workingids=btoolsfile.import_ids_txt()

# lambs to the slaughter
print "Writing to file..."
btoolsfile.active_file_obj=open("%s/fb-comments.csv"%cm.export_dir,'w')
btoolsfile.csv_write_line("Post","Post ID","Name","User ID","Comment","Comment ID")

# write till we drop
for post_id in btoolsfile.targetids:
    post_content=fbio.get_post(post_id)
    comments_data=fbio.get_post_comments(post_id)
    for x in comments_data:
        x_from=x['from']
        ac_name=x_from['name']
        ac_userid=x_from['id']
        ac_message=x['message']
        ac_postid=x['id']
        btoolsfile.csv_write_line(post_content,post_id,ac_name,ac_userid,ac_message,ac_postid)
    fbio.workingids[:] = [item for item in fbio.workingids if item != post_id]
    print "Exported: %s"%post_id

btoolsfile.active_file_obj.close()

print "Export complete!"
cm.keypress_exit("")
