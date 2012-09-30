# imports
from init import makeClient
from foursquare import Foursquare
from flask import session

def getData():
    data = []
    client = makeClient();
    # Fetch accesscode from cookies
    access_token = session['access_token'];
    client.set_access_token(access_token);
    
    # Listing check-ins
    checkIns = client.users.checkins(params={'limit': 5})['checkins'];
    # Look for Tags
    venues = [];
    for i in range(checkIns['count']):
        checkIn = checkIns['items'][i];
        if checkIn['type']=='valueless': continue;
        venues = venues + [checkIn['venue']['id']];

    tagSet = [];
    for i in venues:
        venue = client.venues(i)['venue'];
	if len(venue['tags'])>=5 :
            tagSet += venue['tags'][0:4];
        else:
            tagSet += venue['tags'];
            for j in venue['categories']:
                tagSet+= [j['name']];


    print tagSet
    return tagSet
