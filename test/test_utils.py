from unittest import TestCase
from query.utils import Utils


class TestUtils(TestCase):
    def test_read_file(self):
        # GIVEN
        file_path = "data/index.json"
        
        # WHEN
        util = Utils()
        file = util.read_json_file(path=file_path)
        
        # THEN
        self.assertIsInstance(util, Utils)
    
    def test_write_file(self):
        # GIVEN
        path = "."
        file = "results.json"
        result = {"result":"result"}
        # WHEN
        util = Utils()
        file = util.write_json_file(path=path, file=file, result=result)
        
        # THEN
        self.assertIsInstance(util, Utils)
