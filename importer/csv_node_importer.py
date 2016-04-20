from persistence.NeoGraph import graph
from util.file_utils import read_file_names_from_directory


def build_query_for(file_name, uri):

    label = file_name.split('.')[0]

    query = """
    LOAD CSV WITH HEADERS FROM " """ + uri + """ " AS row
    CREATE (n:""" + label + """ )
    SET n = row
    """
    return query


def import_nodes_from_csv_files(csv_node_path):
    file_names = read_file_names_from_directory(csv_node_path)

    for file_name in file_names:
        url = "file://" + csv_node_path + file_name
        query = build_query_for(file_name, url)
        graph.cypher.execute(query)
    return file_names


