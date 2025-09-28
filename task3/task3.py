import pandas as pd
import numpy as np

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, np.nan, 30, 45, np.nan],
    'Score': [85, 90, np.nan, 70, 95],
    'Department': ['HR', 'Finance', 'HR', 'IT', 'Finance']
}

df = pd.DataFrame(data)
print(df)

df_clean = df.dropna()
print(df_clean)

df['Age'] = df['Age'].fillna(df['Age'].mean())    # fill Age with mean
df['Score'] = df['Score'].fillna(df['Score'].mean())

avg_scores = df_clean.groupby('Department')['Score'].mean()
print(avg_scores)

agg_result = df_clean.groupby('Department').agg({
    'Age': 'mean',
    'Score': ['mean', 'max']
})
print(agg_result)