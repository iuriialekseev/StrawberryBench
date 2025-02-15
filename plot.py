import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def plot_heatmap(pivot_df, title, save_path=None, dpi=300):
    plt.figure(figsize=(12, 7))
    ax = sns.heatmap(
        pivot_df,
        annot=True,
        fmt=".0f",
        cmap="RdYlGn",
        cbar=True,
        cbar_kws={'shrink': 0.5},
        linewidths=0.5
    )

    ax.xaxis.tick_top()
    ax.tick_params(axis='x', which='both', length=0)
    ax.xaxis.set_label_position('top')

    cbar = ax.collections[0].colorbar
    cbar.set_label('Accuracy (%)')

    ax.set_xlabel("Additional R's / Average", fontsize=12)
    ax.set_ylabel("Model", fontsize=12)
    ax.set_title(title, pad=30, fontsize=14)

    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=dpi)
    plt.show()


def plot_bar_chart(df, title, save_path=None, dpi=300):
    # Define provider colors
    provider_colors = {
        'openai': '#74AA9C',
        'anthropic': '#D4C5B9',
        'google': '#669DF7',
        'meta-llama': '#044EAB',
        'mistralai': '#F54E42',
        'x-ai': '#000000',
        'qwen': '#8C564B',
        'deepseek': '#E377C2',
    }

    # Group by model to calculate the average accuracy
    grouped = df.groupby("model").agg(
        average_accuracy=("accuracy", "mean"),
        provider=("provider", "first")
    ).reset_index()

    # Select the top 20 models by average accuracy
    top_models = grouped.sort_values("average_accuracy", ascending=False).head(20)[::-1]
    colors = [provider_colors.get(provider.lower(), "#333333") for provider in top_models["provider"]]

    plt.figure(figsize=(12, 7))
    ax = plt.gca()
    bars = ax.barh(top_models["model"], top_models["average_accuracy"], color=colors)

    # Add accuracy labels on each bar
    for bar in bars:
        width = bar.get_width()
        ax.text(width, bar.get_y() + bar.get_height() / 2, f' {width:.0f}%', va='center', ha='left', fontsize=10)

    # Create legend
    legend_handles = [
        mpatches.Patch(color=provider_colors.get(provider.lower(), "#333333"), label=provider)
        for provider in top_models["provider"].unique()
    ]
    ax.legend(handles=legend_handles, loc='lower right')

    ax.set_xlim(0, 100)
    ax.set_xlabel("Average Accuracy (%)", fontsize=12)
    ax.set_ylabel("Model", fontsize=12)
    ax.set_title(title, fontsize=14)

    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=dpi)
    plt.show()


def plot_all(json_filename, save_plots=False, dpi=300):
    df = pd.read_json(json_filename)

    # Split provider and model from the 'model' field
    df["provider"] = df["model"].apply(lambda x: x.split("/")[0])
    df["model"] = df["model"].apply(lambda x: x.split("/")[-1])

    # Split data based on whether chain-of-thought (CoT) is used
    df_cot = df[df["cot"]]
    df_nocot = df[~df["cot"]]

    # Create a pivot table for heatmaps
    def create_pivot(sub_df):
        pivot = sub_df.pivot(index="model", columns="additional_rs", values="accuracy")
        pivot["average"] = pivot.mean(axis=1)
        return pivot.sort_values("average", ascending=False)

    sns.set_theme(style="white")

    # Plot for CoT records if available
    if not df_cot.empty:
        pivot_cot = create_pivot(df_cot)
        heatmap_save_path = "assets/heatmap_cot.png" if save_plots else None
        bar_chart_save_path = "assets/bar_chart_cot.png" if save_plots else None
        plot_heatmap(pivot_cot, "StrawberryBench with CoT", save_path=heatmap_save_path, dpi=dpi)
        plot_bar_chart(df_cot, "StrawberryBench Top Models with CoT", save_path=bar_chart_save_path, dpi=dpi)
    else:
        print("No records with CoT. Skipping CoT plots.")

    # Plot for non-CoT records if available
    if not df_nocot.empty:
        pivot_nocot = create_pivot(df_nocot)
        heatmap_save_path = "assets/heatmap_nocot.png" if save_plots else None
        bar_chart_save_path = "assets/bar_chart_nocot.png" if save_plots else None
        plot_heatmap(pivot_nocot, "StrawberryBench without CoT", save_path=heatmap_save_path, dpi=dpi)
        plot_bar_chart(df_nocot, "StrawberryBench Top Models without CoT", save_path=bar_chart_save_path, dpi=dpi)
    else:
        print("No records without CoT. Skipping non-CoT plots.")

if __name__ == "__main__":
    plot_all("results.json", save_plots=True, dpi=300)
