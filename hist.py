import matplotlib.pyplot as plt
import pandas as pd

quant_vars = ["Outstate", "Apps", "Accept", "Enroll"]
fig,ax = plt.subplots(2,2,figsize=(10,8))

axes=ax.flatten()
bin_size = [10, 20, 30, 40]
for i,var in enumerate(quant_vars):
    college[var].plot.hist(bins=bin_size[i],ax=axes[i],alpha=0.7,edgecolor="black")
    axes[i].set_title(f"Histogram of {var}")


plt.tight_layout()
plt.show()
