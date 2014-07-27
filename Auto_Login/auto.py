import urllib, urllib2, sys, getpass
class terminalpassword(urllib2.HTTPPasswordMgr):
    def find_user_password(self, realm, authuri):
        retval=urllib2.HTTPPasswordMgr.find_user_password(self, realm, authuri)
        if retval[0]==None and retval[1]==None:
            sys.stdout.write("Login requires for %s at %s\n" %(realm, authuri))
            sys.stdout.write('Username:')
            username=sys.stdin.readline().rstrip()
            #password=sys.stdin.readline().rstrip()
            password=getpass.getpass().rstrip()
            return (username, password)
        else:
            return retval

req=urllib2.Request('http://192.168.1.1')
opener=urllib2.build_opener(urllib2.HTTPBasicAuthHandler(terminalpassword()))
fd=opener.open(req)
print 'retrieved', fd.geturl()
info=fd.info()
for key, value in info.items():
    print '%s=%s' %(key, value)
print urllib2.urlopen(req).geturl()
