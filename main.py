from query.utils import Utils
from query.query import Query
import click


@click.command()
@click.option("--index", default="data/index.json", type=str, help="Path to index file.")
@click.option("--documents", default="data/documents.json", type=str, help="Path to documents file.")
@click.option("--query", default="recette de cuisine", type=str, help="Type your query.")
def main(
    index,
    documents,
    query
):
    utils = Utils()
    my_index = utils.read_json_file(index)
    my_docs = utils.read_json_file(documents)

    user_query = Query(
        query=str(query),
        index=my_index,
        documents=my_docs
    )
    user_query.rank()


if __name__ == "__main__":
    main()
