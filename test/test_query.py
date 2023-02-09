from unittest import TestCase
from query.query import Query


class TestQuery(TestCase):
    def test_query_instance(self):
        # GIVEN
        index = "data/index.json"
        documents = "data/index.json"
        
        # WHEN
        query = Query(query="loyers", index=index, documents=documents)
        
        
        # THEN
        self.assertIsInstance(query, Query)