 
from sendEmailsFuncs.chooseEmails import chooseEmails
from sendEmailsFuncs.sendEmails import gmail_send_message

df = chooseEmails()
print(df)
# gmail_send_message(df['email'])