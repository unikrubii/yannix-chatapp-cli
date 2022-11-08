from unittest import TestCase, main
from getdata import DataHandler
from file_load import open_file
from color import bcolors


class TestGetRoomById(TestCase):
    def test_get_room_by_id(self):
        """
        It tests the getRoomById function.
        """
        cmd = DataHandler()
        data = open_file("ChatAppRawDataJSON.json")
        self.assertEqual(cmd.getRoomById(data, 1), {
            'id': 1,
            'name': 'Party Room',
        })

        self.assertEqual(cmd.getRoomById(data, 2), {
            'id': 2,
            'name': 'Secret Room',
        })

        self.assertEqual(cmd.getRoomById(data, 3), {
            'id': 3,
            'name': 'Open Room',
        })

    def test_get_room_by_id_not_found(self):
        """
        It tests the getRoomById function if the room is not found.
        """
        cmd = DataHandler()
        data = open_file("ChatAppRawDataJSON.json")
        room_id = 4
        self.assertEqual(
            cmd.getRoomById(data, room_id),
            bcolors.FAIL + f"No Room with id: {room_id}" + bcolors.ENDC
        )

        room_id = 5
        self.assertEqual(
            cmd.getRoomById(data, room_id),
            bcolors.FAIL + f"No Room with id: {room_id}" + bcolors.ENDC
        )

    def test_get_room_wrong_key(self):
        """
        It tests the getRoomById function if the dict_key is wrong.
        """
        cmd = DataHandler()
        data = open_file("wrong_key.json")
        # Room_id is incorrect
        room_id = 1
        self.assertEqual(cmd.getRoomById(data, room_id),
            bcolors.FAIL + f"No Room with id: {room_id}" + bcolors.ENDC)

        # Room_id is correct but chat_id is incorrect
        room_id = 2
        self.assertEqual(cmd.getRoomById(data, room_id),
            {'id': 2, 'name': 'Secret Room'})
        # Everything is correct
        room_id = 3
        self.assertEqual(cmd.getRoomById(data, room_id),
            {'id': 3, 'name': 'Open Room'})


class TestAllRoom(TestCase):
    def test_get_all_room(self):
        """
        It tests the getAllRoom function.
        """
        cmd = DataHandler()
        data = open_file("ChatAppRawDataJSON.json")
        self.assertEqual(cmd.getAllRoom(data), [
            {'id': 1, 'name': 'Party Room'},
            {'id': 2, 'name': 'Secret Room'},
            {'id': 3, 'name': 'Open Room'},
        ])


if __name__ == '__main__':
    main(verbosity=2)
