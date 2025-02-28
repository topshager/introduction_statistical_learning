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
