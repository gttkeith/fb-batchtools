import sys,traceback
from core import cm,btoolsinit
btoolsinit.depend_chk()
btoolsinit.fs_ensure()

from core import btoolsfile,fbauth,fbio

print "\nTESTBED\nTest your commands here!\n"
fbauth.begin()

print "Ready to accept input."
exit=False
while exit is False:
    cmd=raw_input("> ")
    try:
        out=eval(cmd)
        print out
    except:
        print "\n** EXCEPTION **\n",traceback.format_exc(),"\n"
