# Create new column based on color condition
df['ModifiedColor'] = df.apply(lambda row: '#' + row['Color'] if row['Color'] == 'Red' else row['Color'], axis=1)

print(df)
