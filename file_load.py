import json


def open_file(path: str):
    """
    It opens a file and returns the data in it

    :param path: str
    :type path: str
    :return: A dictionary
    """
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
        if data == [] or data == {}:
            raise ValueError
        return data


def init_data():
    """
    It reads the data from the file and returns it.
    """
    path = input("Initialize data with file path (default: ChatAppRawDataJSON.json): ")
    if path == "":
        path = "ChatAppRawDataJSON.json"
    return open_file(path)
