import cm
import facebook

global access_token
global graph

def read_access_token():
    global access_token
    tr=open("%s/access_token"%cm.cfg_dir)
    access_token=tr.read()
    tr.close()
    return access_token

def change_access_token():
    global access_token
    print """Head to the following URL and get a new access token for the user/Page which you would like to use Facebook as!

https://developers.facebook.com/tools/explorer/
"""
    access_token=cm.raw_input_lb("Paste your new access token here:\n> ")
    bw=open("%s/access_token"%cm.cfg_dir,'w')
    bw.write(access_token)
    bw.close()
    check_auth(access_token)

def check_auth(access_token):
    global graph
    try:
        graph=facebook.GraphAPI(access_token,version='2.2')
        info=graph.get_object("me")
        ret=info["name"]
        return ret
    except facebook.GraphAPIError:
        print "The access token seems to be invalid or expired."
        change_access_token()

def auth_choose(access_token):
    authenticated=False
    while authenticated is False:
        print "Authenticating..."
        token_name=check_auth(access_token)
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
    auth_choose(read_access_token())
