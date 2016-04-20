from persistence.NeoGraph import graph
from util.file_utils import read_files_from_directory

data_path = data_path = "/home/icke/workspace/neo_importer/csv_data_nodes/"
data_url = "file://" + data_path


def build_query_for(file, url):

    label = file.split('.')[0]

    load_query = """
    LOAD CSV WITH HEADERS FROM " """ + url + """ " AS row
    CREATE (n:""" + label + """ )
    SET n = row
    """
    return load_query


def import_nodes_from_csv_files():
    files = read_files_from_directory(data_path)

    for file in files:
        url = data_url + file
        query = build_query_for(file, url)
        graph.cypher.execute(query)



