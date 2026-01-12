NHS Learning Disability and Autism Data Analysis (Feb 2024)
This repository contains a data analysis and visualization project using official NHS England inpatient statistics for individuals with learning disabilities and autism.

Project Overview
Data Source: NHS England (Learning Disability and Autism Statistics)

Period: February 2024

Tools: Python (Pandas, Matplotlib, Seaborn)

Focus: Patient demographics and hospital length of stay (LOS) analysis

Key Insights
1. Diagnosis Distribution

Analysis of Table 2.2 shows that the number of patients diagnosed with Autism is approximately 13% higher than those with a Learning Disability only. This trend indicates a growing requirement for autism-specific clinical pathways.

2. Demographic Trends

Age Analysis: According to Table 4.6, there is a high concentration of inpatients in the 18-24 age group. This highlights the importance of transition-age support as patients move from child to adult services.

Ethnicity: While the majority of patients identify as White (Table 2.1), monitoring the distribution across all ethnic groups is essential to identify and address potential health inequalities in service access.

3. Length of Stay (LOS)

Long-Stay Challenges: Analysis of Table 2.7 reveals that over 40% of total inpatients have been in hospital care for more than 2 years.

Discharge Bottlenecks: The presence of patients with a length of stay exceeding 10 years suggests significant barriers in transitioning from inpatient units to community-based support systems.

Technical Implementation
Data Preprocessing

Converted non-numeric values (e.g., privacy-protected '*' symbols) into a numerical format to enable statistical calculation.

Isolated key metrics from various sub-tables (1.1, 2.1, 2.7, 4.6) for targeted analysis.

Visualization Strategy

Utilized Seaborn subplots to provide a side-by-side comparison of different demographic variables.

Applied professional color scales (Viridis, Magma, Flare) to improve data readability and presentation quality.

How to Run
Clone the repository: git clone https://github.com/sk8erboi00/nhs-autism-data-analysis.git

Install required packages: pip install pandas matplotlib seaborn

Run the script: python scripts/analysis_full.py

Developed by [Hyeon-Gu Lee]. Part of a health data analytics portfolio.
