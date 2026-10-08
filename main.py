from data_manager import load_data, add_session, edit_session, delete_session
from analysis import show_analysis
from visualization import show_graph


def main():

    while True:

        print("\n========== STUDY TRACKER ==========")
        print("1. Add Study Session")
        print("2. View Sessions")
        print("3. Edit Study Session")
        print("4. Delete Study Session")
        print("5. Analyze Study Data")
        print("6. Show Graph")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        # 1. ADD
        if choice == "1":

            try:
                subject = input("Enter subject: ")
                date = input("Enter date (DD-MM-YYYY): ")

                duration = float(
                    input("Enter study duration in minutes: ")
                )

                if duration <= 0:
                    print("Duration must be greater than 0.")
                    continue

                details = input("Enter study details: ")

                add_session(
                    subject,
                    date,
                    duration,
                    details
                )

            except ValueError:
                print("Please enter a valid number for duration.")

        # 2. VIEW
        elif choice == "2":

            df = load_data()

            print("\n========== STUDY SESSIONS ==========")

            if df.empty:
                print("No study sessions recorded.")
            else:

                for i, row in df.iterrows():

                    print(
                        f"\nSession {i + 1}"
                    )

                    print(
                        f"Subject: {row['Subject']}"
                    )

                    print(
                        f"Date: {row['Date']}"
                    )

                    print(
                        f"Duration: {row['Duration']} minutes"
                    )

                    print(
                        f"Details: {row['Details']}"
                    )

            input("\nPress Enter to return to menu...")

        # 3. EDIT
        elif choice == "3":

            df = load_data()

            if df.empty:
                print("\nNo sessions available to edit.")
                continue

            print("\n========== STUDY SESSIONS ==========")

            for i, row in df.iterrows():

                print(
                    f"{i + 1}. "
                    f"{row['Subject']} | "
                    f"{row['Date']} | "
                    f"{row['Duration']} min | "
                    f"{row['Details']}"
                )

            try:

                number = int(
                    input("\nEnter session number to edit: ")
                )

                index = number - 1

                if index < 0 or index >= len(df):
                    print("Invalid session number.")
                    continue

                subject = input("Enter new subject: ")
                date = input("Enter new date: ")

                duration = float(
                    input("Enter new duration: ")
                )

                details = input("Enter new details: ")

                edit_session(
                    index,
                    subject,
                    date,
                    duration,
                    details
                )

            except ValueError:
                print("Invalid input.")

        # 4. DELETE
        elif choice == "4":

            df = load_data()

            if df.empty:
                print("\nNo sessions available to delete.")
                continue

            print("\n========== STUDY SESSIONS ==========")

            for i, row in df.iterrows():

                print(
                    f"{i + 1}. "
                    f"{row['Subject']} | "
                    f"{row['Date']} | "
                    f"{row['Duration']} min | "
                    f"{row['Details']}"
                )

            try:

                number = int(
                    input("\nEnter session number to delete: ")
                )

                index = number - 1

                if index < 0 or index >= len(df):
                    print("Invalid session number.")
                    continue

                confirm = input(
                    "Are you sure? (y/n): "
                )

                if confirm.lower() == "y":
                    delete_session(index)
                else:
                    print("Deletion cancelled.")

            except ValueError:
                print("Invalid input.")

        # 5. ANALYSIS
        elif choice == "5":

            df = load_data()

            show_analysis(df)

            input("\nPress Enter to return to menu...")

        # 6. GRAPH
        elif choice == "6":

            df = load_data()

            show_graph(df)

        # 7. EXIT
        elif choice == "7":

            print("\nThank you for using Study Tracker!")
            break

        else:

            print("\nInvalid choice. Please enter 1-7.")


if __name__ == "__main__":
    main()