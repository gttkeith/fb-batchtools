import cm
import facebook

global access_token

def read_access_token():
    tr=open("%s/Documents/fb-powerkit/cfg/access_token"%cm.usr_home)
    t=tr.read()
    tr.close()
    return t

def reauth():
    print """Head to the following URL and get a new access token for the user/Page which you would like to use Facebook as!

https://developers.facebook.com/tools/explorer/
"""
    t=cm.raw_input_lb("Paste your new access token here:\n> ")
    bw=open("%s/Documents/fb-powerkit/cfg/access_token"%cm.usr_home,'w')
    bw.write(t)
    bw.close()
    return t

def authenticate():
    authenticated=False
    access_token=read_access_token()

    while authenticated is False:
        try:
            print "Authenticating..."
            graph=facebook.GraphAPI(access_token)
            info=graph.get_object("me",**{'fields':'name'})
            token_name=info["name"]
            print "Authorized: %s"%token_name
            print "\nContinue as this user?\nPress ENTER to continue, or type 'no' and press ENTER to change your access token."
            authchoice=cm.raw_input_lb("> ")
            # TODO: add ability to interrupt with ESC instead of typing no
            if authchoice is "":
                authenticated=True
                return graph
            else:
                print "Authentication canceled."
                access_token="null"
                reauth()
        except facebook.GraphAPIError:
            print "The access token seems to be invalid."
            access_token=reauth()
