from color import bcolors


class DataHandler():
	def getRoomById(self, data):
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

	def getAllRoom(self, data):
		rooms = []
		for room in data:
			rooms.append({"id": room['id'], "name": room["name"]})
		print(rooms)

	def getChatbyId(self, data):
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

	def getAllChatInRoom(self, data):
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