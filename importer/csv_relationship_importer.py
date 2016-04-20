from util.file_utils import read_files_from_directory
from persistence.NeoGraph import graph
from persistence.GraphManager import relation
from persistence.GraphManager import find_node


data_path = data_path = "/home/icke/workspace/neo_importer/csv_data_relationships/"
data_url = "file://" + data_path


def load_rows(url):
    load_query = """
        LOAD CSV WITH HEADERS FROM " """+url+""" " AS row
        RETURN row
    """
    rows = graph.cypher.execute(load_query)
    return rows


def create_relationships():

    files = read_files_from_directory(data_path)

    for file in files:

        relationships = load_rows(data_url+file)

        for relationship in relationships:
            source_name = relationship.row["source.name"]
            source_label = relationship.row["source.label"]

            destination_name = relationship.row["destination.name"]
            destination_label = relationship.row["destination.label"]

            relationship_type = relationship.row["relationship"]

            source_node = find_node(source_label, source_name)
            destination_node = find_node(destination_label, destination_name)

            relation(source_node, relationship_type, destination_node)






