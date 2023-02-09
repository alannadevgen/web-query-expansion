import json
import os


class Utils:
    def __init__(self) -> None:
        pass

    def read_json_file(self, path):
        with open(path, 'r') as json_file:
            json_data = json.loads(json_file.read())
            return json_data

    def write_json_file(self, path, file, result):
        with open(os.path.join(path, file), 'w') as file:
            file.write(
                json.dumps(
                    result,
                    ensure_ascii=False,
                    indent=4
                )
            )
