A = matrix(RR, 7, [.8, .2, 0, 0, 0, 0, 0,  # Sleeping
                   .05, .45, .5, 0, 0, 0, 0,  # Morning
                   0, 0, .65, .35, 0, 0, 0,  # Coffee
                   0, 0, 0, .65, .35, 0, 0,  # Class
                   0, 0, .3, 0, .5, .2, 0,  # Eat food
                   .2, 0, 0, 0, .2, .5, .1,  # Homework
                   .95, 0, 0, 0, 0, 0, .05])  # Movie

emission_symbols = ['zzz', 'I\'m tired', 'Need coffee...', 'Hello!', 'Yay!', 'So bored...', 'That was interesting', 'I\'m hungry', 'Yum', 'Eureka', 'Need a drink']
B = matrix(RR, 7, 11, [.9, .1, 0, 0, 0, 0, 0, 0, 0, 0, 0,  # Sleeping
                       0, .4, .5, .1, 0, 0, 0, 0, 0, 0, 0,  # Morning
                       0, 0, 0, .3, .3, 0, 0, 0, .4, 0, 0,  # Coffee
                       0, 0, .1, 0, 0, .6, .3, 0, 0, 0, 0,  # Class
                       0, 0, 0, 0, 0, 0, 0, .3, .7, 0, 0,  # Eat food
                       0, 0, .3, 0, 0, .2, 0, 0, 0, .1, .4,  # Homework
                       0, 0, 0, 0, .5, 0, .5, 0, 0, 0, 0])  # Movie

initial = [0, 1, 0, 0, 0, 0, 0]

model = hmm.DiscreteHiddenMarkovModel(A, B, initial, emission_symbols)

model
