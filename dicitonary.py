import random
class Mammals:

    def key_sel(self):

        mamm = {
            'elephant': [' a) they move in herds', ' b) it can smell water from miles away',
                         ' c) they have very good memory\n'],
            'dog': [' a) in the wild, live in packs', ' b) very good sense of smell',
                    ' c) used for hunting\n'],
            'bat': [' a) cannot see', ' b) very active at night',
                     ' c) often mistaken to be vampires\n'],
            'human': [' a) warm blooded', ' b) can program',
                      ' c) loves socializing\n']
        }

        count = 0

        while count < len(mamm):
            k = random.choice(list(mamm))

            m = (mamm[k])

            count += 1

            return '\n'.join(m), k

            # return m

    # print(key_sel())
