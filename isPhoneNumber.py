def isPhoneNumber(text):
	if(len(text)!=12):
		return False
	if text[3] != '-' :
		return False
	for i in range(4,7):
		if not text[i].isdecimal():
			return False
	if text[7] != '-':
		return False
	for i in range(8,12):
		if not text[i].isdecimal():
			return False
	return True

message = str(input('Enter the message with a phone number '))
for i in range(len(message)):
	chunk = message[i:i+12]
	if isPhoneNumber(chunk):
		print('Phone number found: '+chunk)
print('Done')