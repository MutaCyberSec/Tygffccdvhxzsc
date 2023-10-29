import re
import dns.resolver

gm = []

def is_valid_gmail(email):
    # Check if the email address follows a valid syntax
        if not re.match(r"[^@]+@gmail\.com$", email):
                return False

    # Check if Gmail has valid MX (Mail Exchange) records
        try:
                mx_records = dns.resolver.resolve('gmail.com', 'MX')
                for mx in mx_records:
                        if 'google.com' in str(mx.exchange):
                                return True
#return False
        except Exception:
                return False

with open('veriss.txt', 'r') as file:
    # Read the entire file content into a string
        file_contents = file.read()

#thems = file_contents.split(',')
thems = "jacksonmuta123@gmail.com,jdkkfkdkkd@gmail.com"
for x in thems:
        email = x
        if is_valid_gmail(email):
                gm.append(x)



with open('nal.txt', 'w') as file:
        dem = ",".join(gm)
        file.write(dem)
print(len(gm))

