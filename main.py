from config.ConfigurationManager import ConfigurationManager
from importer.csv_node_importer import import_nodes_from_csv_files
from importer.csv_relationship_importer import import_relationships_from_csv_files
from logger.logger import logger
from persistence.NeoGraph import graph


def import_csv_data(csv_node_path, csv_relationship_path):
    graph.delete_all()

    node_files = import_nodes_from_csv_files(csv_node_path)
    relationship_files = import_relationships_from_csv_files(csv_relationship_path)

    return node_files, relationship_files


if __name__ == '__main__':

    configurationManager = ConfigurationManager()

    node_path, relationship_path = configurationManager.read_data_path_arguments()
    separator = configurationManager.read_separator_option()

    logger.info("Using Separator for Node Csv Files %s", separator)

    logger.info("Import Nodes from %s", node_path)
    logger.info("Import Relationships from %s", relationship_path)

    imported_node_files, imported_relationship_files \
        = import_csv_data(csv_node_path=node_path, csv_relationship_path=relationship_path)

    logger.info("Imported Relationship Files %s", str(imported_relationship_files).strip('[]'))
    logger.info("Imported Node Files %s",  str(imported_node_files).strip('[]'))





