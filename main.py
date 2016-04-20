from persistence.NeoGraph import graph
from importer.csv_node_importer import import_nodes_from_csv_files
from importer.csv_relationship_importer import import_relationships_from_csv_files
from argument_parser.argument_parser import read_data_path_arguments


def import_csv_data(csv_node_path, csv_relationship_path):
    graph.delete_all()

    node_files = import_nodes_from_csv_files(csv_node_path)
    relationship_files = import_relationships_from_csv_files(csv_relationship_path)

    return node_files, relationship_files


if __name__ == '__main__':
    node_path, relationship_path = read_data_path_arguments()

    print("Import Nodes from ", node_path)
    print("Import Relationships from ", relationship_path)

    imported_node_files, imported_relationship_files \
        = import_csv_data(csv_node_path=node_path, csv_relationship_path=relationship_path)

    print("Imported Node Files", imported_node_files)
    print("Imported Relationship Files", imported_relationship_files)

