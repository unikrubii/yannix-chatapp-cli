from json.decoder import JSONDecodeError
from unittest import TestCase
from file_load import open_file


class TestInitData(TestCase):
    def test_file_not_found(self):
        """
        It tests if the file is false.
        """
        self.assertRaises(FileNotFoundError, open_file, "ChatAppRawDataJSONFalse.json")

    def test_invalid_file(self):
        """
        It tests if the file is invalid.
        """
        self.assertRaises(JSONDecodeError, open_file, "not_json.txt")

    def test_open_file(self):
        """
        It tests the open_file function.
        """
        self.assertEqual(open_file("ChatAppRawDataJSON.json"), [
            {
                'id': 1,
                'name': 'Party Room',
                'chats': [
                    {'id': 1, 'message': "Hello."},
                    {'id': 2, 'message': "Hi."},
                    {'id': 3, 'message': "How are you?"}
                    ]
            },
            {
                'id': 2,
                'name': 'Secret Room',
                'chats': [
                    {'id': 4, 'message': "What time is it?"},
                    {'id': 5, 'message': "It's 10:00."},
                    {'id': 6, 'message': "Thanks."}
                    ]
            },
            {
                'id': 3,
                'name': 'Open Room',
                'chats': [
                    {'id': 7, 'message': "What's up?"},
                    {'id': 8, 'message': "Nothing much."},
                    {'id': 9, 'message': "Cool."}
                    ]
            }
            ])
