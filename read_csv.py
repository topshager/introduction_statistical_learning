import pandas as pd
Auto = pd. read_csv ('Auto.data ',
na_values =['?'],
delim_whitespace =True)
Auto['horsepower ']. sum ()
Auto.shape
