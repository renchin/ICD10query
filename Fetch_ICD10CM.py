# Original script from http://stackoverflow.com/questions/3898574/google-search-using-python-script

import urllib2
import urllib.urlencode
import json
query = raw_input ( 'Query: ' )
query = urllib.urlencode ( { 'q' : query } )
response = urllib.urlopen ( 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + query + ' site:www.icd10data.com').read()
list1 = json.loads(response)

#print list1
results = list1['responseData'] ['results']

for result in results:
    title = result['title']
    code = title.split()
    url = result['url']   
    print code[4]
    print (title + url)
