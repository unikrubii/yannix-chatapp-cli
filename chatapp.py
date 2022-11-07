import json
import sys
from color import bcolors
from getdata import DataHandler


def Menu():
    """
    It prints the menu and returns the user's choice
    :return: The menu is being returned.
    """
    MENU = """
Action
1. Initialize data
2. getRoomById
3. getAllRoom
4. getChatbyId
5. getAllChatInRoom
0. Exit

    """

    print(MENU)
    return int(input("Select the action: "))


def init_data():
    """
    It takes a file path as input, and returns a dictionary of the data in the file
    :return: The data is being returned.
    """
    path = input("Initialize data with file path (default: ChatAppRawDataJSON.json): ")
    if path == "":
        path = "ChatAppRawDataJSON.json"
    try:
        with open(path, encoding='utf-8') as f:
            data = json.load(f)
            print("Initialize...")
            return data
    except json.decoder.JSONDecodeError:
        print(bcolors.FAIL + "Invalid JSON file" + bcolors.ENDC)
        return None


def check_action(action: int, data: list, cmd: DataHandler):
    
    """
    It checks the action and calls the appropriate function from the DataHandler class

    :param action: The action to be performed
    :type action: int
    :param data: list
    :type data: list
    :param cmd: DataHandler
    :type cmd: DataHandler
    """
    if action == 2:
        cmd.getRoomById(data)
    elif action == 3:
        cmd.getAllRoom(data)
    elif action == 4:
        cmd.getChatbyId(data)
    elif action == 5:
        cmd.getAllChatInRoom(data)
    else:
        print(bcolors.WARNING + "Invalid action" + bcolors.ENDC)


def main():
    action = 1
    data = None
    while action != 0:
        try:
            action = Menu()
        except ValueError:
            print(bcolors.WARNING + "Invalid action" + bcolors.ENDC)
            continue

        cmd = DataHandler()
        if action == 0:
            print(bcolors.BOLD + bcolors.OKCYAN + "Bye" + bcolors.ENDC)
            sys.exit(0)
        if action == 1:
            if data is not None:
                print(bcolors.WARNING + "Data is already initialized" + bcolors.ENDC)
                continue
            try:
                data = init_data()
            except FileNotFoundError:
                print(bcolors.FAIL + "File not found" + bcolors.ENDC)
        else:
            if data is None:
                print(bcolors.FAIL + "Please initialize data first" + bcolors.ENDC)
            else:
                check_action(action, data, cmd)


if "__main__" == __name__:
    main()
