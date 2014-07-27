import urllib, urllib2, sys
url='http://www.douban.com/accounts/login'
email='1017290330@qq.com'
password='fengfeng'
data=urllib.urlencode({'form_email':email, 'form_password':password})
req=urllib2.Request(url)
fd=urllib2.urlopen(url, data)
print fd.geturl()
print fd.read()
