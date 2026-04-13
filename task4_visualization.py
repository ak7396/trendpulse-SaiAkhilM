import pandas as pd
import matplotlib.pyplot as plt
import os
#loading data
df = pd.read_csv("data/trends_analysed.csv")#read file
# Create  folder if not exists
os.makedirs("outputs", exist_ok=True)
# Chart 1: Top 10 Stories by Score
# Sort data by score (descending) and take top 10
top10 = df.sort_values(by="score", ascending=False).head(10)

# Shorten long titles (max 50 characters)
top10["short_title"] = top10["title"].apply(lambda x: x[:50] + "..." if len(x) > 50 else x)

# Create horizontal bar chart
plt.figure(figsize=(10, 6))
plt.barh(top10["short_title"], top10["score"])
plt.xlabel("Score")
plt.ylabel("Story Title")
plt.title("Top 10 Stories by Score")

# Invert y-axis so highest score is on top
plt.gca().invert_yaxis()

# Save chart
plt.savefig("outputs/chart1_top_stories.png")
plt.show()
plt.close()

# Chart 2:Stories per Category

category_counts = df["category"].value_counts()

plt.figure()
plt.bar(category_counts.index, category_counts.values)

plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.title("Stories per Category")

plt.savefig("outputs/chart2_categories.png")
plt.show()
plt.close()

# Chart 3: Score vs Comments
# Split data
popular = df[df["is_popular"] == True]
not_popular = df[df["is_popular"] == False]

plt.figure()

plt.scatter(popular["score"], popular["num_comments"], label="Popular")
plt.scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")

plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.title("Score vs Comments")
plt.legend()

plt.savefig("outputs/chart3_scatter.png")
plt.show()
plt.close()

# Bonus: Dashboard

fig, axes = plt.subplots(1, 3)

# Chart 1
axes[0].barh(top10["short_title"], top10["score"])
axes[0].set_title("Top Stories")
axes[0].invert_yaxis()

# Chart 2
axes[1].bar(category_counts.index, category_counts.values)
axes[1].set_title("Stories per Category")
axes[1].set_xlabel("Category")
axes[1].set_ylabel("Count")

# Chart 3
axes[2].scatter(popular["score"], popular["num_comments"], label="Popular")
axes[2].scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")
axes[2].set_title("Score vs Comments")
axes[2].legend()

plt.suptitle("TrendPulse Dashboard")

plt.savefig("outputs/dashboard.png")
plt.show()
plt.close()

print("Charts created successfully!")