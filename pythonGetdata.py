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
ax = sns.barplot(x="Year", y="Value", data=df, palette=palette, alpha=0.8)

for i, v in enumerate(df["Value"]):
    ax.text(i, v + 5, str(v), color='black', ha='center', fontweight='bold')

change_yag = ((df["Value"][1] - df["Value"][0]) / df["Value"][0]) * 100  # 2024 vs 2023
change_budget = ((df["Value"][2] - df["Value"][1]) / df["Value"][1]) * 100  # Budget vs 2024


ax.annotate("+1%", xy=(0.5, 995), xytext=(0.5, 1020),
             textcoords="data", ha='center', fontsize=10,
             arrowprops=dict(arrowstyle='->', color='black'))
ax.annotate("-1%", xy=(1.5, 1000), xytext=(1.5, 1020),
             textcoords="data", ha='center', fontsize=10,
             arrowprops=dict(arrowstyle='->', color='black'))

ax.set_title("2024 vs YAG vs BUDGET", fontweight='bold')
ax.set_ylabel("")

sns.despine(left=True, bottom=True)

plt.show()
