import argparse
import os

def read_data_path_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_node_path")
    parser.add_argument("csv_relationship_path")
    args = parser.parse_args()

    if args.csv_node_path[0] == "/":
        csv_node_path = args.csv_node_path + "/"
    else:
        csv_node_path = os.getcwd() + "/" + args.csv_node_path + "/"

    if args.csv_relationship_path[0] == "/":
        csv_relationship_path = args.csv_relationship_path + "/"
    else:
        csv_relationship_path = os.getcwd() + "/" + args.csv_relationship_path + "/"

    return csv_node_path, csv_relationship_path
