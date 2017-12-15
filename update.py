import urllib2
target_url = https://raw.githubusercontent.com/user/repository/branch/filename
for line in urllib2.urlopen(target_url):
    print line
