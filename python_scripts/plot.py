import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sys

df_different = pd.read_csv(sys.argv[1])
df_different.head()

df_same = pd.read_csv(sys.argv[2])
df_same.head()

sns.boxplot(df_different[['transfer_GB', 'bandwidth_Gb_s']])
plt.savefig('different.png')
plt.clf()

sns.boxplot(df_same[['transfer_GB', 'bandwidth_Gb_s']]).get_figure().savefig('same.png')
plt.savefig('same.png')