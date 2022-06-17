from dicitonary import Mammals

correctAns = Mammals()
# destructuring 
clues, mammal = correctAns.key_sel()

print(clues)

n = input('Enter mammal: ')

breakpoint()

if n.lower() == mammal:
    print('Correct!!')
else:
    print('wrong')
    