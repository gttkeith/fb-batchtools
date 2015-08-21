import json
import ast
import facebook
from pydeps import cm
from pydeps import pkinit
from pydeps import fbauth
from pydeps import fbio
from pydeps import pkfileops

pkinit.init()

# and here we go!
print "\nCOMMENT FETCHER v0.1\nExports all comments on selected posts into a CSV file\n"
fbauth.begin()

fbio.workingids=pkfileops.import_ids_txt()

# lambs to the slaughter
print "Writing to file..."
pkfileops.active_file_obj=open("%s/fb-comments.csv"%cm.export_dir,'w')
pkfileops.csv_write_line("Post","Post ID","Name","User ID","Comment","Comment ID")

# write till we drop
for post_id in pkfileops.targetids:
    post_content=fbio.get_post(post_id)
    comments_data=fbio.get_post_comments(post_id)
    for x in comments_data:
        x_from=x['from']
        ac_name=x_from['name']
        ac_userid=x_from['id']
        ac_message=x['message']
        ac_postid=x['id']
        pkfileops.csv_write_line(post_content,post_id,ac_name,ac_userid,ac_message,ac_postid)
    fbio.workingids[:] = [item for item in fbio.workingids if item != post_id]
    print "Exported: %s"%post_id

pkfileops.active_file_obj.close()

print "Export complete!"
cm.keypress_exit("")
