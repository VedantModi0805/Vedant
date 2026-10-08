import numpy as np


def show_analysis(df):

    if df.empty:
        print("\nNo study sessions available.")
        return

    durations = np.array(df["Duration"])

    print("\n========== STUDY ANALYSIS ==========")

    print(
        "Total study time:",
        durations.sum(),
        "minutes"
    )

    print(
        "Average session:",
        round(durations.mean(), 2),
        "minutes"
    )

    print(
        "Longest session:",
        durations.max(),
        "minutes"
    )

    print(
        "Shortest session:",
        durations.min(),
        "minutes"
    )

    print("\n----- Subject-wise Study Time -----")

    subject_time = df.groupby("Subject")["Duration"].sum()

    print(subject_time)