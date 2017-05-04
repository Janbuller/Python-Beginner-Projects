import time
from random import randint
import os
import Responses_SCR

Asked = []
while True:
    print('Type your question, and it will be answered.')
    print('Type \'Quit\' to Quit')
    User_Input = input('What is your question: ')

    if User_Input == 'Quit':
        Asked_File = open('Asked.txt', 'a')
        Asked_File.write(str(Asked))
        Asked_File.close()
        break
    elif User_Input == 'quit':
        Asked_File = open('Asked.txt', 'a')
        Asked_File.write(str(Asked))
        Asked_File.close()
        break
    else:
        Asked.append(User_Input)
        print('Thinking')
        time.sleep(randint(3, 6))
        Response = Responses_SCR.Responses[randint(0, 15)]
        Asked.append(Response)
        print(Response)
        time.sleep(randint(3, 5))
        os.system('cls')