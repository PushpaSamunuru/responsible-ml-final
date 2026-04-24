import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from pathlib import Path

# Paths
base_dir = Path(__file__).resolve().parents[1]
telemetry_file = base_dir / "telemetry" / "reco_logs.csv"
figures_dir = base_dir / "figures"
figures_dir.mkdir(exist_ok=True)

# Load data
df = pd.read_csv(telemetry_file)

# Parse recommended items
all_items = []
user_lists = []

for items_str in df["recommended_items"]:
    items = str(items_str).split()
    user_lists.append(items)
    all_items.extend(items)

# Basic metrics
total_recommendations = len(all_items)
unique_items = len(set(all_items))
diversity_score = unique_items / total_recommendations if total_recommendations else 0

item_counts = Counter(all_items)
top_items = item_counts.most_common(10)

# Exposure concentration
top_5_exposure = sum(count for _, count in item_counts.most_common(5))
top_5_share = top_5_exposure / total_recommendations if total_recommendations else 0

# Personalization proxy:
# Count how many unique recommendation lists exist
unique_lists = len(set(tuple(lst) for lst in user_lists))

# Summary table
summary_df = pd.DataFrame({
    "Metric": [
        "Number of users tested",
        "Total recommended items",
        "Unique recommended items",
        "Diversity score",
        "Top-5 exposure share",
        "Unique recommendation lists"
    ],
    "Value": [
        len(df),
        total_recommendations,
        unique_items,
        round(diversity_score, 4),
        round(top_5_share, 4),
        unique_lists
    ]
})

summary_csv = figures_dir / "fairness_summary_table.csv"
summary_df.to_csv(summary_csv, index=False)

print("Fairness Summary")
print(summary_df.to_string(index=False))

# Exposure plot
plot_df = pd.DataFrame(top_items, columns=["item_id", "count"])

plt.figure(figsize=(8, 5))
plt.bar(plot_df["item_id"].astype(str), plot_df["count"])
plt.xlabel("Item ID")
plt.ylabel("Recommendation Count")
plt.title("Top Recommended Items by Exposure")
plt.tight_layout()

plot_path = figures_dir / "fairness_exposure_plot.png"
plt.savefig(plot_path, dpi=200)
plt.close()

print(f"\nSaved summary table to: {summary_csv}")
print(f"Saved plot to: {plot_path}")