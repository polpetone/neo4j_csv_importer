from persistence.neo4j_graph import graph
from util.file_utils import read_file_names_from_directory_filtered_by_suffix
from logger.logger import logger
import py2neo


def build_query_for(file_name, uri, separator):

    label = file_name.split('.')[0]

    query = """
    LOAD CSV WITH HEADERS FROM " """ + uri + """ " AS row
    FIELDTERMINATOR '"""+separator+"""'
    CREATE (n:""" + label + """ )
    SET n = row
    """

    logger.debug(query)

    return query


def build_unique_constraint_query(file_name):

    label = file_name.split('.')[0]

    query = """
        CREATE CONSTRAINT ON (n:"""+label+""") ASSERT n.name IS UNIQUE
    """
    return query


def import_nodes_from_csv_files(csv_node_path, separator=','):
    file_names = read_file_names_from_directory_filtered_by_suffix(csv_node_path, ".csv")

    for file_name in file_names:
        url = "file://" + csv_node_path + file_name
        query = build_query_for(file_name, url, separator)
        unique_constraint_query = build_unique_constraint_query(file_name)
        try:
            graph.cypher.execute(unique_constraint_query)
            graph.cypher.execute(query)
        except py2neo.cypher.error.schema.ConstraintViolation as constraintViolation:
            logger.error(constraintViolation)

    return file_names


