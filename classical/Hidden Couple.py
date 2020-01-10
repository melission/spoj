# https://www.spoj.com/problems/HCOUPLE/

numCases = int(input().strip())
for case in range(numCases):
    friendsName = input().strip()
    nameValue = 0
    for letter in friendsName:
        codedLetter = letter.encode('ascii')
        nameValue = nameValue + ord(codedLetter)
    # print(nameValue)
    if nameValue % 3 == 0:
        print('Case {}: Yes'.format(case+1))
    else:
        print('Case {}: No'.format(case+1))