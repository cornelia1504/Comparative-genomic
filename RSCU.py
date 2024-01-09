import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


file_path = r'D:\0-AMU\DLAD\6-GecO\PROJET-TP1\CALCU_python\3.2_gene_compare.xlsx'


df = pd.read_excel(file_path, sheet_name=5, index_col=0)


sns.set()


df_reset = df.reset_index()


plt.figure(figsize=(15, 8))
sns.barplot(data=df_reset.melt(id_vars=['Codon', 'AA'], var_name='Species'), x='Codon', y='value', hue='Species', dodge=True)


plt.title('Gene Comparison')
plt.xlabel('Codon')
plt.ylabel('RSCU')


plt.legend(title='Species', bbox_to_anchor=(1.05, 1), loc='upper left')


plt.tight_layout()


plt.show()