# fb-batchtools
Quick and dirty set of tools for Facebook power users and page admins  


### You'll need  
* Python 2.7: https://www.python.org/download/releases/2.7/  
_Download the appropriate release for the OS you're on, install, and reboot. You can then download fb-batchtools and the scripts should start working._

* Facebook for Python: https://facebook-sdk.readthedocs.org/en/latest/install.html  
_No need to worry about this; fb-batchtools will automatically attempt to install this for you if you don't have it._

* Facebook Graph API access token https://developers.facebook.com/tools/explorer/  
_Remember to enable the relevant permissions for page publishing, page management, ads and insights!_


### Info    
User files are stored at ~/Documents/fb-batchtools, and outputs are exported to ~/Documents/fb-batchtools/export.

IDs can be obtained from the exported Page Insights XLS (recommended), of from the URL of the link itself:  
_http://facebook.com/PAGE_ID_HERE/posts.or.photos.or.stuff/POST_ID_HERE._  

Page names can be used to subsitute IDs as well. IDs from the URL sometimes may result in invalid ID errors; you can check the validity of an ID using the Graph API Explorer (mentioned above).

Place your input IDs and input content in IDs.txt and Content.txt respectively. Some functions use both, some only use one.  


### License
fb-batchtools uses the [GNU General Public License](https://github.com/gttkeith/fb-batchtools/blob/master/LICENSE).
