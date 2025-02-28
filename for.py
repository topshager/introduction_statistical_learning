total = 0
for value in [3,2,19]:
    total += value
print('Total is: {0}'.format(total))


total = 0
for value in [2,3,44]:
    for weight in [4,5,2]:
        total+= value + weight
print('total is:{0}'.format(total))


total = 0
for value, weight in zip([2,3,19],[0.2,0.3,0.5]):
        total += weight * value
print('Weighted average is: {0} '.format(total))


for col in D.columns:
    template = 'column "{0}" has {1:.2%} missing values'
    print(template.format(col,np.isnan(D[col]).mean()),)


fix,ax = subplots(figsize=(8,8))
ax.plot(Auto['horsepower'],Auto['mpg'],'o');


ax =Auto.plot.scatter('horsepower','mpg');
ax.set_title('Horsepower vs. MPG')

fig = ax.figure
fig.savefig('horsepower_mpg.png');


fig,axes = subplots(ncols=3,figsize=(15,5))
Auto.plot.scatter('horsepower','mpg',ax=axes[1]);

Auto.cylinders = pd.Series(Auto.cylinders,dtype ='category')
Auto.cylinders.dtype

fig,ax = subplots(figsize=(8,8))
Auto.boxplot('mpg',by='cylinders',ax=ax);



fig,ax = subplots(figsize=(8,8))
Auto.hist('mpg',ax=ax);

fix,ax = subplots(figsize=(8,8))
Auto.hist('mpg',color='red',bins=12,ax=ax);

pd.plotting.scatter_matrix(Auto);


pd.plotting.scatter_matrix(Auto[['mpg','displacement','weight']]);


Auto[['mpg','weight']].describe()

Auto['cylinders'].describe()
Auto['mpg'].describe()
