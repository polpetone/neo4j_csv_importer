 //   ) )
   //___/ /  ___     //  ___      ___    __  ___  ___       __      ___
  / ____ / //   ) ) // //   ) ) //___) )  / /   //   ) ) //   ) ) //___) )
 //       //   / / // //___/ / //        / /   //   / / //   / / //
//       ((___/ / // //       ((____    / /   ((___/ / //   / / ((____


Neo4j_csv_importer

Preconditions:
- running neo4j on localhost
	- no authentication supported yet
- directory for node data: files has to have csv as suffix
- directory for relationships: separator has to be a comma
- python 3
- py2neo

What it does:
- imports data from csv files into a neo4j
How:
- one directory for nodes
- one directory for relationships
- filename is label name of node

Import of Nodes:
- header of csv file are node properties
- Notice: at the moment there must be one property called name (on header column)

Import of Relationships
- header must have following format: source.name,source.label,relationship,destination.name,destination.label
- name and label must exist
- relationship can be anything
- separator has to be a comma


Options:
- csv files for nodes can have three types of separators: semicolon, comma, tab
- default is comma

Usages:
$ python neo4j_csv_importer.py <node_dir> <relationship_dir>

    Where:
    <node_dir>
    /absolute/path/node_data
    OR
    relative/path/node_data

    <relationship_dir>
    /absolute/path/relationship_data
    OR
    relative/path/relationship_data

Example:
- there are a small sample set of csv data in test_data
- python neo4j_csv_importer.py test_data/csv_nodes test_data/csv_relationships
- this will create some city and person nodes and creates LIVE_IN relationship between them
- open localhost:7474 (default config of neo4j) and watch the result




