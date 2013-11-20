from project.settings import *

# Construct the client object
client = foursquare.Foursquare(
    client_id=FOURSQUARE_CLIENTID,
    client_secret=FOURSQUARE_SECRET,
    redirect_uri='http://localhost/fq/redirect')

# Build the authorization url for your app
auth_uri = client.oauth.auth_url()
