import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Year": ["2023", "2024", "Budget"],
    "Value": [983, 993, 999]
}
df = pd.DataFrame(data)


sns.set_theme(style="whitegrid")
palette = ["#B0B0B0", "#8B008B", "#B0B0B0"]  

fig, ax = plt.subplots(figsize=(8, 6))
sns.barplot(x="Year", y="Value", data=df, palette=palette, alpha=0.8, ax=ax)

for i, v in enumerate(df["Value"]):
    ax.text(i, v + 5, str(v), color='black', ha='center', fontweight='bold')

change_yag = ((df["Value"][1] - df["Value"][0]) / df["Value"][0]) * 100  # 2024 vs 2023
change_budget = ((df["Value"][1] - df["Value"][2]) / df["Value"][2]) * 100  # 2024 vs Budget 

change_yag_text = f"{change_yag:+.0f}%"   
change_budget_text = f"{change_budget:+.0f}%"

ax.annotate(change_yag_text, xy=(0.5, 995), xytext=(0.5, 1020),
             textcoords="data", ha='center', fontsize=10)
ax.annotate(change_budget_text, xy=(1.5, 1000), xytext=(1.5, 1020),
             textcoords="data", ha='center', fontsize=10)

line_y = 1010 
line_kwargs = dict(arrowstyle='-', color='black')

# Line between 2023 and 2024
ax.annotate('', xy=(0, line_y), xytext=(1, line_y), arrowprops=line_kwargs)

# Line between 2024 and Budget
ax.annotate('', xy=(1, line_y), xytext=(2, line_y), arrowprops=line_kwargs)

# Title and labels
ax.set_title("2024 vs YAG vs BUDGET", fontweight='bold')
ax.set_ylabel("")
sns.despine(left=True, bottom=True)

plt.show()
