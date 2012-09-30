import requests
import json

# works r = requests.get('http://openapi.etsy.com/v2/users/amos?api_key=o9hb5cpjkolw3fx44r46q6lh')
# works r = requests.get('http://openapi.etsy.com/v2/categories/Art?api_key=o9hb5cpjkolw3fx44r46q6lh')
##r = requests.get('http://openapi.etsy.com/v2/taxonomy/categories?api_key=o9hb5cpjkolw3fx44r46q6lh')
##j = json.loads(r.text)
##
##results = j['results']

##print json.dumps(results, indent=4)

##for res in results:
##    keywords = res['meta_keywords'].split(', ')
##    for word in keywords:
##        print word
##    print ''

def buildURL():
    tagRequest = 'http://openapi.etsy.com/v2/listings/active?api_key=o9hb5cpjkolw3fx44r46q6lh'
    returnFields = '&fields=listing_id,state,title,description,tags,featured_rank,url,num_favorers'
    keywords = '&keywords=men,slim'
    return tagRequest+returnFields+keywords






tagRequest = requests.get(buildURL())
myLib = json.loads(tagRequest.text)
results = myLib["results"]


print json.dumps(myLib, indent = 4)

print tagRequest.status_code, " " # str(tagRequest.text)








from collections import namedtuple

EtsyListing = namedtuple('EtsyListing', ['title', 'description', 'listing_url',
                                         'image_url', 'featured_rank', 'num_favorers'])

