import numpy as np
import pandas as pd

college = pd.read_csv('College.csv')
college2 = pd. read_csv ('College .csv ', index_col =0)
college3 = college.rename ({'Unnamed : 0': 'College '},
axis =1)
college3 = college3 . set_index ('College ')
college = college3
