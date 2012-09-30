import requests
import json
from collections import Counter
from EtsyListing import EtsyListing

def getProducts(data):
    List = counterToList(importData(data))
    List2 = []
    for i in List:
        List2.append(i[0])        
    return List2

def importData(data):
    EtsyListingCounter = Counter()
    for keyword in data:
        print("We're on the keyword", keyword)
        keywordString = buildURL(keyword)
        textListingLibrary = json.loads(requests.get(keywordString).text)
        for textListing in textListingLibrary['results']:
            EtsyListingCounter.update({convert(textListing)})
    return EtsyListingCounter

def convert(textListing):
    listing_id = textListing['listing_id']
    title = textListing['title']
    description = textListing['description']
    listing_url = textListing['url']
    image_url = findImageURL(listing_id)
    
    mEtsyListing = EtsyListing(listing_id, title, description, listing_url, image_url)

    return mEtsyListing
        
def findImageURL(listing_id):
    urlString = 'http://openapi.etsy.com/v2/listings/' + str(listing_id) + '/images?api_key=o9hb5cpjkolw3fx44r46q6lh'
    imageRequest = requests.get(urlString)
    imageLibrary = json.loads(imageRequest.text)
    for image in imageLibrary['results']:
        if image['rank'] == 1:
            return image['url_170x135']
    return 'http://cdn2.holytaco.com/wp-content/uploads/images/2009/12/funny-pictures-bird-cat-cage.jpg'

def buildURL(keywordString):
    baseString = 'http://openapi.etsy.com/v2/listings/active?limit=5&offset=0&api_key=o9hb5cpjkolw3fx44r46q6lh'
    returnFields = '&fields=listing_id,title,description,url'
    keywords = '&keywords=' + keywordString
    return baseString + returnFields + keywords

def counterToList(counter):
    myList = []
    myList += [counter.popitem()]
    for key in counter:
        placed = 0; val = counter[key]; imax = len(myList); imin = 0
        while (imax > imin and placed == 0):
            imid = (imax + imin)/2
            if(myList[imid][1] < val):
                imin = imid + 1
            elif(myList[imid][1] > val):
                imax = imid
            else:
                placed = 1
        myList.insert((imax+imin)/2, (key, val))
    return myList        
