import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


file_path = r'D:\0-AMU\DLAD\6-GecO\PROJET-TP1\CALCU_python\3.2_gene_compare.xlsx'


df = pd.read_excel(file_path, sheet_name=3, index_col=0)


sns.set()


plt.figure(figsize=(12, 8))


max_values = df.max()


bar_width = 0.4
bar_color1 = 'lightblue'
bar_color2 = 'lightgreen'


for gene, value in df.iloc[2, :].items():
    if value < max_values[gene]:
        plt.bar(gene, max_values[gene] - value, bottom=value, width=bar_width, color=bar_color1)
    plt.bar(gene, value, width=bar_width, color=bar_color2)


line_color = 'red'
ax2 = plt.gca().twinx()
line = ax2.plot(df.columns, df.iloc[1, :], color=line_color, marker='o', label='Coding density')


ax2.yaxis.tick_right()


plt.legend(handles=[plt.Rectangle((0, 0), 1, 1, color=bar_color2),
                    plt.Rectangle((0, 0), 1, 1, color=bar_color1),
                    line[0]],
           labels=['Average gene lengths(bp)', 'Number of genes', 'Coding density (%)'],
           loc='upper right')


plt.title('Gene Comparison')
plt.xlabel('Genes')
ax2.set_yticklabels(['{:,.0%}'.format(x) for x in ax2.get_yticks()])

plt.grid(False)
plt.show()
