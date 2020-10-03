import sklearn as sk
print(sk.__version__)       #it will display version of sklearn

import sys
print(sys.path)

# using below syntax we can retrieve another files to one place all things are possible with the help of sklearn
from sklearn.ensemble import RandomForestClassifier
print(RandomForestClassifier())
from exercise_5 import i
print(i)

