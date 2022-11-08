from unittest import TestCase, main
from getdata import DataHandler
from file_load import open_file
from color import bcolors


class TestGetChatById(TestCase):
    def test_get_test_chat_by_id(self):
        cmd = DataHandler()
        data = open_file("ChatAppRawDataJSON.json")
        chat_id = 1
        self.assertEqual(cmd.getChatbyId(data, chat_id), {
            'id': 1,
            'message': 'Hello.',
        })

        chat_id = 5
        self.assertEqual(cmd.getChatbyId(data, chat_id), {
            'id': 5,
            'message': "It's 10:00.",
        })

        chat_id = 9
        self.assertEqual(cmd.getChatbyId(data, chat_id), {
            'id': 9,
            'message': 'Cool.',
        })

    def test_get_chat_by_id_not_found(self):
        cmd = DataHandler()
        data = open_file("ChatAppRawDataJSON.json")
        chat_id = 0
        self.assertEqual(
            cmd.getChatbyId(data, chat_id),
            bcolors.FAIL +f"No Chat with id: {chat_id}" + bcolors.ENDC
        )

        chat_id = 10
        self.assertEqual(
            cmd.getChatbyId(data, chat_id),
            bcolors.FAIL + f"No Chat with id: {chat_id}" + bcolors.ENDC
        )

    def test_wrong_key(self):
        cmd = DataHandler()
        data = open_file("wrong_key.json")
        chat_id = 3
        self.assertEqual(cmd.getChatbyId(data, chat_id),
            {'id': 3, 'message': 'How are you?'})

        chat_id = 4
        self.assertEqual(cmd.getChatbyId(data, chat_id), 
            bcolors.FAIL + f"No Chat with id: {chat_id}" + bcolors.ENDC)
        chat_id = 5
        self.assertEqual(cmd.getChatbyId(data, chat_id), 
            bcolors.FAIL + f"No Chat with id: {chat_id}" + bcolors.ENDC)
        chat_id = 6
        self.assertEqual(cmd.getChatbyId(data, chat_id), 
            bcolors.FAIL + f"No Chat with id: {chat_id}" + bcolors.ENDC)

        chat_id = 7
        self.assertEqual(cmd.getChatbyId(data, chat_id),
            {'id': 7, 'message': "What's up?"})
        chat_id = 8
        self.assertEqual(cmd.getChatbyId(data, chat_id),
            {'id': 8, 'message': "Nothing much."})
        chat_id = 9
        self.assertEqual(cmd.getChatbyId(data, chat_id),
            {'id': 9, 'message': "Cool."})

class TestGetAllChatInRoom(TestCase):
    def test_all_chat_in_room(self):
        cmd = DataHandler()
        data = open_file("ChatAppRawDataJSON.json")
        room_id = 1
        self.assertEqual(cmd.getAllChatInRoom(data, room_id), [
            {'id': 1, 'message': 'Hello.'},
            {'id': 2, 'message': 'Hi.'},
            {'id': 3, 'message': 'How are you?'},
        ])

        room_id = 2
        self.assertEqual(cmd.getAllChatInRoom(data, room_id), [
            {'id': 4, 'message': "What time is it?"},
            {'id': 5, 'message': "It's 10:00."},
            {'id': 6, 'message': "Thanks."},
        ])

        room_id = 3
        self.assertEqual(cmd.getAllChatInRoom(data, room_id), [
            {'id': 7, 'message': "What's up?"},
            {'id': 8, 'message': "Nothing much."},
            {'id': 9, 'message': "Cool."},
        ])

        room_id = 4
        self.assertEqual(
            cmd.getAllChatInRoom(data, room_id),
            bcolors.FAIL + f"No Room with id: {room_id}" + bcolors.ENDC
        )

    def test_wrong_key(self):
        cmd = DataHandler()
        data = open_file("wrong_key.json")
        room_id = 1
        self.assertEqual(cmd.getAllChatInRoom(data, room_id), [
            {'id': 1, 'message': 'Hello.'},
            {'id': 2, 'message': 'Hi.'},
            {'id': 3, 'message': 'How are you?'},
        ])

        room_id = 2
        self.assertRaises(KeyError, cmd.getAllChatInRoom, data, room_id)

        room_id = 3
        self.assertEqual(cmd.getAllChatInRoom(data, room_id), [
            {'id': 7, 'message': "What's up?"},
            {'id': 8, 'message': "Nothing much."},
            {'id': 9, 'message': "Cool."},
        ])


if __name__ == '__main__':
    main(verbosity=2)
