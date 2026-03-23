import os

log_file_name = ""
filters = {
    "WARNING": 0,
    "ERROR": 0,
    "EMERGENCY": 0,
    "CRITICAL": 0,
    "DEBUG": 0,
    "INFO": 0,
    "TRACE": 0,
    "ALERT": 0,
    "AUDIT": 0,
    "SECURITY": 0,
    "NOTICE": 0,
    "VERBOSE": 0,
}
Change_file = False

# Clear CLI function
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# Functions for reading log file
def start():
    try:
        clear_screen()  # Clear screen when starting reading

        if not Change_file:
            print("You haven't selected a Log file\nReturning to main menu")
            return

        if not filters:
            print("Filters are empty, returning to main menu")
            return

        # Reset filter counts
        for key in filters:
            filters[key] = 0

        # Normalize filter keys to uppercase
        words_to_check = set(key.upper() for key in filters.keys())

        # Try opening the file safely
        try:
            with open(log_file_name, "r") as f:
                for line in f:
                    line_upper = line.upper()
                    for word in words_to_check:
                        if word in line_upper:
                            filters[word] += 1
        except FileNotFoundError:
            print(f"Error: The file '{log_file_name}' was not found.")
            return
        except IOError as e:
            print(f"Error reading file: {e}")
            return

        print("----- Finished! -----")
        for word, count in filters.items():
            print(f"Found {word} {count} times")

    except Exception as e:
        print(f"An unexpected error occurred in start(): {e}")


def edit_filters():
    try:
        clear_screen()  # Clear screen when editing filters
        print("What do you want to do?")
        print("1 - Add Filters")
        print("2 - Delete Filters")
        print("3 - Remove all filters")
        print("0 - Main menu")
        print()
        choice = input("choice? ")

        if choice == "1":
            print("\nType in a filter to add\n")
            filter_name = input("name? ").upper()

            if filter_name in filters:
                print(f"{filter_name} is already inside the log file")
            else:
                filters[filter_name] = 0
                print(f"{filter_name} added to filters")

        elif choice == "2":
            if not filters:
                print("No filters to delete.")
                return
            print("\nType the name of the filter to delete")
            print("Index\tName")
            print("-----------------------")
            for index, word in enumerate(filters):
                print(f"{index}\t{word}")
            print("-----------------------\n")

            name = input("name? ").upper()
            if name in filters:
                del filters[name]
                print(f"{name} has been removed from filters")
            else:
                print(f"{name} does not exist")

        elif choice == "3":
            filters.clear()
            print("Removed every filter")

        elif choice == "0":
            return

        else:
            print("Invalid choice, returning to menu")

    except Exception as e:
        print(f"An unexpected error occurred in edit_filters(): {e}")


def choose_log():
    global Change_file
    global log_file_name
    try:
        clear_screen()  # Clear screen when choosing a log
        log_name = input("Type in the name of the log file: ")

        if os.path.exists(log_name):
            log_file_name = log_name
            print(f"{log_name} was chosen")
            Change_file = True
        else:
            print(f"File '{log_name}' doesn't exist. Make sure it's in the same directory as the Python script")

    except Exception as e:
        print(f"An unexpected error occurred in choose_log(): {e}")


def main():
    try:
        while True:
            clear_screen()  # Clear screen each time the main menu is shown
            print("=================================")
            print("  Log Reader 1.1 / metric-vac")
            print("=================================")
            print()
            print(f"Log file = {log_file_name if Change_file else 'None'}")
            print()
            print("1 - Choose Log file")
            print("2 - Edit Filters")
            print("3 - Start Reading")
            print("0 - Exit")
            print()

            choice = input("choice? ")

            if choice == "1":
                choose_log()
            elif choice == "2":
                edit_filters()
            elif choice == "3":
                start()
            elif choice == "0":
                print("Exiting...")
                break
            else:
                print("Invalid choice, try again.")

            input("\nPress Enter to continue...")  # Pause so user can see messages

    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting safely...")
    except Exception as e:
        print(f"An unexpected error occurred in main(): {e}")


if __name__ == "__main__":
    main()
