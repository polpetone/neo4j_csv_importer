import configparser

config = configparser.ConfigParser()
config.read("config/config")

csv_node_path = config.get("MAIN", "node_dir")
csv_relationship_path = config.get("MAIN", "relationship_dir")
