import feedparser
print('add url to parse')
url=input('')
p = feedparser.parse(url)
print(p['feed']['title'])
print(p['feed']['link'])
print(len(p['entries']))
print(p['entries'][0]['title']) 
print(p.entries[0]['link'])
for post in p.entries:
    print(post.title + ": " + post.link + "")
print(p.headers)         	
print(p.headers.get('content-type'))
