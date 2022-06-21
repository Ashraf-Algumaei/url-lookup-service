from typing import List
import azure.cosmos.cosmos_client as cosmos_client

from azure.cosmos import documents


class CosmosClientManager:
    """
    Encapsulates cosmos client creation for other services to use
    """

    def __init__(self, host_url: str, master_key: str, database: str, container: str):
        self.host = host_url
        self.master_key = master_key
        self.connectionPolicy = documents.ConnectionPolicy()
        self.cosmos_client = cosmos_client.CosmosClient(self.host, {'masterKey': self.master_key},
                                                        documents.ConsistencyLevel.Eventual,
                                                        connection_policy=self.connectionPolicy)
        self.database_client = self.cosmos_client.get_database_client(database)
        self.url_container_client = self.database_client.get_container_client(container)

    def get_record(self, item_id: str, partition_key: str) -> dict:
        """Returns Cosmos DB record based on item_id and partition_key

        Args:
            item_id: Cosmos Record Id
            parition_key: Cosmos Partition key
        """
        record = self.url_container_client.read_item(item=item_id, partition_key=partition_key)

        return record
