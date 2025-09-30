
sent_message = 'Hey there! This is a secret message.'
unsent_message = 'This message has been unsent.'

with open('sent_message.txt', 'w') as file:
  file.write(sent_message)



with open('sent_message.txt', 'r+') as file: #the 'r+' lets you read and write the file. 
  original_message = file.read()
  file.seek(0)
  file.truncate(len(unsent_message))

  file.write(unsent_message)

print('Original Message:', sent_message)
print('Unsent Message:', unsent_message)