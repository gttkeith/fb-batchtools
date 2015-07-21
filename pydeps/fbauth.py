import cm
import facebook
from os.path import exists

global access_token

def read_access_token():
    tr=open("cfg/access_token")
    t=tr.read()
    tr.close()
    return t

def reauth():
    print """Head to the following URL and get a new access token for the user/Page which you would like to use Facebook as!

https://developers.facebook.com/tools/explorer/
"""
    t=cm.raw_input_lb("Paste your new access token here:\n> ")
    bw=open("cfg/access_token",'w')
    bw.truncate()
    bw.write(t)
    bw.close()
    return t

def authenticate():
    authenticated=False
    at_check=exists("cfg/access_token")
    
    if at_check is True:
        access_token=read_access_token()
    else:
        print "There's no Facebook access token to read!"
        access_token=reauth()

    while authenticated is False:
        try:
            print "Authenticating..."
            graph=facebook.GraphAPI(access_token)
            info=graph.get_object("me",**{'fields':'name'})
            token_name=info["name"]
            print "Authorized: %s"%token_name
            print "\nContinue as this user?\nPress ENTER to continue, or type 'no' and press ENTER to change your access token."
            authchoice=cm.raw_input_lb("> ")
            # TODO: add ability to interrupt with ESC
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
