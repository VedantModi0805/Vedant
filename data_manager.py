import pandas as pd
import os

FILE = "study_data.csv"


def load_data():
    if os.path.exists(FILE):
        return pd.read_csv(FILE)

    return pd.DataFrame(
        columns=["Subject", "Date", "Duration", "Details"]
    )


def add_session(subject, date, duration, details):

    df = load_data()

    new_session = pd.DataFrame([{
        "Subject": subject,
        "Date": date,
        "Duration": duration,
        "Details": details
    }])

    df = pd.concat([df, new_session], ignore_index=True)

    df.to_csv(FILE, index=False)

    print("\nStudy session added successfully!")


def edit_session(index, subject, date, duration, details):

    df = load_data()

    if index < 0 or index >= len(df):
        print("Invalid session number.")
        return

    df.loc[index, "Subject"] = subject
    df.loc[index, "Date"] = date
    df.loc[index, "Duration"] = duration
    df.loc[index, "Details"] = details

    df.to_csv(FILE, index=False)

    print("\nStudy session updated successfully!")


def delete_session(index):

    df = load_data()

    if index < 0 or index >= len(df):
        print("Invalid session number.")
        return

    df = df.drop(index)

    df = df.reset_index(drop=True)

    df.to_csv(FILE, index=False)

    print("\nStudy session deleted successfully!")