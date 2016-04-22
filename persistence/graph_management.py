from persistence.neo4j_graph import graph
from py2neo import Relationship


def create_relationship(source, relation_type, destination, **properties):
    graph.create_unique(Relationship(source, relation_type, destination, **properties))


def find_node(label, name):
    return graph.find_one(label, property_key="name", property_value=name)
