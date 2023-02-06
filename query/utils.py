import json
import os
from typing import Dict


class Utils:
    def __init__(self) -> None:
        pass

    def read_json_file(self, path):
        with open(path, 'r') as json_file:
            json_data = json.loads(json_file.read())
            return json_data
