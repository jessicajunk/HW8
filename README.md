HW8
===

This Hidden Markov Model shows an average day of an average college student.

The model is as follows:

Discrete Hidden Markov Model with 7 States and 11 Emissions

Transition matrix:

[ 0.8  0.2  0.0  0.0  0.0  0.0  0.0]
[0.05 0.45  0.5  0.0  0.0  0.0  0.0]
[ 0.0  0.0 0.65 0.35  0.0  0.0  0.0]
[ 0.0  0.0  0.0 0.65 0.35  0.0  0.0]
[ 0.0  0.0  0.3  0.0  0.5  0.2  0.0]
[ 0.2  0.0  0.0  0.0  0.2  0.5  0.1]
[0.95  0.0  0.0  0.0  0.0  0.0 0.05]

Emission matrix:

[0.9 0.1 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0]
[0.0 0.4 0.5 0.1 0.0 0.0 0.0 0.0 0.0 0.0 0.0]
[0.0 0.0 0.0 0.3 0.3 0.0 0.0 0.0 0.4 0.0 0.0]
[0.0 0.0 0.1 0.0 0.0 0.6 0.3 0.0 0.0 0.0 0.0]
[0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.3 0.7 0.0 0.0]
[0.0 0.0 0.3 0.0 0.0 0.2 0.0 0.0 0.0 0.1 0.4]
[0.0 0.0 0.0 0.0 0.5 0.0 0.5 0.0 0.0 0.0 0.0]

Initial probabilities: [0.0000, 1.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000]

Emission symbols: ['zzz', "I'm tired", 'Need coffee...', 'Hello!', 'Yay!', 'So bored...', 'That was interesting', "I'm hungry", 'Yum', 'Eureka', 'Need a drink']
