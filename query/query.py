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
        documents_id = set()
        for token in self.tokens:
            if token in self.index.keys():
                for document_id in self.index[token].keys():
                    if document_id not in documents_id:
                        documents_id.add(int(document_id))
        self.found_documents = sorted(documents_id)
