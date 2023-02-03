from __future__ import print_function
import base64
from email.message import EmailMessage
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.errors import HttpError

def gmail_send_message(recipient):
    SCOPES = ['https://mail.google.com/']
    creds = None

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials2.json', SCOPES)
            creds = flow.run_local_server(port=8080)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('gmail', 'v1', credentials=creds)
        message = EmailMessage()

        message.set_content('''Dear Avi Dreyfuss,

I hope this email finds you well. My name is Aaron Xie and I am a college student at Dartmouth College, majoring in Computer Science. I am reaching out to you because I am greatly interested in the investment management industry and I admire the work that Fortress Investment Group does.

As I was researching the industry, I came across your LinkedIn profile and your role as CFO in the Credit Division at Fortress Investment Group. I believe you would be a valuable resource for me to learn more about the industry. I would be honored to hear more about your career journey, specifically at Fortress Investment Group, and gain any advice you might have for someone just starting out in the industry.

A bit about me-- I currently have a leadership position in Dartmouth's Blockchain Finance club, and I'm currently doing product engineering at Primitive.xyz, a fintech startup. Here's my resume for more context on my background.

Thank you for taking the time to read this email and I look forward to hearing back from you.
Aaron''')

        message['To'] = recipient
        message['From'] = 'Aaron Xie <gduser2@workspacesamples.dev>'
        message['Subject'] = 'Dartmouth Student Chat Request - Interested in Fortress'

        # encoded message
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()) \
            .decode()

        create_message = {
            'raw': encoded_message
        }
        # pylint: disable=E1101
        send_message = (service.users().messages().send
                        (userId="me", body=create_message).execute())
        print(F'Message Id: {send_message["id"]}')
    except HttpError as error:
        print(F'An error occurred: {error}')
        send_message = None
    return send_message
