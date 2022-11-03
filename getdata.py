from color import bcolors


class DataHandler():
	def getRoomById(self, data):
		room_id = input("getRoomById: ")
		for room in data:
			if room['id'] == room_id:
				print({"id": room_id, "name": room["name"]})
				return
		print(bcolors.FAIL + f"No Room with id: {room_id}" + bcolors.ENDC)

	def getAllRoom(self, data):
		rooms = []
		for room in data:
			rooms.append({"id": room['id'], "name": room["name"]})
		print(rooms)

	def getChatbyId(self, data):
		chat_id = int(input("getChatbyId: "))
		for room in data:
			for chat in room['chats']:
				if chat['id'] == chat_id:
					print({"id": chat_id, "message": chat["message"]})
					return
		print(bcolors.FAIL + f"No Chat with id: {chat_id}" + bcolors.ENDC)

	def getAllChatInRoom(self, data):
		room_id = input("getAllChatInRoom: ")
		for room in data:
			if room['id'] == room_id:
				print(room['chats'])
				return
		print(bcolors.FAIL + f"No Room with id: {room_id}" + bcolors.ENDC)