import matplotlib.pyplot as plt


def show_graph(df):

    if df.empty:
        print("\nNo data available for graph.")
        return

    subject_time = df.groupby("Subject")["Duration"].sum()

    subject_time.plot(kind="bar")

    plt.title("Study Time by Subject")
    plt.xlabel("Subject")
    plt.ylabel("Study Time (minutes)")

    plt.tight_layout()

    plt.show()