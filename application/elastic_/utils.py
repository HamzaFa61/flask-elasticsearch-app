import json
from from_root import from_root
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk


def create_index_if_not_exists(index_name: str, es_client: Elasticsearch, mapping: dict):
    if not es_client.indices.exists(index=index_name):
        es_client.indices.create(index=index_name, body=mapping)


def index_data(es_client: Elasticsearch, index_name: str, doc_type: str):
    # check if data is already indexed
    if es_client.count(index=index_name)['count'] == 0:
        # read data from JSON file using ijson
        with open(from_root('news_dataset.json'), 'r') as f:
            news_data = [json.loads(line) for line in f]

        # bulk index all documents in Elasticsearch
        actions = [
            {
                "_index": index_name,
                "_type": doc_type,
                "_source": doc
            }
            for doc in news_data
        ]
        bulk(es_client, actions)