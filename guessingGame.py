from dicitonary import Mammals

clues = ['they move in herds', 'it can smell water from miles away',
         'they have very good memory']
question = 'Guess the mammal:  '
answer = ''
numb = 1
correctAns = 'elephant'
i = 0

# iterate through the clues. the number of clues determines the chances you have to guess the correct answer
while answer != correctAns and numb <= 3:
    # print the first clue
    print('Clue #' + str(numb) + ' ' + clues[i])

    # ask the question and get the answer as well
    answer = input(question)

    # check if the answer is correct
    if answer.lower().strip() == correctAns:
        print('win!!!')

        break

    # no chances left
    else:
        print('Wrong !!!')
        
        # no more chances left
        if numb == 3:
            print('You lose')

    numb += 1
    i += 1
    print('line 33 here')
    