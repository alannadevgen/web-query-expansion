import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
import re

LANGUAGES = {
    "fr": "french",
    "en": "english"
}

class Query:
    def __init__(self, query, lang='fr') -> None:
        self.query = query
        self.stop_words = stopwords.words(LANGUAGES[lang])
        self.pattern = re.compile(r'([؟!\?]+|[:\.،؛»\]\)\}"«\[\(\{])')


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
        tokens = [word.lower() for word in text.split(' ') if word not in self.stop_words]
        return tokens

    def find_documents_from_index(self):
        pass


if __name__ == "__main__":
    query = Query(query="Karine Lacombe")
    print(query.tokenize_query())