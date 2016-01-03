#!/usr/bin/python
#
# LaunchBar Action Script for Seslisozluk.com
#
import sys
import json
import urllib2
import bs4

keyword = " ".join(sys.argv[1:])
url="https://www.seslisozluk.net/%s-nedir-ne-demek/" % keyword
html = urllib2.urlopen(url).read()
soup = bs4.BeautifulSoup(html)
items = []
for segment in soup.findAll("div", {'class': 'sozluk'}):
    items1 = segment.ol.children
    for child in items1:
        try:
            word = child.children.next().strip()
            try:
                description = child.findAll("i")[0].text.strip()
                title = "%s: %s" % (word, description)
            except:
                title = word

            items.append({'title': title})
        except:
            pass
    items.append({'title': '----------------'})

print json.dumps(items)
