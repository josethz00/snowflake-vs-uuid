import matplotlib.pyplot as plt
import numpy as np

categories = ("UUID", "Snowflake")
commands_means = {
    'Generation': (0.0300, 0.0243),
    'INSERT': (49.2, 36.9),
    'SELECT': (0.0945, 0.1001),
    'SELECT BY ID (WHERE)': (0.0010, 0.0005),
    'SELECT + ORDER BY': (0.1013, 0.1002),
    'UPDATE': (0.00603118, 0.00179332),
}

colors = plt.cm.get_cmap('tab20').colors

fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(12, 6), constrained_layout=True)
axes = axes.flatten()  # Convert 2D array of subplots to 1D

for i, (attribute, measurement) in enumerate(commands_means.items()):
    ax = axes[i]
    y_max = max(measurement) * 1.1

    if attribute == 'INSERT':
        ax.set_ylim(0, y_max)  # Adjust limit for INSERT
    else:
        ax.set_ylim(0, y_max)  # Set common limit for other commands

    rects = ax.bar(categories, measurement, color=colors[:2])
    ax.bar_label(rects, padding=3)

    if attribute in ('SELECT BY ID', 'SELECT + ORDER BY', 'UPDATE'):
        # Add secondary y-axis for milliseconds
        ax2 = ax.twinx()
        y_ticks = [v * 1000 for v in ax.get_yticks()]
        y_labels = [f"{v:.0f} ms" for v in y_ticks]
        ax2.set_yticks(y_ticks)
        ax2.set_yticklabels(y_labels)

    ax.set_title(attribute, fontsize=12)
    ax.set_ylabel('Seconds (s)', fontsize=10)
    ax.grid(axis='y', linestyle='--', alpha=0.5)

plt.show()