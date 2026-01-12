import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'LD_AT_Feb2024.csv'
df = pd.read_csv(file_path)

df['Value'] = pd.to_numeric(df['Value'].replace('*', '0'), errors='coerce').fillna(0)

diagnosis_data = df[(df['Table'] == 2.2) & (df['Measure'] == 'Diagnosis')].copy()

plt.figure(figsize=(12, 7))
sns.set_theme(style="whitegrid")
sns.barplot(data=diagnosis_data, x='Value', y='Dimension', hue='Dimension', palette='viridis', legend=False)

plt.title('NHS Patient Diagnosis Distribution (Feb 2024)', fontsize=15)
plt.xlabel('Number of Patients', fontsize=12)
plt.ylabel('Diagnosis Type', fontsize=12)
plt.tight_layout()

plt.show()

print("--- NHS Data Summary---")
autism_count = diagnosis_data[diagnosis_data['Dimension'] == 'Autism']['Value'].values[0]
ld_count = diagnosis_data[diagnosis_data['Dimension'] == 'Learning disability']['Value'].values[0]
print(f"(Autism) the number of patient : {autism_count}")
print(f"(Learning disability) the number of patient : {ld_count}")