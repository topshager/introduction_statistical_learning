import pandas as pd
import seaborn as sns
Boston = pd.read_csv('Boston.csv')

sns.pairplot(Boston.select_dtypes(include=['number']))

plt.show()
