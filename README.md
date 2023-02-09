# Web query expansion

The aim of this project is to build a query ranking tool. A user types in a query and a list of relevant documents is returned. These documents are web pages that are described by their title and their URL. The results of the user's query are printed and stored in a `results.json` file by default. The documents are sorted by relevancy.

## Quick start

First, you will need to clone the repo.
```bash
git clone https://github.com/alannagenin/web-query.git
cd web-query
```

Then, we will set a virtual environment.
```python
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
Once everything is set up, we can run the ranking process through the CLI. Multiple options can be used, you can see them through the following command.

```bash
python3 main.py --help
# Usage: main.py [OPTIONS]

# Options:
#   --index TEXT      Path to index file.
#   --documents TEXT  Path to documents file.
#   --query TEXT      Type your query.
#   --path TEXT       Path to ouput results of the query.
#   --file TEXT       File name to ouput results of the query.
#   --lang [fr|en]    Language of the query.
#   --help            Show this message and exit.
```

By default, the values are:
* `--index` "data/index.json" $\rightarrow$ Default index
* `--documents` "data/documents.json" $\rightarrow$ Default documents
* `--query` "recette de cuisine" $\rightarrow$ Query for cooking recipes
* `--path` "." $\rightarrow$ Output results at the root of the project
* `--file` "results.json" $\rightarrow$ Output query results in `results.json` file
* `--lang` "fr" $\rightarrow$ French

## Contributors

[Alanna DEVLIN-GENIN](https://github.com/alannagenin)