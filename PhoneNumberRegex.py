import re
phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumberRegex.search(input('Enter the message with a phone number '))
print('Phone number found: ' + mo.group())
