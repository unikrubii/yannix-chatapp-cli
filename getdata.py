from color import bcolors


# > This class is used to handle data from json file
class DataHandler():
    def getRoomById(self, data: list):
        """
        It takes a list of dictionaries, and prints the dictionary with the key 'id'
        that matches the user input

        :param data: The data that is passed to the function
        :return: A list of dictionaries
        """
        try:
            room_id = int(input("getRoomById: "))
            if room_id <= 0:
                raise ValueError
        except ValueError:
            print(bcolors.FAIL + "Invalid input" + bcolors.ENDC)
            return

        for room in data:
            if room['id'] == room_id:
                print({"id": room_id, "name": room["name"]})
                return
        print(bcolors.FAIL + f"No Room with id: {room_id}" + bcolors.ENDC)

    def getAllRoom(self, data: list):
        """
        It takes in a list of dictionaries, and returns a list of dictionaries

        :param data: The data that is returned from the API call
        """
        rooms = []
        for room in data:
            rooms.append({"id": room['id'], "name": room["name"]})
        print(rooms)

    def getChatbyId(self, data: list):
        """
        It takes in a list of dictionaries, and prints out the message of the chat with the given id

        :param data: The data that is passed to the function
        :return: A dictionary with the id and message of the chat with the given id.
        """
        try:
            chat_id = int(input("getChatbyId: "))
            if chat_id <= 0:
                raise ValueError
        except ValueError:
            print(bcolors.FAIL + "Invalid input" + bcolors.ENDC)
            return

        for room in data:
            for chat in room['chats']:
                if chat['id'] == chat_id:
                    print({"id": chat_id, "message": chat["message"]})
                    return
        print(bcolors.FAIL + f"No Chat with id: {chat_id}" + bcolors.ENDC)

    def getAllChatInRoom(self, data: list):
        """
        It takes a list of rooms, and prints all the chats in a room with a given id

        :param data: list
        :type data: list
        :return: A list of all the chats in the room with the given id.
        """
        try:
            room_id = int(input("getAllChatInRoom: "))
            if room_id <= 0:
                raise ValueError
        except ValueError:
            print(bcolors.FAIL + "Invalid input" + bcolors.ENDC)
            return

        for room in data:
            if room['id'] == room_id:
                print(room['chats'])
                return
        print(bcolors.FAIL + f"No Room with id: {room_id}" + bcolors.ENDC)
