from chatterbot.storage import StorageAdapter
from py2neo import Graph, Node

class Neo4jStorageAdapter(StorageAdapter):
    _graph = None

    @classmethod
    def _get_graph(cls, uri):
        if cls._graph is None:
            cls._graph = Graph(uri)
        return cls._graph

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.uri = kwargs.get('uri', 'bolt://localhost:7687')
        self.graph = self._get_graph(self.uri)

    def create(self, **kwargs):
        statement_node = Node("Statement", **kwargs)
        self.graph.create(statement_node)
        return statement_node

    def get_random(self):
        query = "MATCH (s:Statement) RETURN s, rand() as r ORDER BY r LIMIT 1"
        result = self.graph.run(query).evaluate()
        return result

    def count(self):
        query = "MATCH (s:Statement) RETURN COUNT(s) AS statementCount"
        result = self.graph.run(query).data()
        return result[0]["statementCount"]

    def filter(self, **kwargs):
        query = "MATCH (s:Statement) WHERE "
        conditions = []

        for key, value in kwargs.items():
            conditions.append(f"s.{key} = '{value}'")

        query += " AND ".join(conditions)
        query += " RETURN s"

        result = self.graph.run(query).data()
        return [record["s"] for record in result]

    def remove(self, statement_text):
        query = f"MATCH (s:Statement {{text: '{statement_text}'}}) DELETE s"
        self.graph.run(query)

    def drop(self):
        query = "MATCH (s:Statement) DETACH DELETE s"
        self.graph.run(query)

# Usage:
# neo4j_adapter = Neo4jStorageAdapter(uri='bolt://localhost:7687')
# neo4j_adapter.create(text='Hello', in_response_to='Hi')
# random_statement = neo4j_adapter.get_random()
# count = neo4j_adapter.count()
# filtered_statements = neo4j_adapter.filter(in_response_to='Hi')
# neo4j_adapter.remove(statement_text='Hello')
# neo4j_adapter.drop()
