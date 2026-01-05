import os

flag_list = ["error", "warning", "critical"]
result = {flag: 0 for flag in flag_list}

changed_log = False
log_file = "test.txt"

def Sel_log():
    global log_file
    global changed_log
    print("Log selecter selected")
    print("Enter the name of the log file(with extension)")
    print()
    name = input("log? ")
    
    try:
        name = name.lower()
    except KeyboardInterrupt:
        print("Thank you for using Log Reader")
        start()
    except Exception as e:
        print(f"Unknown Error: {e}")
        start()


    if name == "":
        print("Nothing has been entered. Sending back to program")
        start()
    if os.path.exists(name):
        log_file = name
        changed_log = True
        print(f"{log_file} has been selected")
        start()
        
    else:
        print(f"File {log_file} doesnt exists, sending to main menu")
        start()



def filt_log():
    print()
    print("Filter selected")
    print()
    print(" ------------------- \n1 - Add Flag\n2 - Remove Flag\n ------------------- ")
    print()

    try:
        choice = int(input("choice? "))
        if choice == 1:
            
            print()
            print("Add Filter Selected, Enter the flag")
            print("Added Filters:")
            print("----------------")
            for flag in flag_list:
                print(flag)
            print("----------------")
            print()
            new_flag = input("flag? ").lower()
            if new_flag in flag_list:
                print(f"{new_flag} already exsists, sending to menu")
                start()
            else:
                flag_list.append(new_flag)
                result[new_flag] = 0
                start()

        elif choice == 2:
            
            print()
            print("Remove Filter Selected, Enter the flag")
            print("Added Filters:")
            print("----------------")
            for flag in flag_list:
                print(flag)
            print("----------------")
            print()
            old_flag = input("flag? ").lower()
            if old_flag in flag_list:
                flag_list.remove(old_flag)
                del result[old_flag]
                print(f"{old_flag} has been deleted")
                start()
            else:
                print(f"{old_flag} doesnt exists in the list, sending to menu")
                start()

        else:
            print("Nothing was selectws, sending back to menu")
            start()
    
    except ValueError:
        print(f"{choice} is invalid, sending to main menu")
        start()



def main():
    if changed_log == False:
        print("You havent selected the log file, it will read the default txt file in the directory\nare you sure you want to do that?")
        print()
        choice = input("yes/no? ").lower()
        if choice == "no":
            print("Reading cancelled, senidng back to main menu")
            start()


    with open(log_file, "r") as file:
        for line in file:                  
            line_lower = line.lower()
            for flag in flag_list:         
                if flag in line_lower:
                    result[flag] += 1

    
    print(" --- READING COMPLETE --- ")
    print()
    print(" --- Results --- ")
    with open(f"result_{log_file}.txt", "a") as files:
        files.write(f"RESULTS OF {log_file}\n")
        files.write("--------------\n")

        for flag, count in result.items():
            
            output_line = f"{flag}: {count}\n"
            print(output_line, end="")
            files.write(output_line)
    
    print(f"Results have been saved to 'result_{log_file}.txt'")
    start()
    
    

    


def start():
    print()
    print(" -- Welcome to Log Reader - by Nebil Nasser -- ")
    print()
    print("1 - Add Filter")
    print("2 - Select Log File")
    print("3 - Start Reading")
    print("0 - Exit")
    print()

    try:
        choice = input("choice? ")
        choice = int(choice)
        if choice == 1:
            filt_log()
        elif choice == 2:
            Sel_log()
        elif choice == 3:
            main()
        elif choice == 0:
            print("Thank you for using")
            quit()
    except ValueError:
        print(f"{choice} is not a valid choice, exiting program")
        quit()
    except KeyboardInterrupt:
        print("Thank you for using Log Reader")
        quit()
    except Exception as e:
        print(f"Unknown error: {e}")
        quit()

start()