import pandas as pd

# reading a csv file
df = pd.read_csv("trendpulse-SaiAkhilM/data/trends_clean.csv", delimiter=',')

# printing first 5 rows
print(f"First 5 rows:\n{df.head(5)}")

# printing shape
print(f"\nShape of df is: {df.shape}")

# average of score and num_comments using numeric_only it will fetch avg of numerical columns
print(f"\nAverage of score and num_comments:\n{df.mean(numeric_only=True)}")

# calculating statistics for score column
mean_val = df['score'].mean()
median_val = df['score'].median()
std_val = df['score'].std()
max_val = df['score'].max()
min_val = df['score'].min()

print(f"""
--- Score Stats ---
Mean score   : {mean_val:,.0f}
Median score : {median_val:,.0f}
Std deviation: {std_val:,.0f}
Max score    : {max_val:,.0f}
Min score    : {min_val:,.0f}
""")

# categories with more number of stories
print(f"Categories with more number of stories:\n{df.groupby('category').size().sort_values(ascending=False).head(1)}")

print("-" * 20)

# finding story with maximum comments
max_comments = df['num_comments'].max()
df[df['num_comments'] == max_comments]

print("most commented story:")
print(df.loc[df['num_comments'].idxmax(), ['title', 'num_comments']])

df['engagement']= df['num_comments'] / (df['score']+1)#added a new column which is 	num_comments / (score + 1) — how much discussion a story gets per upvote'''
df['is_popular']=df['score'] > mean_val
#print(df.head())
df.to_csv("trendpulse-SaiAkhilM/data/trends_analysed.csv", index=False)
print("Saved to data/trends_analysed.csv")