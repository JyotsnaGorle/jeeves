import httplib2
import os

from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools
from conf.data_sources import data_sources

try:
    import argparse

    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'
CLIENT_SECRET_FILE = os.path.join(data_sources['gmail_api_key_path'], 'client_secret.json')


class EmailReader():
    def __init__(self):
        self.type = "s/w"

    def get_credentials(self):

        home_dir = os.path.expanduser('~')
        credential_dir = os.path.join(home_dir, 'credentials')
        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)
        credential_path = os.path.join(credential_dir,
                                       'gmail-quickstart.json')

        store = oauth2client.file.Storage(credential_path)
        credentials = store.get()
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
            if flags:
                credentials = tools.run_flow(flow, store, flags)
            else:  # Needed only for compatability with Python 2.6
                credentials = tools.run(flow, store)
            print 'Storing credentials to ' + credential_path
        return credentials

    def read_mails(self):

        user_id = 'me'
        label = 'UNREAD'
        credentials = self.get_credentials()
        http = credentials.authorize(httplib2.Http())
        service = discovery.build('gmail', 'v1', http=http)
        response = service.users().messages().list(userId=user_id, labelIds=label).execute()
        messages = []

        if 'messages' in response:
            messages.extend(response['messages'])
        print response['resultSizeEstimate']
        print messages[0:5]

        for each in messages[0:5]:
            message_content = service.users().messages().get(userId=user_id, id=each['id'],
                                                             format='raw').execute()
            print message_content['snippet']
