from unittest import TestCase
from query.query import Query
from query.utils import Utils


class TestQuery(TestCase):
    def test_query_instance(self):
        # GIVEN
        index = "data/index.json"
        documents = "data/index.json"

        # WHEN
        query = Query(query="loyers", index=index, documents=documents)

        # THEN
        self.assertIsInstance(query, Query)

    def test_tokenize(self):
        # GIVEN
        index = "data/index.json"
        documents = "data/index.json"

        # WHEN
        query = Query(query="révision des loyers",
                      index=index, documents=documents)
        query.tokenize_query()

        # THEN
        self.assertIsInstance(query, Query)
        self.assertSequenceEqual(query.tokens, ["révision", "loyers"])

    def test_find_token_in_document(self):
        # GIVEN
        utils = Utils()
        index = utils.read_json_file("data/index.json")
        documents = utils.read_json_file("data/documents.json")

        # WHEN
        query = Query(query="loyers", index=index, documents=documents)
        query.tokenize_query()
        query.find_token_in_document()

        # THEN
        self.assertIsInstance(query, Query)
        self.assertEqual(
            query.found_documents,
            {
                "loyers": {"214": {"positions": [4], "count": 1}, "295": {"positions": [5], "count": 1}}
            }
        )
    
    def test_rank_documents_from_index(self):
        # GIVEN
        utils = Utils()
        index = utils.read_json_file("data/index.json")
        documents = utils.read_json_file("data/documents.json")

        # WHEN
        query = Query(query="loyers", index=index, documents=documents)
        query.tokenize_query()
        query.find_token_in_document()
        query.rank_documents_from_index()

        # THEN
        self.assertIsInstance(query, Query)
        self.assertEqual(
            query.ranked_documents,
            {
                "214": 1,
                "295": 1
            }
        )

    def test_rank_documents_from_index(self):
        # GIVEN
        utils = Utils()
        index = utils.read_json_file("data/index.json")
        documents = utils.read_json_file("data/documents.json")

        # WHEN
        query = Query(query="loyers", index=index, documents=documents)
        query.tokenize_query()
        query.find_token_in_document()
        query.rank_documents_from_index()

        # THEN
        self.assertIsInstance(query, Query)
        self.assertEqual(
            query.ranked_documents,
            {
                "214": 1,
                "295": 1
            }
        )
    
    def test_get_documents_from_ranking(self):
        # GIVEN
        utils = Utils()
        index = utils.read_json_file("data/index.json")
        documents = utils.read_json_file("data/documents.json")

        # WHEN
        query = Query(query="loyers", index=index, documents=documents)
        query.tokenize_query()
        query.find_token_in_document()
        query.rank_documents_from_index()
        query.get_documents_from_ranking()

        # THEN
        self.assertIsInstance(query, Query)
        self.assertEqual(
            query.result,
            [
                {'title': 'Indice de référence des loyers (IRL) | Service-public.fr', 'url': 'https://www.service-public.fr/particuliers/actualites/A12956?xtor=RSS-111'},
                {'title': "    IRL Indice de référence des loyers de l'INSEE    ", 'url': 'https://bail.dispofi.fr/IRL-indice-reference-loyers'}
            ]
        )
