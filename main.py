import re

email = re.compile(r'(^[a-zA-Z0-9]+@[a-zA-Z]+\.[a-z]+$)') # email should be valid
password = re.compile(r'^[a-zA-Z0-9$#@]{8,}\d') # password length should be 8 char long

input_email = 'mayanknagora@gmail.com'
input_password = 'mayank@10'

result_email = email.fullmatch(input_email)
result_password = password.fullmatch(input_password)

print(result_email)
print(result_password)
