from apiclient import discovery
from google_auth_oauthlib.flow import InstalledAppFlow


scopes = ["https://www.googleapis.com/auth/calendar.readonly"]

flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes=scopes)
flow.run_console()

