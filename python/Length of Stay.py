import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Data Loading and Preprocessing
df = pd.read_csv('LD_AT_Feb2024.csv')
df['Value'] = pd.to_numeric(df['Value'].replace('*', '0'), errors='coerce').fillna(0)

# 2. Extract Length of Stay Data (Table 2.7)
los_df = df[(df['Table'] == 2.7) & (df['Measure'] == 'LOS')].copy()

# Define chronological order for LOS
los_order = [
    'Up to three months',
    'Three months up to six months',
    'Six months up to one year',
    'One year up to two years',
    'Two years up to five years',
    'Five years up to ten years',
    'More than ten years'
]

# 3. Visualization
plt.figure(figsize=(14, 8))
sns.set_theme(style="whitegrid")

barplot = sns.barplot(
    data=los_df,
    x='Value',
    y='Dimension',
    order=los_order,
    hue='Dimension',
    palette='flare',
    legend=False
)

plt.title('Distribution of Length of Stay (Feb 2024)', fontsize=16, pad=20)
plt.xlabel('Number of Patients', fontsize=12)
plt.ylabel('Duration of Hospitalization', fontsize=12)

# Add data labels to bars
for p in barplot.patches:
    width = p.get_width()
    plt.text(width + 5, p.get_y() + p.get_height()/2, f'{int(width)}', va='center')

plt.tight_layout()
plt.savefig('my_plot3.png')
plt.show()

# 4. Statistical Summary Output
total_patients = los_df['Value'].sum()
long_stay_criteria = ['Two years up to five years', 'Five years up to ten years', 'More than ten years']
long_stay_count = los_df[los_df['Dimension'].isin(long_stay_criteria)]['Value'].sum()
percentage = (long_stay_count / total_patients) * 100

print(f"--- Length of Stay Analysis Summary ---")
print(f"Total Inpatients Analyzed: {int(total_patients)}")
print(f"Long-stay Patients (2+ Years): {int(long_stay_count)}")
print(f"Percentage of Long-stay Patients: {percentage:.1f}%")