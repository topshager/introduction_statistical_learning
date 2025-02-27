Auto_re.loc[lambda df:df['year'] > 80 ,['weight','origin']]
Auto_re.loc[lambda df:(df['year'] > 80) & (df['mpg']>30),['weight','origin']]
