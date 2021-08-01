import pandas as pd
from sklearn import preprocessing

TRAINING_DATA = None
FOLD = None

FOLD_MAPPING = {
    0 : [1,2,3,4],
    1: [0,2,3,4],
    2:[0,1,3,4],
    3:[0,1,2,4],
    4:[0,1,2,3]
}