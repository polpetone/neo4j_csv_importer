from persistence.NeoGraph import graph
from importer.csv_node_importer import import_nodes_from_csv_files
from importer.csv_relationship_importer import create_relationships

graph.delete_all()
import_nodes_from_csv_files()
create_relationships()