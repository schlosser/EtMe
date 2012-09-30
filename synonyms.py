import requests
import string

def getSynonyms(word):
    url = "http://words.bighugelabs.com/api/2/765022ea2b61ad9eb1abb967285eab2e/" + word + "/"
    synonyms = requests.get(url)
    synonyms = string.split(str(synonyms.text), "\n", 4) 
    newSynonyms = []
    for word in synonyms:
        words = string.split(word, "|")
        newSynonyms.append(words[len(words) - 1])
    return newSynonyms
