import json
import sys
from color import bcolors
from getdata import DataHandler
from file_load import init_data


def print_menu():
    """
    It prints the menu and returns the user's choice
    :return: The menu is being returned.
    """
    menu = """
Action
1. Initialize data
2. getRoomById
3. getAllRoom
4. getChatbyId
5. getAllChatInRoom
0. Exit

    """

    print(menu)
    return int(input("Select the action: "))


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
        try:
            room_id = int(input("getRoomById: "))
            if room_id <= 0:
                raise ValueError
            print(cmd.getRoomById(data, room_id))
        except ValueError:
            print(bcolors.FAIL + "Invalid input" + bcolors.ENDC)
            return
    elif action == 3:
        print(cmd.getAllRoom(data))
    elif action == 4:
        try:
            chat_id = int(input("getChatbyId: "))
            if chat_id <= 0:
                raise ValueError
        except ValueError:
            print(bcolors.FAIL + "Invalid input" + bcolors.ENDC)
            return
        print(cmd.getChatbyId(data, chat_id))
    elif action == 5:
        try:
            room_id = int(input("getAllChatInRoom: "))
            if room_id <= 0:
                raise ValueError
        except ValueError:
            print(bcolors.FAIL + "Invalid input" + bcolors.ENDC)
            return
        print(cmd.getAllChatInRoom(data, room_id))
    else:
        print(bcolors.WARNING + "Invalid action" + bcolors.ENDC)


def main():
    data = None
    while True:
        try:
            action = print_menu()
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
            except json.decoder.JSONDecodeError:
                print(bcolors.FAIL + "Invalid JSON file" + bcolors.ENDC)
            except FileNotFoundError:
                print(bcolors.FAIL + "File not found" + bcolors.ENDC)
            except ValueError:
                print(bcolors.FAIL + "Nothing in JSON" + bcolors.ENDC)
            if data:
                print(bcolors.OKGREEN + "Data initialized" + bcolors.ENDC)
        else:
            if data is None:
                print(bcolors.FAIL + "Please initialize data first" + bcolors.ENDC)
            else:
                check_action(action, data, cmd)


if "__main__" == __name__:
    main()
