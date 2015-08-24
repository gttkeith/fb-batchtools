import cm
import facebook

global access_token
global graph

def read_access_token():
    global access_token
    tr=open("%s/access_token"%cm.cfg_dir)
    access_token=tr.read()
    tr.close()

def change_access_token():
    global access_token
    print """Head to the following URL and get a new access token for the user/Page which you would like to use Facebook as!

https://developers.facebook.com/tools/explorer/
"""
    at_raw=cm.raw_input_lb("Paste your new access token here:\n> ")
    bw=open("%s/access_token"%cm.cfg_dir,'w')
    bw.write(at_raw)
    bw.close()
    read_access_token()
    ret=check_auth()
    return ret

def check_auth():
    global access_token
    global graph
    try:
        graph=facebook.GraphAPI(access_token,version='2.2')
        info=graph.get_object("me")
        ret=info["name"]
        return ret
    except facebook.GraphAPIError:
        print "The access token seems to be invalid or expired."
        ret=change_access_token()
        return ret

def auth_choose():
    global graph
    authenticated=False
    while authenticated is False:
        print "Authenticating..."
        token_name=check_auth()
        print "Authorised: %s"%token_name
        print "\nContinue as this user?\nPress ENTER to continue, or type 'no' and press ENTER to change your access token."
        authchoice=cm.raw_input_lb("> ")
        # TODO: add ability to interrupt with ESC instead of typing no
        if authchoice is "":
            authenticated=True
            return graph
        else:
            print "Authentication canceled."
            access_token="null"
            change_access_token()

def begin():
    read_access_token()
    auth_choose()
