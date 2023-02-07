import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
import re

LANGUAGES = {
    "fr": "french",
    "en": "english"
}

class Query:
    def __init__(self, query, index, documents, lang='fr') -> None:
        self.query = query
        self.index = index
        self.documents = documents
        self.stop_words = stopwords.words(LANGUAGES[lang])
        self.pattern = re.compile(r'([؟!\?]+|[:\.،؛»\]\)\}"«\[\(\{])')
        self.tokens = []


    def tokenize_query(self):
        '''
        Tokenizes a query by returning its tokens

        Parameters
        ----------
        text : str
            query text
        
        Returns
        -------
        list
            tokens of the query splitted by space (deleting the stop words)
        '''
        text = self.pattern.sub(r' \1 ', self.query.replace('\n', ' ').replace('\t', ' '))
        self.tokens = [word.lower() for word in text.split(' ') if word not in self.stop_words]        

    def find_token_in_document(self):
        documents_ids = []
        documents = {}
        for token in self.tokens:
            if token in self.index.keys():
                for document_id in self.index[token].keys():
                    # if document_id not in documents_ids:
                    documents_ids.append(document_id)
                    documents[token] = self.index[token]
        if documents:
            self.found_documents = documents
            print(self.found_documents)
        # if no token found in index
        else:
            self.found_documents = None

    def find_documents_from_index(self):
        ranked_documents = {}
        for token in self.found_documents:
            for document in self.found_documents[token]:
                if document in ranked_documents:
                    ranked_documents[document] += self.found_documents[token][document]['count']
                else:
                    ranked_documents[document] = self.found_documents[token][document]['count']
