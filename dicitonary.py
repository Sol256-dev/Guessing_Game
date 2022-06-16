import random

class Mammals:

    def key_sel():

        mamm = {
            'elephant': [' a) they move in herds\n', ' b) it can smell water from miles away\n',
                         ' c) they have very good memory\n\n'],
            'dog': [' a) in the wild, live in packs\n', ' b) very good sense of smell\n',
                    ' c) used for hunting\n\n'],
            'bat': [' a) cannot see\n', ' b) very active at night\n',
                     ' c) often mistaken to be vampires\n\n'],
            'human': [' a) warm blooded\n', ' b) can program\n',
                      ' c) loves socializing\n\n']
        }

        count = 0

        while count < len(mamm):
            k = random.choice(list(mamm))
           
            count += 1

            return k

    print(key_sel())
