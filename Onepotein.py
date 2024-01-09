import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


file_path = r'D:\0-AMU\DLAD\6-GecO\PROJET-TP1\CALCU_python\COG_vs_EggNOG_1.xlsx'


df3 = pd.read_excel(file_path, sheet_name=2)

subset_df = df3[['Number', 'Species']]


sns.set(style="whitegrid")
sns.set_palette("husl")


plt.figure(figsize=(10, 6))
ax = sns.barplot(x='Number', y='Species', data=subset_df, ci=None)


plt.title("Orthologs of protein WP_004693536.1")


ax.xaxis.set_major_locator(plt.MaxNLocator(integer=True))

for p in ax.patches:
    ax.annotate(f'{p.get_width():.0f}', (p.get_width(), p.get_y() + p.get_height() / 2), ha='left', va='center')


plt.xticks(rotation=45, ha='right')


plt.tight_layout()


plt.show()
