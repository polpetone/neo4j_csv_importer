from util.file_utils import read_file_names_from_directory_filtered_by_suffix
from persistence.neo4j_graph import graph
from persistence.graph_management import create_relationship
from persistence.graph_management import find_node
from logger.logger import logger


def load_rows(uri):
    load_query = """
        LOAD CSV WITH HEADERS FROM " """ + uri + """ " AS row
        RETURN row
    """
    rows = graph.cypher.execute(load_query)
    return rows


def import_relationships_from_csv_files(csv_relationship_path):

    file_names = read_file_names_from_directory_filtered_by_suffix(csv_relationship_path, ".csv")

    for file_name in file_names:

        uri = "file://" + csv_relationship_path + file_name
        relationships = load_rows(uri)

        for relationship in relationships:
            source_name = relationship.row["source.name"]
            source_label = relationship.row["source.label"]

            destination_name = relationship.row["destination.name"]
            destination_label = relationship.row["destination.label"]

            relationship_type = relationship.row["relationship"]

            try:
                source_node = find_node(source_label, source_name)
                destination_node = find_node(destination_label, destination_name)
                create_relationship(source_node, relationship_type, destination_node)
            except AttributeError as attribute_error:
                logger.warn("Could not create relationship for %s %s Error: %s",
                            source_label, source_name, attribute_error)

    return file_names






