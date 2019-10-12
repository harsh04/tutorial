# myfile = open('fruits.txt')
# content = myfile.read()
# print(content)
# myfile.close()    # explicitly close opened files


# with will handle closing of file automatically
# with open('files/vegitables.txt', 'w') as myfile:
#     myfile.write('tomatos\n')
#     myfile.write('onions')

# with open('files/fruits.txt', 'r') as myfile:
#     content = myfile.read()

# with open('files/vegitables.txt', 'a+') as myfile:
#     myfile.write('\n' + content)
#     myfile.seek(0)
#     content = myfile.read()

# print(content)

dictionary = {}
with open('files/secret.txt') as myfile:
    for line in myfile:
        (key, val) = line.split('=')
        dictionary[key] = str(val).replace('\n','')

print('Welcome to version {}'.format(dictionary['version']))
while True:
    password = input('Enter password :')
    if password == dictionary['password']:
        print('Valid password')
        break
    else:
        print('Invalid password')
