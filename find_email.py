import pandas as pd
df = pd.read_csv("result.csv")

# basic data cleanse
df = df[df['name'].str.split().str.len() <= 2]
pattern = r'.+at Fortress'
df = df[df['job'].str.contains(pattern, regex=True, na=False)]

# get emails
df['email'] = df['name'].str.extract(r'(\w)\w*\s(\w+)', expand=False).apply('.'.join, axis=1)
df['email'] = df['email'] + "@fortress.com"

# create new csv
df.to_csv('df.csv', index=False)

df