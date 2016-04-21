import argparse
import os

from config import constants


class ConfigurationManager:

    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("csv_node_path")
        self.parser.add_argument("csv_relationship_path")
        self.parser.add_argument("-s", action='store_true')
        self.parser.add_argument("-t", action='store_true')
        self.args = self.parser.parse_args()

    def read_data_path_arguments(self):

        if self.args.csv_node_path[0] == "/":
            csv_node_path = self.args.csv_node_path + "/"
        else:
            csv_node_path = os.getcwd() + "/" + self.args.csv_node_path + "/"

        if self.args.csv_relationship_path[0] == "/":
            csv_relationship_path = self.args.csv_relationship_path + "/"
        else:
            csv_relationship_path = os.getcwd() + "/" + self.args.csv_relationship_path + "/"

        return csv_node_path, csv_relationship_path

    def read_separator_option(self):

        if self.args.t is False and self.args.s is False:
            return constants.COMMA_SEPARATOR
        if self.args.t is True and self.args.s is False:
            return constants.TAB_SEPARATOR
        if self.args.t is True and self.args.s is True:
            return constants.TAB_SEPARATOR
        if self.args.t is False and self.args.s is True:
            return constants.SEMICOLON_SEPARATOR





