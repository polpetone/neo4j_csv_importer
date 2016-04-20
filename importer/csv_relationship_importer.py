from util.file_utils import read_file_names_from_directory
from persistence.NeoGraph import graph
from persistence.GraphManager import create_relationship
from persistence.GraphManager import find_node


def load_rows(uri):
    load_query = """
        LOAD CSV WITH HEADERS FROM " """ + uri + """ " AS row
        RETURN row
    """
    rows = graph.cypher.execute(load_query)
    return rows


def import_relationships_from_csv_files(csv_relationship_path):

    file_names = read_file_names_from_directory(csv_relationship_path)

    for file_name in file_names:

        uri = "file://" + csv_relationship_path + file_name
        relationships = load_rows(uri)

        for relationship in relationships:
            source_name = relationship.row["source.name"]
            source_label = relationship.row["source.label"]

            destination_name = relationship.row["destination.name"]
            destination_label = relationship.row["destination.label"]

            relationship_type = relationship.row["relationship"]

            source_node = find_node(source_label, source_name)
            destination_node = find_node(destination_label, destination_name)

            create_relationship(source_node, relationship_type, destination_node)

    return file_names






