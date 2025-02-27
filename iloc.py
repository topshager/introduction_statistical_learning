rows = ['amc rebel sst ', 'ford torino ']
Auto_re.loc[rows]
Auto_re.iloc [[3 ,4]]
Auto_re.iloc [: ,[0 ,2 ,3]]
Auto_re.iloc [[3 ,4] ,[0 ,2 ,3]]
Auto_re.loc['ford galaxie 500 ', ['mpg ', 'origin ']]

idx_80 = Auto_re['year'] > 80
Auto_re.loc[idx_80,['weight','origin']]
