from color import bcolors


# > This class is used to handle data from json file
class DataHandler():
    def getRoomById(self, data: list, room_id: int):
        """
        It takes a list of dictionaries and an integer as arguments and returns a dictionary with the
        key-value pairs of the room with the matching id
        
        :param data: list - this is the list of rooms that we're going to search through
        :type data: list
        :param room_id: The id of the room you want to get
        :type room_id: int
        :return: A dictionary with the room id and name.
        """
        if not isinstance(data, list):
            raise TypeError
        for room in data:
            if list(room.keys())[0] != 'id':
                continue
            if room['id'] == room_id:
                return {"id": room['id'], "name": room["name"]}
        return bcolors.FAIL + f"No Room with id: {room_id}" + bcolors.ENDC

    def getAllRoom(self, data: list):
        """
        It takes in a list of dictionaries, and returns a list of dictionaries

        :param data: The data that is returned from the API call
        """
        if not isinstance(data, list):
            raise TypeError
        rooms = []
        for room in data:
            rooms.append({"id": room['id'], "name": room["name"]})
        return(rooms)

    def getChatbyId(self, data: list, chat_id: int):
        """
        It takes a list of dictionaries, and a chat_id, and prints the message of the chat with the
        given chat_id
        
        :param data: list - the list of rooms
        :type data: list
        :param chat_id: The id of the chat you want to get
        :type chat_id: int
        :return: The chat with the given id.
        """
        if not isinstance(data, list):
            raise TypeError
        for room in data:
            for chat in room['chats']:
                for key, _ in chat.items():
                    if key not in ('id', 'message'):
                        break
                    if chat['id'] == chat_id:
                        return {"id": chat_id, "message": chat["message"]}
        return bcolors.FAIL + f"No Chat with id: {chat_id}" + bcolors.ENDC

    def getAllChatInRoom(self, data: list, room_id: int):
        """
        It takes a list of rooms, and prints all the chats in a room with a given id

        :param data: list
        :type data: list
        :return: A list of all the chats in the room with the given id.
        """
        if not isinstance(data, list):
            raise TypeError
        for room in data:
            for key, _ in room.items():
                if key not in ('id', 'chats'):
                    break
                if room['id'] == room_id:
                    for key, message in [chat.items() for chat in room['chats']]:
                        if key[0] != 'id' or message[0] != 'message':
                            raise KeyError
                        return room['chats']
        return bcolors.FAIL + f"No Room with id: {room_id}" + bcolors.ENDC
