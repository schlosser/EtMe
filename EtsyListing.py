class EtsyListing:

    def __init__(self, listing_id, title, description, listing_url,
                 image_url):
        self.LISTING_ID = listing_id
        self.TITLE = title
        self.DESCRIPTION = description
        self.LISTING_URL = listing_url
        self.IMAGE_URL = image_url

    def __eq__(self, other):
        if(self.LISTING_ID == other.LISTING_ID):
            return True
        else:
            return False

    def __hash__(self):
        return hash(self.LISTING_ID)
