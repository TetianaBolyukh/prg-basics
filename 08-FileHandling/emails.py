import re
def sender_address(content):
    sender = re.search(r'From:.*<(.+@\w.+com)>', content)
    return sender.group(1)

def recipient_address(content):
    recipient = re.search(r'To:.*<(.+@\w.+com)>', content)
    return recipient.group(1)

def email_subject(content):
    subject = re.search(r'Subject:\s+(.*)', content)
    return subject.group(1)

def email_body(content):
    body = re.search(r'\n\n(.*)', content, re.S)
    return body.group(1)