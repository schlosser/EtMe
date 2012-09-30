from foursquare import Foursquare

base_url="http://localhost:5000"

def makeClient():
    return Foursquare(client_id = "3GZG0BE3SQSWRKGCXXSEJD4FM2TWGXTQOFQUWOKCQ3ZILXEP",
            client_secret = "EXTDHANAPBAR3PDAGJU2DLLZFJPPH1KZYESMY00LXZCVTEBW",
            redirect_uri = base_url + "/auth2")

