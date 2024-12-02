from emails import sender_address, recipient_address, email_subject, email_body

with open('email.txt','r') as file:
    content = file.read()
    lines = content.splitlines()

print(sender_address(content))
print(recipient_address(content))
print(email_subject(content))
print(email_body(content))