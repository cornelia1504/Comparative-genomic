# 1
import pandas as pd
file_path1 = r'D:\0-AMU\DLAD\6-GecO\PROJET-TP1\ftp-files\GCF_000024945.1_feature_table\GCF_000024945.1.txt'
df = pd.read_csv(file_path1, delimiter='\t')
filtered_df = df[(df['# feature'] == 'CDS') & (df['class'] == 'with_protein')]
total_cds_coding = filtered_df['feature_interval_length'].sum()
predicted_cds = len(filtered_df)
mean_cds = int(round(total_cds_coding/predicted_cds))
maximal_cds = filtered_df['feature_interval_length'].max()
print(maximal_cds)
coding_density = "{:.2f}%".format((total_cds_coding/2132142) * 100)
print(coding_density)
print(total_cds_coding)

# CDS whole length
import pandas as pd

file_path1 = r'D:\0-AMU\DLAD\6-GecO\PROJET-TP1\ftp-files\GCF_000024945.1_feature_table\GCF_000024945.1.txt'
df = pd.read_csv(file_path1, delimiter='\t')

filtered_df = df[df['# feature'] == 'CDS']
total_cds_coding = filtered_df['feature_interval_length'].sum()


#1.1
import pandas as pd
file_path = r'D:\0-AMU\DLAD\6-GecO\PROJET-TP1\ftp-files\1.1-GCF_026057735.1\GCF_026057735.1_ASM2605773v1_feature_table.txt'
df = pd.read_csv(file_path, delimiter='\t')
filtered_df = df[(df['# feature'] == 'CDS') & (df['class'] == 'with_protein')]
total_cds_coding = filtered_df['feature_interval_length'].sum()
predicted_cds = len(filtered_df)
mean_cds = int(round(total_cds_coding/predicted_cds))
maximal_cds = filtered_df['feature_interval_length'].max()
print(maximal_cds)
coding_density = "{:.2f}%".format((total_cds_coding/2205714) * 100)
print(coding_density)
print(total_cds_coding)
#1.2
import pandas as pd
file_path = r'D:\0-AMU\DLAD\6-GecO\PROJET-TP1\ftp-files\1.2-GCF_013393365.1\GCF_013393365.1_ASM1339336v1_feature_table.txt'
df = pd.read_csv(file_path, delimiter='\t')
filtered_df = df[(df['# feature'] == 'CDS') & (df['class'] == 'with_protein')]
total_cds_coding = filtered_df['feature_interval_length'].sum()
predicted_cds = len(filtered_df)
mean_cds = int(round(total_cds_coding/predicted_cds))
maximal_cds = filtered_df['feature_interval_length'].max()
print(maximal_cds)
coding_density = "{:.2f}%".format((total_cds_coding/2097818) * 100)
print(coding_density)
print(total_cds_coding)
#2.1
import pandas as pd
file_path = r'D:\0-AMU\DLAD\6-GecO\PROJET-TP1\ftp-files\2.1-GCF_003010495.1\GCF_003010495.1_ASM301049v1_feature_table.txt'
df = pd.read_csv(file_path, delimiter='\t')
filtered_df = df[(df['# feature'] == 'CDS') & (df['class'] == 'with_protein')]
total_cds_coding = filtered_df['feature_interval_length'].sum()
predicted_cds = len(filtered_df)
mean_cds = int(round(total_cds_coding/predicted_cds))
maximal_cds = filtered_df['feature_interval_length'].max()
print(maximal_cds)
coding_density = "{:.2f}%".format((total_cds_coding/2478942) * 100)
print(coding_density)
print(total_cds_coding)
#2.2
import pandas as pd
file_path = r'D:\0-AMU\DLAD\6-GecO\PROJET-TP1\ftp-files\2.2-GCF_900343095.1\GCF_900343095.1_PRJEB25867_feature_table.txt'
df = pd.read_csv(file_path, delimiter='\t')
filtered_df = df[(df['# feature'] == 'CDS') & (df['class'] == 'with_protein')]
total_cds_coding = filtered_df['feature_interval_length'].sum()
predicted_cds = len(filtered_df)
mean_cds = int(round(total_cds_coding/predicted_cds))
maximal_cds = filtered_df['feature_interval_length'].max()
print(maximal_cds)
coding_density = "{:.2f}%".format((total_cds_coding/2320245) * 100)
print(coding_density)
print(total_cds_coding)


