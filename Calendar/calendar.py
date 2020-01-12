from apiclient import discovery
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle


scopes = ["https://www.googleapis.com/auth/calendar.readonly"]

flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes=scopes)
authorization_url, state = flow.authorization_url(
    access_type='offline',
    include_granted_scopes='true')
credentials = flow.run_local_server()

pickle.dump(credentials, open("token.pkl", "wb"))
credentials = pickle.load(open("token.pkl", "rb"))

service = discovery.build("calendar", "v3", credentials=credentials)

result = service.calendarList().list().execute()
calendarId = result['items'][0]['id']

result = service.events().list(calendarId=calendarId).execute()
result["items"][0]