run:
	python3 chatapp.py

test_init:
	python3 -m unittest test/test_init_data.py

test_room:
	python3 -m unittest test/test_get_room.py

test_chat:
	python3 -m unittest test/test_get_chat.py

.PHONY: run test_init test_room test_chat
