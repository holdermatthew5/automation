import re

result = []
numbers = []
emails = []
regex = '\(?\d{3}?\S?\d{3}\S?\d{4}'
regex1 = '\S+@\S+.[a-z]{3}'
with open('assets/potential_contacts.txt') as pc:
    lines = pc.readlines()
    numbers1 = [re.findall(regex, i) for i in lines if re.findall(regex, i)]
    for i in numbers1:
        if type(i) == list:
            for j in i:
                numbers.append(j)
        else:
            numbers.append(i.group())
    for i in range(len(numbers)):
        if not numbers[i][0].isdigit():
            numbers[i] = f'{numbers[i][1:4]}-{numbers[i][5:8]}-{numbers[i][9:]}'
        if re.search('\d{10}', numbers[i]):
            numbers[i] = f'{numbers[i][:3]}-{numbers[i][3:6]}-{numbers[i][6:]}'
        if numbers[i][3] == '.':
            numbers[i] = f'{numbers[i][:3]}-{numbers[i][4:7]}-{numbers[i][8:]}'
    result = sorted(numbers)
    numfile = open('assets/numbers.txt', 'w+')
    for i in result:
        print(i)
        numfile.write(i+'\n')
    numfile.close()
    emails1 = [re.findall(regex1, i) for i in lines if re.findall(regex1, i)]
    for i in emails1:
        if type(i) == list:
            for j in i:
                emails.append(j)
        else:
            emails.append(i)
    emails = sorted(emails)
    emailfile = open('assets/emails.txt', 'w+')
    for i in emails:
        emailfile.write(i+'\n')
    emailfile.close()
