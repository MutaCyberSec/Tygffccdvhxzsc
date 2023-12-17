import os



with open('gmailNor.txt', 'r') as file:
    # Read the entire file content into a string
    file_contents = file.read()

recipient_emails = file_contents

x = 0

#recipients = "jacksonmuta123@gmail.com,mwangijackson829@yahoo.com,segechaken023@gmail.com"

email_body = """
<!DOCTYPE html>
<html>
<head>
  <title>Email Confirmation</title>
</head>
<body style ="font-size: 20px;">
  <p>You have received this email because it was used to create n account.If this wasn't you please ignore it.</p>


</p>
</body>
</html>
"""

recipient_list = recipient_emails.split(',')

for recipient in recipient_list:
    email_command = f'mail -a "Content-Type: text/html" -s "Appreciation" {recipient} <<EOF'
    full_email = email_command + email_body
    os.system(full_email)
    x = x +1

print(x)
