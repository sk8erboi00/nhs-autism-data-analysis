import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('LD_AT_Feb2024.csv')
df['Value'] = pd.to_numeric(df['Value'].replace('*', '0'), errors='coerce').fillna(0)


age_autism = df[(df['Table'] == 4.6) & (df['Dimension2'] == 'Aut')].copy()

ethnicity_df = df[(df['Table'] == 2.1) & (df['Measure'] == 'Ethnicity')].copy()

fig, ax = plt.subplots(1, 2, figsize=(22, 8))
sns.set_theme(style="whitegrid")

if not ethnicity_df.empty:
    sns.barplot(data=ethnicity_df, x='Value', y='Dimension', ax=ax[0],
                hue='Dimension', palette='rocket', legend=False)
    ax[0].set_title('Overall Patient Distribution by Ethnicity (Table 2.1)', fontsize=15)
    ax[0].set_xlabel('Number of Patients')

if not age_autism.empty:
    sns.barplot(data=age_autism, x='Value', y='Dimension', ax=ax[1],
                hue='Dimension', palette='viridis', legend=False)
    ax[1].set_title('Autism Patient Distribution by Age Group (Table 4.6)', fontsize=15)
    ax[1].set_xlabel('Number of Patients')

plt.tight_layout()
plt.show()

print("--- NHS Data Analysis Summary ---")
if not age_autism.empty:
    top_age = age_autism.loc[age_autism['Value'].idxmax(), 'Dimension']
    print(f"The most prevalent age group among autism inpatients: {top_age}")
if not ethnicity_df.empty:
    top_eth = ethnicity_df.loc[ethnicity_df['Value'].idxmax(), 'Dimension']
    print(f"Most represented ethnic group among all service users: {top_eth}")