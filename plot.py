import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def plot_heatmap(pivot_df, title, save_path=None):
    plt.figure(figsize=(12, 7))
    ax = sns.heatmap(
        pivot_df,
        annot=True,
        fmt=".0f",
        cmap="Blues",
        cbar=True,
        cbar_kws={"shrink": 0.5},
        linewidths=0.5,
    )

    cbar = ax.collections[0].colorbar
    cbar.set_label("Accuracy (%)")

    ax.set_xlabel("Additional r's", fontsize=12)
    ax.set_ylabel("Model", fontsize=12)
    ax.set_title(title, pad=20, fontsize=14, loc="left", fontweight="bold")

    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=300)
    plt.show()


def plot_bar_chart(df, title, save_path=None, limit=None, add_cot_label=False):
    provider_colors = {
        "openai": "#74AA9C",
        "anthropic": "#D4A27F",
        "google": "#4285F4",
        "meta-llama": "#0064E0",
        "mistralai": "#FF8205",
        "microsoft": "#EF6950",
        "x-ai": "#000000",
        "qwen": "#615CED",
        "deepseek": "#4D6BFE",
        "openrouter": "#8B8D98",
    }

    plot_df = df.copy()

    if add_cot_label:
        plot_df["display_model"] = plot_df.apply(
            lambda row: f"{row['model']} (cot)" if row["type"] == "cot" else row["model"],
            axis=1,
        )
    else:
        plot_df["display_model"] = plot_df["model"]

    plot_df["provider"] = plot_df["provider"].fillna("unknown")

    grouped = plot_df.groupby("display_model").agg(average_accuracy=("accuracy", "mean"), provider=("provider", "first")).reset_index()

    top_models = grouped.sort_values("average_accuracy", ascending=False)

    if limit:
        top_models = top_models[:limit]

    colors = [provider_colors.get(provider.lower(), "#333333") for provider in top_models["provider"]]

    fig, ax = plt.subplots(figsize=(16, 6))

    ax.bar(
        top_models["display_model"],
        top_models["average_accuracy"],
        color=colors,
    )

    unique_providers = sorted(top_models["provider"].unique(), key=str.lower)
    legend_handles = [
        mpatches.Patch(
            color=provider_colors.get(provider.lower(), "#333333"),
            label=provider,
        )
        for provider in unique_providers
    ]

    ax.legend(
        handles=legend_handles, loc="upper center", bbox_to_anchor=(0.5, 1.12), ncol=len(unique_providers), fontsize=14, frameon=False
    )

    ax.set_ylim(0, 100)

    ax.set_ylabel("Average accuracy (%)", fontsize=20, color="gray")
    ax.set_xlabel(None)

    plt.xticks(rotation=45, ha="right", fontsize=16)
    plt.yticks(fontsize=14)

    ax.set_title(title, fontsize=28, loc="left", fontweight="bold", pad=50)

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.show()


def create_pivot(sub_df):
    pivot = sub_df.pivot(index="model", columns="additional_rs", values="accuracy")
    if not pivot.empty:
        pivot = pivot.loc[pivot.mean(axis=1).sort_values(ascending=False).index]
    return pivot


def plot_all(json_filename, save_plots=False):
    df = pd.read_json(json_filename)

    df["provider"] = df["model"].apply(lambda x: x.split("/")[0])
    df["model"] = df["model"].apply(lambda x: x.split("/")[-1])

    df_nocot = df[df["type"] == "nocot"]
    df_cot = df[df["type"] == "cot"]
    df_reasoning = df[df["type"] == "reasoning"]

    sns.set_theme(style="whitegrid")

    if not df_nocot.empty:
        pivot_nocot = create_pivot(df_nocot)
        heatmap_save_path = "results/heatmap_nocot.png" if save_plots else None
        bar_chart_save_path = "results/bar_chart_nocot.png" if save_plots else None

        if not pivot_nocot.empty:
            plot_heatmap(pivot_nocot, "StrawberryBench: Baseline", save_path=heatmap_save_path)
        else:
            print("Pivot table for 'nocot' is empty. Skipping heatmap.")
        plot_bar_chart(df_nocot, "StrawberryBench: Baseline", save_path=bar_chart_save_path, limit=10)
    else:
        print("No records with 'nocot' type. Skipping nocot plots.")

    if not df_cot.empty:
        pivot_cot = create_pivot(df_cot)
        heatmap_save_path = "results/heatmap_cot.png" if save_plots else None
        bar_chart_save_path = "results/bar_chart_cot.png" if save_plots else None

        if not pivot_cot.empty:
            plot_heatmap(pivot_cot, "StrawberryBench: Chain of Thought", save_path=heatmap_save_path)
        else:
            print("Pivot table for 'cot' is empty. Skipping heatmap.")
        plot_bar_chart(df_cot, "StrawberryBench: Chain of Thought", save_path=bar_chart_save_path, limit=10)
    else:
        print("No records with 'cot' type. Skipping CoT plots.")

    if not df_reasoning.empty:
        pivot_reasoning = create_pivot(df_reasoning)
        heatmap_save_path = "results/heatmap_reasoning.png" if save_plots else None
        bar_chart_save_path = "results/bar_chart_reasoning.png" if save_plots else None

        if not pivot_reasoning.empty:
            plot_heatmap(
                pivot_reasoning,
                "StrawberryBench: Reasoning",
                save_path=heatmap_save_path,
            )
        else:
            print("Pivot table for 'reasoning' is empty. Skipping heatmap.")
        plot_bar_chart(
            df_reasoning,
            "StrawberryBench: Reasoning",
            save_path=bar_chart_save_path,
            limit=10,
        )
    else:
        print("No records with 'reasoning' type. Skipping reasoning plots.")

    if not df.empty:
        leaderboard_save_path = "results/leaderboard.png" if save_plots else None
        plot_bar_chart(
            df,
            "StrawberryBench: Results",
            save_path=leaderboard_save_path,
            limit=10,
            add_cot_label=True,
        )
    else:
        print("DataFrame is empty. Skipping the leaderboard plot.")


if __name__ == "__main__":
    plot_all("results/results.json", save_plots=True)
