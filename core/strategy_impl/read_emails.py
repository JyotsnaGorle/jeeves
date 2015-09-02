from .base_strategy import BaseStrategy
from utils.say import say
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from conf.data_sources import data_sources

import httplib2
import os
import argparse
import oauth2client

flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'
CLIENT_SECRET_FILE = os.path.join(data_sources['gmail_api_key_path'], 'client_secret.json')

# TODO: check for the existence of the CLIENT_SECRET_FILE

class EmailReader:
    def get_credentials(self):
        home_dir = os.path.expanduser('~')
        credential_dir = os.path.join(home_dir, 'credentials')
        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)
        credential_path = os.path.join(credential_dir,
                                       'login_credentials.json')

        store = oauth2client.file.Storage(credential_path)
        credentials = store.get()
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
            credentials = tools.run_flow(flow, store, flags)
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

        say('you have %d unread emails; and how many would you like me to read?' % response['resultSizeEstimate'])
        limit = int(raw_input("reply: "))

        count = 0
        for each in messages[:limit]:
            count += 1
            message_content = service.users().messages().get(userId=user_id, id=each['id'],
                                                             format='raw').execute()
            say('message %d' % count)
            say(message_content['snippet'])


class ReadEmails(BaseStrategy):
    def __init__(self):
        self.type = "s/w"

    def describe(self):
        return "I'm supposed to read you your emails"

    def perform(self):
        email_reader = EmailReader()
        email_reader.read_mails()

    def react(self):
        say("reading today's unread emails")
