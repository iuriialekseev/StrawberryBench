import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


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
    ax.set_title(title, pad=20, fontsize=14)

    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=300)
    plt.show()


def plot_bar_chart(df, title, save_path=None, limit=None, add_cot_label=False):
    provider_colors = {
        "openai": "#74AA9C",
        "anthropic": "#D4C5B9",
        "google": "#669DF7",
        "meta-llama": "#044EAB",
        "mistralai": "#F54E42",
        "x-ai": "#000000",
        "qwen": "#8C564B",
        "deepseek": "#E377C2",
    }

    plot_df = df.copy()

    if add_cot_label:
        plot_df["display_model"] = plot_df.apply(
            lambda row: f"{row['model']} (cot)"
            if row["type"] == "cot"
            else row["model"],
            axis=1,
        )
    else:
        plot_df["display_model"] = plot_df["model"]

    grouped = (
        plot_df.groupby("display_model")
        .agg(average_accuracy=("accuracy", "mean"), provider=("provider", "first"))
        .reset_index()
    )

    top_models = grouped.sort_values("average_accuracy", ascending=False)
    if limit:
        top_models = top_models[:limit]

    top_models = top_models[::-1]

    colors = [
        provider_colors.get(provider.lower(), "#333333")
        for provider in top_models["provider"]
    ]

    plt.figure(figsize=(12, 7))
    ax = plt.gca()
    bars = ax.barh(
        top_models["display_model"],
        top_models["average_accuracy"],
        color=colors,
    )

    for bar in bars:
        width = bar.get_width()
        ax.text(
            width,
            bar.get_y() + bar.get_height() / 2,
            f" {width:.0f}%",
            va="center",
            ha="left",
            fontsize=10,
        )

    unique_providers = sorted(top_models["provider"].unique(), key=str.lower)
    legend_handles = [
        mpatches.Patch(
            color=provider_colors.get(provider.lower(), "#333333"),
            label=provider,
        )
        for provider in unique_providers
    ]
    ax.legend(handles=legend_handles, loc="lower right")

    ax.set_xlim(0, 100)
    ax.set_xlabel("Average Accuracy (%)", fontsize=12)
    ax.set_ylabel("Model", fontsize=12)
    ax.set_title(title, fontsize=14)

    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=300)
    plt.show()


def create_pivot(sub_df):
    pivot = sub_df.pivot(index="model", columns="additional_rs", values="accuracy")
    return pivot.loc[pivot.mean(axis=1).sort_values(ascending=False).index]


def plot_all(json_filename, save_plots=False):
    df = pd.read_json(json_filename)

    df["provider"] = df["model"].apply(lambda x: x.split("/")[0])
    df["model"] = df["model"].apply(lambda x: x.split("/")[-1])

    df_nocot = df[df["type"] == "nocot"]
    df_cot = df[df["type"] == "cot"]
    df_reasoning = df[df["type"] == "reasoning"]

    sns.set_theme(style="white")

    if not df_nocot.empty:
        pivot_nocot = create_pivot(df_nocot)
        heatmap_save_path = "assets/heatmap_nocot.png" if save_plots else None
        bar_chart_save_path = "assets/bar_chart_nocot.png" if save_plots else None

        plot_heatmap(
            pivot_nocot, "StrawberryBench - Baseline", save_path=heatmap_save_path
        )
        plot_bar_chart(
            df_nocot, "StrawberryBench - Baseline", save_path=bar_chart_save_path
        )
    else:
        print("No records with 'nocot' type. Skipping nocot plots.")

    if not df_cot.empty:
        pivot_cot = create_pivot(df_cot)
        heatmap_save_path = "assets/heatmap_cot.png" if save_plots else None
        bar_chart_save_path = "assets/bar_chart_cot.png" if save_plots else None

        plot_heatmap(pivot_cot, "StrawberryBench - Chain of Thought", save_path=heatmap_save_path)
        plot_bar_chart(
            df_cot, "StrawberryBench - Chain of Thought", save_path=bar_chart_save_path
        )
    else:
        print("No records with 'cot' type. Skipping CoT plots.")

    if not df_reasoning.empty:
        pivot_reasoning = create_pivot(df_reasoning)
        heatmap_save_path = "assets/heatmap_reasoning.png" if save_plots else None
        bar_chart_save_path = "assets/bar_chart_reasoning.png" if save_plots else None

        plot_heatmap(
            pivot_reasoning,
            "StrawberryBench - Reasoning Models",
            save_path=heatmap_save_path,
        )
        plot_bar_chart(
            df_reasoning,
            "StrawberryBench - Reasoning Models",
            save_path=bar_chart_save_path,
        )
    else:
        print("No records with 'reasoning' type. Skipping reasoning plots.")

    if not df.empty:
        leaderboard = "assets/leaderboard.png" if save_plots else None
        plot_bar_chart(
            df,
            "StrawberryBench - Leaderboard - Top 20",
            save_path=leaderboard,
            limit=20,
            add_cot_label=True,
        )
    else:
        print("No records found. Skipping the leaderboard plot.")


if __name__ == "__main__":
    plot_all("results.json", save_plots=True)
