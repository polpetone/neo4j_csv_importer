         _          _            _             _          _          _            _            _             _
        /\ \       /\ \         _\ \          /\ \       /\ \       /\ \         /\ \         /\ \     _    /\ \
       /  \ \     /  \ \       /\__ \        /  \ \     /  \ \      \_\ \       /  \ \       /  \ \   /\_\ /  \ \
      / /\ \ \   / /\ \ \     / /_ \_\      / /\ \ \   / /\ \ \     /\__ \     / /\ \ \     / /\ \ \_/ / // /\ \ \
     / / /\ \_\ / / /\ \ \   / / /\/_/     / / /\ \_\ / / /\ \_\   / /_ \ \   / / /\ \ \   / / /\ \___/ // / /\ \_\
    / / /_/ / // / /  \ \_\ / / /         / / /_/ / // /_/_ \/_/  / / /\ \ \ / / /  \ \_\ / / /  \/____// /_/_ \/_/
   / / /__\/ // / /   / / // / /         / / /__\/ // /____/\    / / /  \/_// / /   / / // / /    / / // /____/\
  / / /_____// / /   / / // / / ____    / / /_____// /\____\/   / / /      / / /   / / // / /    / / // /\____\/
 / / /      / / /___/ / // /_/_/ ___/\ / / /      / / /______  / / /      / / /___/ / // / /    / / // / /______
/ / /      / / /____\/ //_______/\__\// / /      / / /_______\/_/ /      / / /____\/ // / /    / / // / /_______\
\/_/       \/_________/ \_______\/    \/_/       \/__________/\_\/       \/_________/ \/_/     \/_/ \/__________/


Neo4j_csv_importer

Attention:
- going to delete all existent data in running neo4j instance

Preconditions:
- running neo4j on localhost
- directory for node data: files has to have csv as suffix
- directory for relationships: separator has to be a comma
- python 3
- py2neo

What it does:
- imports data from csv files into a neo4j

- one directory for nodes
- one directory for relationships

Options:
- csv files for nodes can have three types of separators: semicolon, comma, tab

Usages:
$ python 3 neo4j_csv_importer.py <node_dir> <relationship_dir>

Where:
<node_dir> is
- absolute path to directory of csv files with nodes
OR
- relative path to directory of csv file with nodes

-filename is label name of node

<relationship_dir> is
- absolute path to directory of csv files with relationships
OR
- relative path to directory of csv files with relationships






