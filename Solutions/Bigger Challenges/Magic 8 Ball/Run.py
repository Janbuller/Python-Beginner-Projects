import time
from random import randint
import os

Responses = ('As i see it, yes.', 'Ask again later.', 'Better not tell you now.', 'Cannot predict now.', 'Concentrate and ask again',
            'Don\'t count on it', 'It is certain.', 'It is decidely so.', 'Most likely.', 'My reply is no.', 'My sources say no.',
             'Yes.', 'Yes - definitely', 'You may rely on it', 'Without a doubt.', 'Of course')

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
        Response = Responses[randint(0, 15)]
        Asked.append(Response)
        print(Response)
        time.sleep(randint(3, 5))
        os.system('cls')
