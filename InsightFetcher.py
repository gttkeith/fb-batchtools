from core import cm,btoolsinit
btoolsinit.init()

from core import btoolsfile,fbauth,fbio
import operator

print "\nINSIGHT FETCHER\nExports insight data on selected pages/posts into a CSV file\nMay work on pages that you do not administrate\n"
fbauth.begin()

btoolsfile.import_ids_txt()
btoolsfile.smart_edit("%s/fb-insights.csv"%cm.export_dir)

for obj_id in btoolsfile.targetids:
    obj_content=fbio.fb_interact(fbio.get_content,obj_id)
    btoolsfile.csv_write_line("%s: %s"%(obj_content,obj_id))
    btoolsfile.csv_write_line()
    insights_data=fbio.fb_interact(fbio.get_insights,obj_id)
    for insight_data in insights_data:
        dtitle=insight_data["title"]
        ddesc=insight_data["description"]
        btoolsfile.csv_write_line("%s - %s"%(dtitle,ddesc))
        latest_data=insight_data["values"].pop().get("value")
        if type(latest_data) is dict:
            dkeys=[]
            dvalues=[]
            dsorted = sorted(latest_data.items(), key=operator.itemgetter(1), reverse=True)
            for k,v in dsorted:
                dkeys.append(k)
                dvalues.append(v)
            btoolsfile.csv_write_line(*dkeys)
            btoolsfile.csv_write_line(*dvalues)
        elif type(latest_data) is list:
            dvalues=[]
            for v in latest_data:
                dvalues.append(v)
            btoolsfile.csv_write_line(*dvalues)
        else:
            btoolsfile.csv_write_line(latest_data)
        btoolsfile.csv_write_line()
    fbio.remove_from_workingids(obj_id)
    if len(insights_data) is 0:
        btoolsfile.csv_write_line("(no insights available)")
        btoolsfile.csv_write_line()
    for r in range(2):
        btoolsfile.csv_write_line()
    print "Exported: %s (%s/%s)"%(obj_id,len(btoolsfile.targetids)-len(fbio.workingids),len(btoolsfile.targetids))

btoolsfile.active_file_obj.close()

print "Export complete!"
cm.exexc(None,None)
