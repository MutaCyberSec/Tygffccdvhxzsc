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
  <title>Your Thank You</title>
</head>
<body style ="font-size: 20px;">
  <p>We extend our heartfelt gratitude for your generous support. Your donations make a profound impact, helping us create positive change in our community. Thank you.</p>

  <p>If you feel like you could help another family through Psychological ,financial or emotional difficulties or help  a child save their dreams, please visit our website:

<br> <a href="https://borderlesscharities.com" style="display: inline-block; padding: 10px 20px;     background-color: #093157; color: white; text-decoration: none; border-radius: 5px;">Borderless</a></p>
<br>
If you received this email in the spam folder,please mark as not spam since this is our new domain
where Gmail has less history about.
To unsubscribe from our newsletters respond to this email with the word "unsubscribe"
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
