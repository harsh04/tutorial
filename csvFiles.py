import pandas as pd
import os

if os.path.exists('files/Data.csv'):
    data = pd.read_csv('files/Data.csv')
    print(data)
else:
    print('File not present')
