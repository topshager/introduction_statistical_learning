Auto_re.loc[lambda df:df['year'] > 80 ,['weight','origin']]
Auto_re.loc[lambda df:(df['year'] > 80) & (df['mpg']>30),['weight','origin']]

Auto_re.loc[lambda df: (df['displacement '] < 300)
& (df.index.str.contains ('ford ')
| df.index.str.contains ('datsun ')),
['weight ', 'origin ']
]
