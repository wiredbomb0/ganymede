import urllib2
target_url = "https://raw.githubusercontent.com/wiredbomb0/valkyrie/master/valkyrie.filter"
for line in urllib2.urlopen(target_url):
  print line,
