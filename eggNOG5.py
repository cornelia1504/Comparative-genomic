import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


file_path = r'D:\0-AMU\DLAD\6-GecO\PROJET-TP1\CALCU_python\eggnog_percentage -all.csv'


df = pd.read_csv(file_path)


colors = sns.color_palette('husl', 5)


plt.figure(figsize=(15, 8))
for i, col in enumerate(df.columns[1:]):
    plt.subplot(2, 3, i + 1)
    plt.bar(df[df.columns[0]], df[col], color=colors[i])
    plt.title(f'{col} Percentage Distribution')
    plt.xlabel(df.columns[0])
    plt.ylabel('Percentage')

plt.tight_layout()
plt.show()
